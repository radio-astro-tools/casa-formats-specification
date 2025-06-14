import pathlib

import toolviper.utils.logger as logger

from typing import Union, Dict, Any

from casaio.tablestream.python.common import Common
from casaio.tablestream.python.regular_table_description import RegularTableDescription

from casaio.io import filestream

class Table:
    def __init__(self, basename=None):
        self.basename = basename
        self.regular_table_desc = None
        self.common_stream = None


    def set_file(self, basename: str)->None:

        # Make sure the file exists
        if pathlib.Path(basename).exists():
            if self.basename is not None:
                pass
                logger.warning(f"File name changed: {self.basename} --> {basename}")

            self.basename = basename

        else:
            logger.error(f"File does not exist: {basename}")

            pass

    def get_keywords(self, is_regular_table=True) -> None:
        from tabulate import tabulate
        from casaio.io import constants

        filename = str(pathlib.Path(self.basename).joinpath("table.dat").absolute())
        sequence_number = None

        with  filestream.OpenKaitaiStream(filename) as _io:
            if self.common_stream is None:
                self.common_stream = Common(_io)

            if is_regular_table:
                _io.seek(self.common_stream.stream_position)

                if self.regular_table_desc is None:
                    self.regular_table_desc = RegularTableDescription(_io=_io)

            entries = []

            for i, entry in enumerate(self.regular_table_desc.desc.table_keywords.desc.fields):
                entries.append([entry.name.value, constants.casacore_data_types_list[entry.type], entry.comment.value])

            table = tabulate(entries, headers=["name", "dtype", "comment"], tablefmt="fancy_outline")
            print(table)
            return None

    def get_column(self, name: str, is_regular_table=True, reshape: bool=False)->Union[None, Dict]:
        filename = str(pathlib.Path(self.basename).joinpath("table.dat").absolute())
        sequence_number = None

        with  filestream.OpenKaitaiStream(filename) as _io:
            if self.common_stream is None:
                self.common_stream = Common(_io)

            if is_regular_table:
                _io.seek(self.common_stream.stream_position)

                if self.regular_table_desc is None:
                    self.regular_table_desc = RegularTableDescription(_io=_io)

            for i, entry in enumerate(self.regular_table_desc.desc.columns.column_info):

                if entry.column_name.value == name:
                    logger.debug(f"Column name: {name}: sequence number: {entry.manager_number}")
                    sequence_number = entry.manager_number
                    manager_type = self.regular_table_desc.desc.columns.column_desc[i].manager_type.value
                    data_type = self.regular_table_desc.desc.columns.column_desc[i].data_type

        if sequence_number is None:
            logger.error(f"Column name: {name}: not found in regular table")
            return None

        # From here should probably be part of a manager class for a tiled standard manager
        filename = str(pathlib.Path(self.basename).joinpath(f"table.f{sequence_number}").absolute())
        with  filestream.OpenKaitaiStream(filename) as _io:
            manager_package = filestream.load_manager(name=manager_type)
            manager = manager_package(_io=_io, filename=filename)

        return manager.get_column(data_type=data_type, reshape=reshape)

    def get_column_description(self, is_regular_table=True, view=False)->Union[None, Dict]:
        from tabulate import tabulate

        filename = str(pathlib.Path(self.basename).joinpath("table.dat").absolute())
        column_description = {}

        with  filestream.OpenKaitaiStream(filename) as _io:
            if self.common_stream is None:
                self.common_stream = Common(_io)

            if is_regular_table:
                _io.seek(self.common_stream.stream_position)

                if self.regular_table_desc is None:
                    self.regular_table_desc = RegularTableDescription(_io=_io)

            for i, entry in enumerate(self.regular_table_desc.desc.columns.column_info):

                sequence_number = entry.manager_number
                manager_type = self.regular_table_desc.desc.columns.column_desc[i].manager_type.value
                data_type = self.regular_table_desc.desc.columns.column_desc[i].data_type

                column_description[entry.column_name.value] = {
                    "manager_type": manager_type,
                    "sequence_number": sequence_number,
                    "data_type": data_type,
                }

        if view:
            entries = []
            for key, value in column_description.items():
                entries.append(
                    [
                        key,
                        *value.values(),
                    ]
                )

            table = tabulate(entries, headers=["name", "manager", "sequence_number", "data_type"], tablefmt="fancy_outline")
            print(table)
            return None

        return column_description


