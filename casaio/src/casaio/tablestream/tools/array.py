from math import prod
from math import ceil

import numpy as np

from ._casa_chunking import _combine_chunks

def combine_chunks(array_1d, itemsize, shape, oversample):
    if len(shape) < 4:
        shape = tuple(shape) + (1,) * (4 - len(shape))

    if len(oversample) < 4:
        oversample = tuple(oversample) + (1,) * (4 - len(oversample))

    native_shape = [s // o for (s, o) in zip(shape, oversample)]

    return _combine_chunks(np.ascontiguousarray(array_1d), itemsize, *native_shape[::-1], *oversample[::-1])

class ArrayWrapper:
    """
    A wrapper class for dask that accesses chunks from a CASA file on request.
    It is assumed that this wrapper will be used to construct a dask array that
    has chunks aligned with the CASA file chunks.

    Having a single wrapper object such as this is far more efficient than
    having one array wrapper per chunk. This is because the dask graph gets
    very large if we end up with one dask array per chunk and slows everything
    down.
    """

    def __init__(self, filename, totalshape, chunkshape, chunkoversample=None,
                 dtype=None, itemsize=None, memmap=False, offset=0):
        self._filename = filename
        self._totalshape = totalshape[::-1]
        self._chunkshape = chunkshape[::-1]
        self._chunkoversample = chunkoversample[::-1]
        self.shape = totalshape[::-1]
        self.dtype = dtype
        self.ndim = len(self.shape)
        self._stacks = np.ceil(np.array(totalshape) / np.array(chunkshape)).astype(int)
        self._chunksize = prod(chunkshape)
        self._itemsize = itemsize
        self._memmap = memmap
        self._offset = offset

        if not memmap:
            if self._itemsize == 1:
                self._array = np.unpackbits(np.fromfile(filename, dtype='uint8'), bitorder='little')

            else:
                self._array = np.fromfile(filename, dtype=np.uint8)

        self._last_item = None
        self._last_result = None

    def __getitem__(self, item):

        # dask does not cache calls to __getitem__ so in some cases might call it twice with
        # the same item - rather than try and cache multiple possible items we implement a
        # simple caching strategy of at least ensuring that successive calls with the same
        # input are cached (https://github.com/dask/dask/issues/8420).
        # This is important for example for Table.__repr__ which accesses the cells
        # one by one.
        if item == self._last_item:
            return self._last_result

        # TODO: potentially normalize item, for now assume it is a list of slice objects

        indices = []
        for dim in range(self.ndim):
            if isinstance(item[dim], slice):
                indices.append(item[dim].start // self._chunkshape[dim])
            else:
                indices.append(item[dim] // self._chunkshape[dim])

        chunk_number = indices[0]
        for dim in range(1, self.ndim):
            chunk_number = chunk_number * self._stacks[::-1][dim] + indices[dim]

        offset = chunk_number * self._chunksize * self._itemsize + self._offset * self._itemsize

        item_in_chunk = []
        for dim in range(self.ndim):
            if isinstance(item[dim], slice):
                item_in_chunk.append(slice(item[dim].start - indices[dim] * self._chunkshape[dim],
                                           item[dim].stop - indices[dim] * self._chunkshape[dim],
                                           item[dim].step))
            else:
                item_in_chunk.append(item[dim] - indices[dim] * self._chunkshape[dim])
        item_in_chunk = tuple(item_in_chunk)

        if self._itemsize == 1:

            if self._memmap:
                n_native = prod(self._chunkoversample)
                rounded_up_chunksize = ceil(self._chunksize / n_native / 8) * n_native
                offset = offset // self._chunksize * rounded_up_chunksize
                array_uint8 = np.fromfile(self._filename, dtype=np.uint8,
                                          offset=offset, count=rounded_up_chunksize)
                array_bits = np.unpackbits(array_uint8, bitorder='little')
            else:
                array_bits = self._array[offset * 8: (offset + self._chunksize) * 8]

            chunk = combine_chunks(array_bits, 1,
                                   shape=self._chunkshape,
                                   oversample=self._chunkoversample)[:self._chunksize]

            result = chunk.reshape(self._chunkshape[::-1], order='F').T[item_in_chunk].astype(np.bool_)

        else:

            if self._memmap:
                data_bytes = np.fromfile(self._filename, dtype=np.uint8,
                                         offset=offset,
                                         count=self._chunksize * self._itemsize)
            else:
                data_bytes = self._array[chunk_number * self._chunksize * self._itemsize:
                                         (chunk_number + 1) * self._chunksize * self._itemsize]

            result = (combine_chunks(data_bytes,
                                     self._itemsize,
                                     shape=self._chunkshape,
                                     oversample=self._chunkoversample)
            .view(self.dtype)
            .reshape(self._chunkshape[::-1], order='F').T[item_in_chunk])

        self._last_item = item
        self._last_result = result

        #print(f"chunksize: {self.chunksize}")
        #print(f"chunksize: {self.chunkshape}")
        #print(f"chunkoversample: {self._chunkoversample}")
        #print(f"count: {self._chunksize * self._itemsize}")

        return result