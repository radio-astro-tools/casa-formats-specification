import pathlib
import importlib

import toolviper.utils.logger as logger

from typing import Union, IO

from kaitaistruct import KaitaiStream

from casaio.tablestream.python.tiled_shape_storage_manager import TiledShapeStorageManager
from casaio.io import constants

class OpenKaitaiStream:
    def __init__(self, filename: str, mode: str="rb"):
        self.filename: str = filename
        self.file_handle: Union[None, IO] = None
        self.mode: str = mode
        self.file: Union[str, None] = None

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

def load_manager(name: str)->Union[type[TiledShapeStorageManager], None]:
    if not name in constants.manager_list.keys():
        logger.error(f"Module {name} not found")
        return None

    module = ".".join(["casaio.io.managers", constants.manager_list[name]["module"]])
    manager = importlib.import_module(name=module)

    return getattr(manager, constants.manager_list[name]["package"])