# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))


class TableIncrementalStore(KaitaiStruct):
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
        self.header = TableIncrementalStore.Header(self._io, self, self._root)
        self.trash = self._io.read_bytes((512 - self._io.pos()))
        self.data = []
        for i in range(self.header.num_buckets):
            self.data.append(TableIncrementalStore.Bucket(self.header.bucket_size, self._io, self, self._root))

        self.index_set = TableIncrementalStore.IndexSet(self._io, self, self._root)

    class OneCol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rows_stored = self._io.read_u4le()
            self.rows_populated = []
            for i in range(self.rows_stored):
                self.rows_populated.append(self._io.read_u4le())

            self.some_int = []
            for i in range(50):
                self.some_int.append(self._io.read_u4le())

    class IndexMap(KaitaiStruct):
        def __init__(self, index_version, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.index_version = index_version
            self._read()

        def _read(self):
            self.number = self._io.read_u4le()
            self.type = TableIncrementalStore.TypeName(u"Block", self._io, self, self._root)
            self.version = self._io.read_u4le()
            self.size = self._io.read_u4le()
            self.elements = []
            for i in range(self.size):
                _on = self.index_version
                if _on == 1:
                    self.elements.append(self._io.read_u4le())
                else:
                    self.elements.append(self._io.read_u8le())

    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_u4le()
            self.value = (self._io.read_bytes(self.len)).decode(u"ASCII")

    class DataBlock(KaitaiStruct):
        def __init__(self, block_size, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.block_size = block_size
            self._read()

        def _read(self):
            self.block = self._io.read_bytes(self.block_size)

    class Bucket(KaitaiStruct):
        def __init__(self, bucket_size, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.bucket_size = bucket_size
            self._read()

        def _read(self):
            self.index_offset = self._io.read_u4le()
            self.data = self._io.read_bytes((self.index_offset - 4))
            self.index = self._io.read_bytes((self.bucket_size - self.index_offset))

        @property
        def first_col(self):
            if hasattr(self, '_m_first_col'):
                return self._m_first_col

            _pos = self._io.pos()
            self._io.seek(28977)
            self._m_first_col = TableIncrementalStore.OneCol(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_first_col', None)

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\xBE\xBE\xBE\xBE":
                raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io,
                                                           u"/types/header/seq/0")
            self.number01 = self._io.read_u4le()
            self.type = TableIncrementalStore.String(self._io, self, self._root)
            self.version = self._io.read_u4le()
            if self.version == 5:
                self.isbigendian = self._io.read_u1()

            self.bucket_size = self._io.read_u4le()
            self.num_buckets = self._io.read_u4le()
            self.persistent_cache_size = self._io.read_u4le()
            self.unique_column_number = self._io.read_u4le()
            self.number_free_buckets = self._io.read_u4le()
            self.first_free_bucket = self._io.read_s4le()

    class OnexCol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_rows = self._io.read_u4le()
            self.row_numbers_of_values_stored_in_row = self._io.read_u4le()
            self.offset_in_data_part_of_values_stored = []
            for i in range(self.num_rows):
                self.offset_in_data_part_of_values_stored.append(self._io.read_u4le())

    class TypeName(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            self.size = self._io.read_u4le()
            self.name = (self._io.read_bytes(len(self.value))).decode(u"ASCII")
            if not self.name == self.value:
                raise kaitaistruct.ValidationNotEqualError(self.value, self.name, self._io, u"/types/type_name/seq/1")

    class IndexSet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\xBE\xBE\xBE\xBE":
                raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io,
                                                           u"/types/index_set/seq/0")
            self.size = self._io.read_u4le()
            self.type = TableIncrementalStore.TypeName(u"ISMIndex", self._io, self, self._root)
            self.version = self._io.read_u4le()
            self.blocks_in_use = self._io.read_u4le()
            self.index_2_row = TableIncrementalStore.IndexMap(self.version, self._io, self, self._root)
            self.index_2_bucket = TableIncrementalStore.IndexMap(self.version, self._io, self, self._root)
