# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class StandardStorageManager(KaitaiStruct):
    """User defined version of base numerical data types. This will allow for the
    compilation of languages like c++ and rust
    """

    class IsEndian(Enum):
        false = 0
        true = 1
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = StandardStorageManager.Header(self._io, self, self._root)
        self.header_remains = self._io.read_bytes((512 - self._io.pos()))
        self.bucket = StandardStorageManager.DataBucket(self.header.bucket_size, self.header.n_buckets, self._io, self, self._root)

    class StringBucketHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.free_bucket_list = self._io.read_u4le()
            self.n_bytes_used = self._io.read_u4le()
            self.n_deleted = self._io.read_u4le()
            self.next_bucket = self._io.read_u4le()


    class OneCol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rows_stored = self._io.read_u4le()
            self.rows_populated = []
            for i in range(1):
                self.rows_populated.append(self._io.read_u4le())

            self.some_int = []
            for i in range(1):
                self.some_int.append(self._io.read_u4le())



    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4le()
            self.value = (self._io.read_bytes(self.length)).decode(u"ASCII")


    class DataBucket(KaitaiStruct):
        def __init__(self, bucket_size, n_buckets, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.bucket_size = bucket_size
            self.n_buckets = n_buckets
            self._read()

        def _read(self):
            self.data = []
            for i in range(self.n_buckets):
                self.data.append(self._io.read_bytes(self.bucket_size))



    class Bucket(KaitaiStruct):
        def __init__(self, bucket_size, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.bucket_size = bucket_size
            self._read()

        def _read(self):
            self.offset = self._io.read_u4le()
            self.data = self._io.read_bytes((self.offset - 4))
            self.index = self._io.read_bytes((self.bucket_size - self.offset))

        @property
        def columns(self):
            if hasattr(self, '_m_columns'):
                return self._m_columns

            _pos = self._io.pos()
            self._io.seek(self.offset)
            self._m_columns = StandardStorageManager.OneCol(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_columns', None)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\xBE\xBE\xBE\xBE":
                raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/types/header/seq/0")
            self.size = self._io.read_u4le()
            self.name = StandardStorageManager.String(self._io, self, self._root)
            self.version = self._io.read_u4le()
            if self.version > 2:
                self.is_endian = KaitaiStream.resolve_enum(StandardStorageManager.IsEndian, self._io.read_u1())

            self.bucket_size = self._io.read_u4le()
            self.n_buckets = self._io.read_u4le()
            self.cache_size = self._io.read_u4le()
            self.n_free_buckets = self._io.read_u4le()
            self.first_free_bucket = self._io.read_s4le()
            self.n_index_buckets = self._io.read_u4le()
            self.first_index_bucket = self._io.read_s4le()
            if self.version > 1:
                self.offset_index = self._io.read_u4le()

            self.last_string_heap_bucket = self._io.read_s4le()
            self.index_length = self._io.read_u4le()
            self.n_indicies = self._io.read_u4le()



