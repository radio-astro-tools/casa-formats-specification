import pathlib
import importlib

import toolviper.utils.logger as logger

from typing import Union

from kaitaistruct import KaitaiStream

from casaio.tablestream.python.common import Common
from casaio.tablestream.python.tiled_shape_storage_manager import TiledShapeStorageManager


class OpenKaitaiStream:
    def __init__(self, filename: str, mode: str="rb"):
        self.filename = filename
        self.file_handle = None
        self.mode = mode
        self.file = None

    def __enter__(self):
        path = pathlib.Path(self.filename)

        if path.exists():
            self.file_handle = open(path, self.mode)

            return KaitaiStream(self.file_handle)

        else:
            self.filename = None
            return None

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if not self.file_handle is None:
            self.file_handle.close()

def load_manager(name: str)->Union[object, None]:
    manager_list = {
        "IncrementalStMan": "incremental_storage_manager",
        "StandardStMan": "standard_storage_manager",
        "TiledStMan": "tiled_storage_manager",
        "TiledShapeStMan": "tiled_shape_storage_manager"
    }

    if not name in manager_list.keys():
        logger.error(f"Module {name} not found")
        return None

    package = ".".join(["python", manager_list[name]])
    manager = importlib.import_module(name="casaio", package=package)

    return manager