import cython
import numpy as np

from casaio.io import constants
from casaio.tablestream.python import tiled_shape_storage_manager
from casaio.tablestream.python import tiled_column_storage_manager
from casaio.tablestream.python.regular_table_description import RegularTableDescription

from typing import Union, Dict, IO

@cython.cclass
class TiledShapeStorageManager:
    __slots__ = "filename", "manager", "table_description"

    def __init__(self, filename: Union[None, str] = None, _io=IO):
        self.filename = filename
        self.manager = tiled_shape_storage_manager.TiledShapeStorageManager(_io)
        self.table_description = None

    @cython.ccall
    def get_column(self, data_type: type, reshape: bool=False) -> Dict:
        # Working with the managers from here on out, in the case of a get_column() function,
        # this should probably be a special class that handles the differences between different
        #  managers, but for now I'm going to use direct access.
        data = {}

        for index in self.manager.cube_index.elements:
            tsm_filename = "_".join([self.filename, f"TSM{index}"])

            data[index] = self.read_tsm(
                filename=tsm_filename,
                data_type=data_type,
                total_shape=self.manager.itsm_dimension[index].cube_shapes.elements,
                chunk_shape=self.manager.itsm_dimension[index].tile_shapes.elements,
                reshape=reshape
            )

        return data


    @cython.ccall
    @staticmethod
    def read_tsm(filename, data_type, total_shape, chunk_shape, reshape: bool=False):

        total_shape = np.array(total_shape)

        chunk_shape = np.array(chunk_shape)

        chunk_shape = list(map(int, chunk_shape))

        # This line will work for the file I have, but the dtype qualifier needs to be changed to
        # reflect the endianess in a later version.
        tsm_data = np.fromfile(filename, dtype=constants.casacore_data_types[data_type])

        data_length = np.prod(total_shape)

        if reshape:
            return tsm_data[:data_length].reshape(total_shape)

        return tsm_data


# Placeholder for Column version tiled class
@cython.cclass
class TiledColumnStorageManager:
    __slots__ = "filename", "manager", "table_description"

    def __init__(self, filename: Union[None, str] = None, _io=IO):
        self.filename = filename
        self.manager = tiled_column_storage_manager.TiledColumnStorageManager(_io)
        self.table_description = None

    @cython.ccall
    def get_column(self, data_type: type, reshape: bool=False) -> Dict:
        # Working with the managers from here on out, in the case of a get_column() function,
        # this should probably be a special class that handles the differences between different
        #  managers, but for now I'm going to use direct access.
        data = {}

        # This doesn't seem to exist in the column storage manager. Need to
        # look into this more....
        #
        # for index in self.manager.cube_index.elements:
        index = 0
        tsm_filename = "_".join([self.filename, f"TSM0"])

        data[index] = self.read_tsm(
                filename=tsm_filename,
                data_type=data_type,
                total_shape=self.manager.itsm_dimension[index].cube_shapes.elements,
                chunk_shape=self.manager.itsm_dimension[index].tile_shapes.elements,
                reshape=reshape
        )

        return data


    @cython.ccall
    @staticmethod
    def read_tsm(filename, data_type, total_shape, chunk_shape, reshape: bool=False):

        total_shape = np.array(total_shape)

        chunk_shape = np.array(chunk_shape)

        chunk_shape = list(map(int, chunk_shape))

        # This line will work for the file I have, but the dtype qualifier needs to be changed to
        # reflect the endianess in a later version.
        tsm_data = np.fromfile(filename, dtype=constants.casacore_data_types[data_type])

        data_length = np.prod(total_shape)

        if reshape:
            return tsm_data[:data_length].reshape(total_shape)

        return tsm_data