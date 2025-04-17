import pathlib

import numpy as np
import toolviper.utils.logger as logger

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


    def get_column(self, name: str, is_regular_table=True)->None:
        filename = str(pathlib.Path(self.basename).joinpath("table.dat").absolute())
        sequence_number = None

        with  filestream.OpenKaitaiStream(filename) as _io:
            common_stream = Common(_io)

            if is_regular_table:
                _io.seek(common_stream.stream_position)
                self.regular_table_desc = RegularTableDescription(_io=_io)

            for i, entry in enumerate(self.regular_table_desc.desc.columns.column_info):
                if entry.column_name.value == name:
                    logger.info(f"Column name: {name}: sequence number: {entry.manager_number}")
                    sequence_number = entry.manager_number
                    manager_type = self.regular_table_desc.desc.columns.column_desc[i].manager_type.value


        if sequence_number is None:
            logger.error(f"Column name: {name}: not found in regular table")
            return None

        filename = str(pathlib.Path(self.basename).joinpath(f"table.f{sequence_number}").absolute())
        with  filestream.OpenKaitaiStream(filename) as _io:
            manager = filestream.load_manager(name=manager_type)
            logger.info(f"Manager name: {manager}")

        return None




