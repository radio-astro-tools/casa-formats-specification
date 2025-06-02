import cython
import numpy as np

from casaio.io import constants
from casaio.tablestream.python import standard_storage_manager

from typing import Union, Dict, IO

@cython.cclass
class StandardStorageManager:
    __slots__ = "filename", "manager"

    def __init__(self, filename: Union[None, str] = None, _io=IO):
        self.filename = filename
        self.manager = standard_storage_manager.StandardStorageManager(_io)

    @cython.ccall
    def get_column(self, data_type: type, reshape: bool=False) -> np.ndarray:
        # The data is read as a list of byte strings by kaitai and soe we need to efficiently decode it
        data = np.array([np.frombuffer(d, dtype=np.int16) for d in self.manager.bucket.data])

        return data
