# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Common(KaitaiStruct):
    """The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
    oriented storage system for radio astronomy data. Many systems use it to store, manipulate and process
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
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\xBE\xBE\xBE\xBE":
            raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/seq/0")
        self.size = self._io.read_u4be()
        self.type = Common.String(self._io, self, self._root)
        self.version = self._io.read_u4be()
        _on = self.version
        if _on == 1:
            self.nrows = self._io.read_u4be()
        elif _on == 2:
            self.nrows = self._io.read_u4be()
        elif _on == 3:
            self.nrows = self._io.read_u8be()
        self.little_endian = self._io.read_u4be()
        self.name = Common.String(self._io, self, self._root)
        self.table_desc_info = Common.DescInfo(self._io, self, self._root)

    class TableDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = Common.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.name = Common.String(self._io, self, self._root)


    class DescInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = Common.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.name = Common.String(self._io, self, self._root)


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4be()
            self.value = (self._io.read_bytes(self.length)).decode(u"ASCII")


    class Complex8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.real = self._io.read_f4be()
            self.imaginary = self._io.read_f4be()


    class Complex16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.real = self._io.read_f8be()
            self.imaginary = self._io.read_f8be()


    @property
    def stream_position(self):
        if hasattr(self, '_m_stream_position'):
            return self._m_stream_position

        self._m_stream_position = self._io.pos()
        return getattr(self, '_m_stream_position', None)


