# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO

from .dtype import Dtype

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class TiledShapeStorageManager(KaitaiStruct):
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
        self.header = TiledShapeStorageManager.Header(self._io, self, self._root)
        self.number = self._io.read_u4be()
        self.type = TiledShapeStorageManager.String(self._io, self, self._root)
        self.version = self._io.read_u4be()
        if self.version == 5:
            self.isbigendian = self._io.read_u1()

        self.idk = self._io.read_u1()
        self.sequence_numer = self._io.read_u4be()
        self.n_rows = self._io.read_u4be()
        self.n_columns = self._io.read_u4be()
        self.dtype = self._io.read_u4be()
        self.column_name = TiledShapeStorageManager.String(self._io, self, self._root)
        self.max_cache = self._io.read_u4be()
        self.n_dimensions = self._io.read_u4be()
        self.n_record_files = self._io.read_u4be()
        self.itsm_cube_size = []
        for i in range(self.n_record_files):
            self.itsm_cube_size.append(TiledShapeStorageManager.ItsmsCubeSize(self._io, self, self._root))

        self.unknown = self._io.read_u4be()
        self.itsm_dimension = []
        for i in range(self.n_record_files):
            self.itsm_dimension.append(TiledShapeStorageManager.ItsmsDimension(self._io, self, self._root))

        self.default_tile_shape = TiledShapeStorageManager.Iposition(self._io, self, self._root)
        self.number_used_row_map = self._io.read_u4be()
        self.last_row = TiledShapeStorageManager.Block(self._io, self, self._root)
        self.cube_index = TiledShapeStorageManager.Block(self._io, self, self._root)
        self.last_row_subcube = TiledShapeStorageManager.Block(self._io, self, self._root)

    class Iposition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nbytes = self._io.read_u4be()
            self.type = TiledShapeStorageManager.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.n_elements = self._io.read_u4be()
            self.elements = []
            for i in range(self.n_elements):
                self.elements.append(self._io.read_u4be())



    class SubRecordArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = TiledShapeStorageManager.Iposition(self._io, self, self._root)
            self.unknown = self._io.read_bytes(4)


    class ItsmsDimension(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown = self._io.read_u4be()
            self.record = TiledShapeStorageManager.Record(self._io, self, self._root)
            self.flag = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.n_dimensions = self._io.read_u4be()
            self.cube_shapes = TiledShapeStorageManager.Iposition(self._io, self, self._root)
            self.tile_shapes = TiledShapeStorageManager.Iposition(self._io, self, self._root)
            self.more_unknown = self._io.read_u8be()


    class RecordDescription(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = TiledShapeStorageManager.ReadType(self._io, self, self._root)
            self.n_records = self._io.read_u4be()
            self.sub_record_description = []
            for i in range(self.n_records):
                self.sub_record_description.append(TiledShapeStorageManager.SubRecordDescription(self._io, self, self._root))

            self.unknown = self._io.read_u4be()


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4be()
            self.value = (self._io.read_bytes(self.length)).decode(u"ASCII")


    class ReadType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nbytes = self._io.read_u4be()
            self.type = TiledShapeStorageManager.String(self._io, self, self._root)
            self.version = self._io.read_u4be()


    class Complex8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.real = self._io.read_f4be()
            self.imaginary = self._io.read_f4be()


    class SubRecordTable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_bytes(8)


    class Array(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.cxx_type = TiledShapeStorageManager.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.n_shape = self._io.read_u4be()
            self.shape = []
            for i in range(self.n_shape):
                self.shape.append(self._io.read_u4be())

            self.n_elements = self._io.read_u4be()
            self.elements = []
            for i in range(self.n_elements):
                _on = self.type
                if _on == 14:
                    self.elements.append(Dtype.Int1(self._io, self, self._root))
                elif _on == 17:
                    self.elements.append(Dtype.Uint2(self._io, self, self._root))
                elif _on == 24:
                    self.elements.append(TiledShapeStorageManager.String(self._io, self, self._root))
                elif _on == 20:
                    self.elements.append(Dtype.Float4(self._io, self, self._root))
                elif _on == 13:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 19:
                    self.elements.append(Dtype.Uint4(self._io, self, self._root))
                elif _on == 23:
                    self.elements.append(TiledShapeStorageManager.Complex16(self._io, self, self._root))
                elif _on == 15:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 21:
                    self.elements.append(Dtype.Float8(self._io, self, self._root))
                elif _on == 16:
                    self.elements.append(Dtype.Int2(self._io, self, self._root))
                elif _on == 18:
                    self.elements.append(Dtype.Int4(self._io, self, self._root))
                elif _on == 22:
                    self.elements.append(TiledShapeStorageManager.Complex8(self._io, self, self._root))
                elif _on == 30:
                    self.elements.append(Dtype.Int8(self._io, self, self._root))



    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.n_rows = self._io.read_u4be()
            self.name = TiledShapeStorageManager.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.size = self._io.read_u4be()
            self.elements = []
            for i in range(self.size):
                self.elements.append(self._io.read_u4be())



    class ItsmsCubeSize(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flag = self._io.read_u1()
            if self.flag == 1:
                self.mode = self._io.read_u4be()

            if self.flag == 1:
                self.unknown = self._io.read_u4be()

            if self.flag == 1:
                _on = self.mode
                if _on == 1:
                    self.total_cube_size = self._io.read_u4be()
                elif _on == 2:
                    self.total_cube_size = self._io.read_u8be()



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
            self.number = self._io.read_u4be()
            self.type = TiledShapeStorageManager.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            if self.version == 5:
                self.isbigendian = self._io.read_u1()



    class TypeName(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.name = (self._io.read_bytes(len(self.value))).decode(u"ASCII")
            if not self.name == self.value:
                raise kaitaistruct.ValidationNotEqualError(self.value, self.name, self._io, u"/types/type_name/seq/1")


    class SubRecordDescription(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = TiledShapeStorageManager.String(self._io, self, self._root)
            self.type = self._io.read_u4be()
            _on = self.type
            if _on == 10:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 0:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 6:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 7:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 11:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 12:
                self.value = TiledShapeStorageManager.SubRecordTable(self._io, self, self._root)
            elif _on == 5:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 8:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 9:
                self.value = TiledShapeStorageManager.String(self._io, self, self._root)
            elif _on == 25:
                self.value = TiledShapeStorageManager.SubRecordDescription(self._io, self, self._root)
            else:
                self.value = TiledShapeStorageManager.SubRecordArray(self._io, self, self._root)


    class Complex16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.real = self._io.read_f8be()
            self.imaginary = self._io.read_f8be()


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = TiledShapeStorageManager.ReadType(self._io, self, self._root)
            self.record_description = TiledShapeStorageManager.RecordDescription(self._io, self, self._root)



