# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class TsmBinaryData(KaitaiStruct):
    """The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
    oriented storage system for radio astronoy data. Many systems use it to store, manipulate and process
    the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
    from the telescopes and the images that are produced as a final product. This file parses only the
    table description stored in the table.dat file within the table directory.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.data = []
        i = 0
        while not self._io.is_eof():
            self.data.append(TsmBinaryData.Complex8(self._io, self, self._root))
            i += 1


    class Complex8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.real = self._io.read_f4be()
            self.imaginary = self._io.read_f4be()



