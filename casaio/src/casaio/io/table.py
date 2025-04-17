import pathlib

import numpy as np
import toolviper.utils.logger as logger

from typing import Union, Dict

from casaio.tablestream.python.common import Common
from casaio.tablestream.python.regular_table_description import RegularTableDescription

from casaio.io import filestream

class Table:
    def __init__(self):
        self.basename = None
        self.regular_table_desc = None


    def set_file(self, basename: str)->None:

        # Make sure the file exists
        if pathlib.Path(basename).exists():
            if self.basename is not None:
                logger.warning(f"File name changed: {self.basename} --> {basename}")

            self.basename = basename

        else:
            logger.error(f"File does not exist: {basename}")


    def get_column(self, name: str, is_regular_table=True)->Union[None, Dict]:
        filename = str(pathlib.Path(self.basename).joinpath("table.dat").absolute())
        sequence_number = None

        with  filestream.OpenKaitaiStream(filename) as _io:
            common_stream = Common(_io)

            if is_regular_table:
                _io.seek(common_stream.stream_position)
                self.regular_table_desc = RegularTableDescription(_io=_io)

            for i, entry in enumerate(self.regular_table_desc.desc.columns.column_info):
                if entry.column_name.value == name:
                    logger.debug(f"Column name: {name}: sequence number: {entry.manager_number}")
                    sequence_number = entry.manager_number
                    manager_type = self.regular_table_desc.desc.columns.column_desc[i].manager_type.value


        if sequence_number is None:
            logger.error(f"Column name: {name}: not found in regular table")
            return None

        filename = str(pathlib.Path(self.basename).joinpath(f"table.f{sequence_number}").absolute())
        with  filestream.OpenKaitaiStream(filename) as _io:
            manager_package = filestream.load_manager(name=manager_type)
            manager = manager_package(_io)

            # Working with the managers from here on out, in the case of a get_column() function,
            # this should probably be a special class that handles the differences between different
            #  managers, but for now I'm going to use direct access.
            data = {}

            for index in manager.cube_index.elements:
                tsm_filename = "_".join([filename, f"TSM{index}"])

                data[index] = self.read_tsm(
                    filename=tsm_filename,
                    total_shape=manager.itsm_dimension[index].cube_shapes.elements,
                    chunk_shape=manager.itsm_dimension[index].tile_shapes.elements
                )

        return data

    @staticmethod
    def read_tsm(filename, total_shape, chunk_shape):
        # This needs to be moved to the manager class provisionally

        total_shape = np.array(total_shape)
        chunk_shape = np.array(chunk_shape)
        chunk_shape = list(map(int, chunk_shape))

        tsm_data = np.fromfile(filename, dtype=np.complex64)

        data_length = np.prod(total_shape)

        return tsm_data[:data_length].reshape(total_shape)




