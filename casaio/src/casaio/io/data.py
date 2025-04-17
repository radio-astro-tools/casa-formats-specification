import pathlib

import numpy as np

from kaitaistruct import KaitaiStream

from casaio.tablestream.python.metadata import Metadata
from casaio.tablestream.python.common import Common
from casaio.tablestream.python.regular_table_description import RegularTableDescription
from casaio.tablestream.python.tiled_shape_storage_manager import TiledShapeStorageManager
from casaio.tablestream.python.tsm_binary_data import TsmBinaryData

def get_data(filename):
    values = []
    indices = []
    elements = []

    with KaitaiStream(open(filename, "rb")) as _io:
        column_desc = get_column_description("DATA")
        #table = TableIncrementalStore(_io=_io, stream=column_desc)

        return column_desc

def get_column_description(column):
    table_desc = get_table_description(is_regular_table=True)

    for i, desc in enumerate(table_desc.desc.columns.column_desc):
        if desc.name.value == column:
            return desc

def get_table_description(is_regular_table=False):
    with KaitaiStream(
            open(
                "/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.ms"
                "/table.dat", "rb")) as _io:
        common_stream = Common(_io)

        if is_regular_table:
            _io.seek(common_stream.stream_position)
            regular_table_desc = RegularTableDescription(_io=_io)

        return regular_table_desc
def get_column(name="DATA", is_regular_table=True):
    with KaitaiStream(
            open(
                "/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.ms"
                "/table.dat", "rb")) as _io:
        common_stream = Common(_io)

        if is_regular_table:
            _io.seek(common_stream.stream_position)
            regular_table_desc = RegularTableDescription(_io=_io)

        for i, entry in enumerate(regular_table_desc.desc.columns.column_info):
            if entry.column_name.value == name:
                print(f"name: {name}, sequence: {entry.manager_number}")

                sequence_number = entry.manager_number
    file = f"/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.ms/table.f{sequence_number}"
    with KaitaiStream(
            open(f"/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.ms/table.f{sequence_number}", "rb")) as _io:

        print(f"file: {file}")
        tiled_manager = TiledShapeStorageManager(_io)

        print(f"size: {tiled_manager.cube_index.size}")
        print(f"n_rows: {tiled_manager.cube_index.n_rows}")

        for element in tiled_manager.cube_index.elements:
            print(f"cube: {element}")

        print(f"default: {tiled_manager.default_tile_shape.elements}")
        print(f"tsm indicies: {np.unique(tiled_manager.cube_index.elements)}")

        for index in tiled_manager.cube_index.elements:
            data = read_tsm(
                filename=file,
                index=index,
                sequence_number=entry.manager_number,
                manager=tiled_manager,
                total_shape=tiled_manager.itsm_dimension[index].cube_shapes.elements,
                chunk_shape=tiled_manager.itsm_dimension[index].tile_shapes.elements
            )


        return data

def read_tsm(filename, index, sequence_number, manager, total_shape, chunk_shape):
    # The following is mostly out of the astropy code and I don't completely follow it yet
    # but .... for speed of development ....

    total_shape = np.array(total_shape)
    chunk_shape = np.array(chunk_shape)
    chunk_shape = list(map(int, chunk_shape))

    chunk_size = np.prod(chunk_shape)
    memory_map = True

    stacks = np.ceil(total_shape / chunk_shape).astype(int)
    target_chunk_size = 10000000       # not sure where this comes from in the astropy code
    if chunk_size < target_chunk_size:
        # Find optimal chunk - since we want to be efficient we want the new
        # chunks to be contiguous on disk so we first try and increase the
        # chunk size in x, then y, etc.

        chunk_oversample = previous_chunk_oversample = [1 for i in range(len(chunk_shape))]

        finished = False
        for dim in range(len(chunk_shape)):

            factors = [f for f in range(stacks[dim] + 1) if stacks[dim] % f == 0]

            for factor in factors:
                chunk_oversample[dim] = factor
                if np.prod(chunk_oversample) * chunk_size > target_chunk_size:
                    chunk_oversample = previous_chunk_oversample
                    finished = True
                    break
                previous_chunk_oversample = chunk_oversample.copy()
            if finished:
                break

    else:
        chunk_oversample = (1,) * len(chunk_shape)

    #chunk_shape = [chunk * oversample for (chunk, oversample) in zip(chunk_shape, chunk_oversample)]
    #print(f"chunk shape: {chunk_shape}")

    data_file = filename + f"_TSM{index}"
    #print(f"data_file: {data_file}")

    #with KaitaiStream(open(data_file, "rb")) as _io:
    #    tsm_data = TsmBinaryData(_io)

    tsm_data = np.fromfile(data_file, dtype=np.complex64)

    data_length = np.prod(total_shape)

    return tsm_data[:data_length]

    #new_tsm_data = array.combine_chunks(
    #    tsm_data,
    #    np.dtype("<c8").itemsize,
    #    chunk_shape,
    #    chunk_oversample
    #)

    #return new_tsm_data

    #wrapper = array.ArrayWrapper(
    #    filename=data_file,
    #    totalshape=total_shape,
    #    chunkshape=chunk_shape,
    #    chunkoversample=chunk_oversample,
    #    dtype="<c8",
    #    itemsize=np.dtype("<c8").itemsize,
    #    memmap=memory_map,
    #    offset=0
    #)

    #return wrapper
    #import uuid
    #from dask import array as darray

    #da = darray.from_array(wrapper, name="CASA data " + str(uuid.uuid4()), chunks=chunk_shape[::-1], meta=np.array([[[]]], dtype="<c8"))
    #final_slice = tuple([slice(dimension) for dimension in total_shape[::-1]])
    #return da[final_slice]

