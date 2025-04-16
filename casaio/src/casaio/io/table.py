import pathlib

import numpy as np
import toolviper.utils.logger as logger

from kaitaistruct import KaitaiStream

from casaio.tablestream.python.metadata import Metadata
from casaio.tablestream.python.common import Common
from casaio.tablestream.python.regular_table_description import RegularTableDescription
from casaio.tablestream.python.tiled_shape_storage_manager import TiledShapeStorageManager
from casaio.tablestream.python.tsm_binary_data import TsmBinaryData


class Table:
    def __init__(self):
        self.basename = None

    def set_file(self, basename: str)->None:

        # Make sure the file exists
        if pathlib.Path(basename).exists():
            if self.basename is not None:
                logger.warning(f"File name changed: {self.basename} --> {basename}")

            self.basename = basename

        else:
            logger.error(f"File does not exist: {basename}")


    def get_column(self, name: str, is_regular_table=True)->None:
        pass