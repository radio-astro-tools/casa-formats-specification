# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO

from .dtype import Dtype

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Metadata(KaitaiStruct):
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
        _on = self.version_bytes
        if _on == 33554432:
            self._is_le = True
        elif _on == 1:
            self._is_le = False
        elif _on == 16777216:
            self._is_le = True
        elif _on == 50331648:
            self._is_le = True
        elif _on == 3:
            self._is_le = False
        elif _on == 2:
            self._is_le = False
        if not hasattr(self, '_is_le'):
            raise kaitaistruct.UndecidedEndiannessError("/")
        elif self._is_le == True:
            self._read_le()
        elif self._is_le == False:
            self._read_be()

    def _read_le(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\xBE\xBE\xBE\xBE":
            raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/seq/0")
        self.size = self._io.read_u4le()
        self.type = Metadata.String(self._io, self, self._root, self._is_le)
        self.version = self._io.read_u4le()
        _on = self.version
        if _on == 1:
            self.nrows = self._io.read_u4le()
        elif _on == 2:
            self.nrows = self._io.read_u4le()
        elif _on == 3:
            self.nrows = self._io.read_u8le()
        self.big_endian = self._io.read_u4le()
        self.name = Metadata.String(self._io, self, self._root, self._is_le)
        self.desc = Metadata.TableDesc(self._io, self, self._root, self._is_le)

    def _read_be(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\xBE\xBE\xBE\xBE":
            raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/seq/0")
        self.size = self._io.read_u4be()
        self.type = Metadata.String(self._io, self, self._root, self._is_le)
        self.version = self._io.read_u4be()
        _on = self.version
        if _on == 1:
            self.nrows = self._io.read_u4be()
        elif _on == 2:
            self.nrows = self._io.read_u4be()
        elif _on == 3:
            self.nrows = self._io.read_u8be()
        self.big_endian = self._io.read_u4be()
        self.name = Metadata.String(self._io, self, self._root, self._is_le)
        self.desc = Metadata.TableDesc(self._io, self, self._root, self._is_le)

    class ArrayColumnStorageDetails(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/array_column_storage_details")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.shape_column_definition = self._io.read_u1()
            if self.shape_column_definition > 0:
                self.filler = self._io.read_u4le()

            if self.shape_column_definition > 0:
                self.shape = Metadata.Iposition(self._io, self, self._root, self._is_le)


        def _read_be(self):
            self.shape_column_definition = self._io.read_u1()
            if self.shape_column_definition > 0:
                self.filler = self._io.read_u4be()

            if self.shape_column_definition > 0:
                self.shape = Metadata.Iposition(self._io, self, self._root, self._is_le)



    class DataValue(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.type = type
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/data_value")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            _on = self.type
            if _on == 10:
                self.value = Metadata.Complex16(self._io, self, self._root, self._is_le)
            elif _on == 0:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 4:
                self.value = Dtype.Uint2(self._io, self, self._root)
            elif _on == 6:
                self.value = Dtype.Uint4(self._io, self, self._root)
            elif _on == 7:
                self.value = Dtype.Float4(self._io, self, self._root)
            elif _on == 1:
                self.value = Dtype.Int1(self._io, self, self._root)
            elif _on == 11:
                self.value = Metadata.String(self._io, self, self._root, self._is_le)
            elif _on == 12:
                self.value = Metadata.String(self._io, self, self._root, self._is_le)
            elif _on == 3:
                self.value = Dtype.Int2(self._io, self, self._root)
            elif _on == 5:
                self.value = Dtype.Int4(self._io, self, self._root)
            elif _on == 8:
                self.value = Dtype.Float8(self._io, self, self._root)
            elif _on == 9:
                self.value = Metadata.Complex8(self._io, self, self._root, self._is_le)
            elif _on == 2:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 29:
                self.value = Dtype.Int8(self._io, self, self._root)
            elif _on == 25:
                self.value = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            else:
                self.value = Metadata.Array(self.type, self._io, self, self._root, self._is_le)

        def _read_be(self):
            _on = self.type
            if _on == 10:
                self.value = Metadata.Complex16(self._io, self, self._root, self._is_le)
            elif _on == 0:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 4:
                self.value = Dtype.Uint2(self._io, self, self._root)
            elif _on == 6:
                self.value = Dtype.Uint4(self._io, self, self._root)
            elif _on == 7:
                self.value = Dtype.Float4(self._io, self, self._root)
            elif _on == 1:
                self.value = Dtype.Int1(self._io, self, self._root)
            elif _on == 11:
                self.value = Metadata.String(self._io, self, self._root, self._is_le)
            elif _on == 12:
                self.value = Metadata.String(self._io, self, self._root, self._is_le)
            elif _on == 3:
                self.value = Dtype.Int2(self._io, self, self._root)
            elif _on == 5:
                self.value = Dtype.Int4(self._io, self, self._root)
            elif _on == 8:
                self.value = Dtype.Float8(self._io, self, self._root)
            elif _on == 9:
                self.value = Metadata.Complex8(self._io, self, self._root, self._is_le)
            elif _on == 2:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 29:
                self.value = Dtype.Int8(self._io, self, self._root)
            elif _on == 25:
                self.value = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            else:
                self.value = Metadata.Array(self.type, self._io, self, self._root, self._is_le)


    class ReferenceTableDesc(KaitaiStruct):
        def __init__(self, version, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.version = version
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/reference_table_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.column_map_size = self._io.read_u4le()
            self.column_map_type = Metadata.TypeName(u"SimpleOrderedMap", self._io, self, self._root, self._is_le)
            self.column_map_version = self._io.read_u4le()
            self.default_value = self._io.read_u4le()
            self.n_column_maps = self._io.read_u4le()
            self.block_allocation_increment = self._io.read_u4le()
            self.column_maps = []
            for i in range(self.n_column_maps):
                self.column_maps.append(Metadata.ColumnMap(self._io, self, self._root, self._is_le))

            self.column_order_size = self._io.read_u4le()
            self.column_order_type = Metadata.TypeName(u"Array", self._io, self, self._root, self._is_le)
            self.column_order_version = self._io.read_u4le()
            self.n_column_order_shape = self._io.read_u4le()
            self.column_order_shape = []
            for i in range(self.n_column_order_shape):
                self.column_order_shape.append(self._io.read_u4le())

            self.n_column_order = self._io.read_u4le()
            self.column_order = []
            for i in range(self.n_column_order):
                self.column_order.append(Metadata.String(self._io, self, self._root, self._is_le))

            _on = self.version
            if _on == 2:
                self.row_order = Metadata.ColumnRowDetails32b(self._io, self, self._root, self._is_le)
            elif _on == 1:
                self.row_order = Metadata.ColumnRowDetails64b(self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.column_map_size = self._io.read_u4be()
            self.column_map_type = Metadata.TypeName(u"SimpleOrderedMap", self._io, self, self._root, self._is_le)
            self.column_map_version = self._io.read_u4be()
            self.default_value = self._io.read_u4be()
            self.n_column_maps = self._io.read_u4be()
            self.block_allocation_increment = self._io.read_u4be()
            self.column_maps = []
            for i in range(self.n_column_maps):
                self.column_maps.append(Metadata.ColumnMap(self._io, self, self._root, self._is_le))

            self.column_order_size = self._io.read_u4be()
            self.column_order_type = Metadata.TypeName(u"Array", self._io, self, self._root, self._is_le)
            self.column_order_version = self._io.read_u4be()
            self.n_column_order_shape = self._io.read_u4be()
            self.column_order_shape = []
            for i in range(self.n_column_order_shape):
                self.column_order_shape.append(self._io.read_u4be())

            self.n_column_order = self._io.read_u4be()
            self.column_order = []
            for i in range(self.n_column_order):
                self.column_order.append(Metadata.String(self._io, self, self._root, self._is_le))

            _on = self.version
            if _on == 2:
                self.row_order = Metadata.ColumnRowDetails32b(self._io, self, self._root, self._is_le)
            elif _on == 1:
                self.row_order = Metadata.ColumnRowDetails64b(self._io, self, self._root, self._is_le)

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = 2
            return getattr(self, '_m_type', None)


    class UnknownInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/unknown_info")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.idk = self._io.read_u1()

        def _read_be(self):
            self.idk = self._io.read_u1()


    class Iposition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/iposition")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            self.n_elements = self._io.read_u4le()
            self.elements = []
            for i in range(self.n_elements):
                _on = self.version
                if _on == 1:
                    self.elements.append(self._io.read_u4le())
                elif _on == 2:
                    self.elements.append(self._io.read_u8le())


        def _read_be(self):
            self.type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4be()
            self.n_elements = self._io.read_u4be()
            self.elements = []
            for i in range(self.n_elements):
                _on = self.version
                if _on == 1:
                    self.elements.append(self._io.read_u4be())
                elif _on == 2:
                    self.elements.append(self._io.read_u8be())



    class ColumnsetOptionsType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/columnset_options_type")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.value = self._io.read_s4le()
            self.block_size = self._io.read_u4le()

        def _read_be(self):
            self.value = self._io.read_s4be()
            self.block_size = self._io.read_u4be()


    class SubrecordDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/subrecord_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.size = self._io.read_u4le()
            self.type = Metadata.TypeName(u"RecordDesc", self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            self.n_fields = self._io.read_s4le()
            self.comment = Metadata.String(self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.TypeName(u"RecordDesc", self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4be()
            self.n_fields = self._io.read_s4be()
            self.comment = Metadata.String(self._io, self, self._root, self._is_le)


    class ColumnRowDetails64b(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/column_row_details_64b")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.num_maps_base = self._io.read_u8le()
            self.has_row_order = self._io.read_u1()
            self.num_maps = self._io.read_u8le()
            self.maps = []
            for i in range(self.num_maps):
                self.maps.append(self._io.read_u4le())


        def _read_be(self):
            self.num_maps_base = self._io.read_u8be()
            self.has_row_order = self._io.read_u1()
            self.num_maps = self._io.read_u8be()
            self.maps = []
            for i in range(self.num_maps):
                self.maps.append(self._io.read_u4be())



    class TableDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/table_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.size = self._io.read_u4le()
            self.type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            _on = self.type.value
            if _on == u"TableDesc":
                self.table = Metadata.RegularTableDesc(self._io, self, self._root, self._is_le)
            elif _on == u"RefTable":
                self.table = Metadata.ReferenceTableDesc(self.version, self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4be()
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            _on = self.type.value
            if _on == u"TableDesc":
                self.table = Metadata.RegularTableDesc(self._io, self, self._root, self._is_le)
            elif _on == u"RefTable":
                self.table = Metadata.ReferenceTableDesc(self.version, self._io, self, self._root, self._is_le)


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/string")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.length = self._io.read_u4le()
            self.value = (self._io.read_bytes(self.length)).decode(u"ASCII")

        def _read_be(self):
            self.length = self._io.read_u4be()
            self.value = (self._io.read_bytes(self.length)).decode(u"ASCII")


    class ColumnSpec(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/column_spec")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.n_cols = self._io.read_u4le()
            self.column_desc = []
            for i in range(self.n_cols):
                self.column_desc.append(Metadata.ColumnDesc(self._io, self, self._root, self._is_le))

            self.column_set = Metadata.StorageDesc(self._io, self, self._root, self._is_le)
            self.column_info = []
            for i in range(self.n_cols):
                self.column_info.append(Metadata.StorageDetails(self.column_desc[i].dimensions, self._io, self, self._root, self._is_le))

            self.n_dm_info = self._io.read_u4le()
            self.dminfo = []
            for i in range(16):
                self.dminfo.append(Metadata.DmHeaderInfo(self._io, self, self._root, self._is_le))


        def _read_be(self):
            self.n_cols = self._io.read_u4be()
            self.column_desc = []
            for i in range(self.n_cols):
                self.column_desc.append(Metadata.ColumnDesc(self._io, self, self._root, self._is_le))

            self.column_set = Metadata.StorageDesc(self._io, self, self._root, self._is_le)
            self.column_info = []
            for i in range(self.n_cols):
                self.column_info.append(Metadata.StorageDetails(self.column_desc[i].dimensions, self._io, self, self._root, self._is_le))

            self.n_dm_info = self._io.read_u4be()
            self.dminfo = []
            for i in range(16):
                self.dminfo.append(Metadata.DmHeaderInfo(self._io, self, self._root, self._is_le))



    class Complex8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/complex8")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.real = self._io.read_f4le()
            self.imaginary = self._io.read_f4le()

        def _read_be(self):
            self.real = self._io.read_f4be()
            self.imaginary = self._io.read_f4be()


    class RecordFieldDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/record_field_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.type = self._io.read_s4le()
            if self.type == 12:
                self.subtable_filler = self._io.read_u4le()

            if self.type == 24:
                self.string_array_filler_size = self._io.read_u4le()

            if self.type == 24:
                self.string_array_filler_iposition = Metadata.Iposition(self._io, self, self._root, self._is_le)

            if self.type != 25:
                self.comment = Metadata.String(self._io, self, self._root, self._is_le)

            if self.type == 25:
                self.subrecord = Metadata.SubrecordDesc(self._io, self, self._root, self._is_le)


        def _read_be(self):
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.type = self._io.read_s4be()
            if self.type == 12:
                self.subtable_filler = self._io.read_u4be()

            if self.type == 24:
                self.string_array_filler_size = self._io.read_u4be()

            if self.type == 24:
                self.string_array_filler_iposition = Metadata.Iposition(self._io, self, self._root, self._is_le)

            if self.type != 25:
                self.comment = Metadata.String(self._io, self, self._root, self._is_le)

            if self.type == 25:
                self.subrecord = Metadata.SubrecordDesc(self._io, self, self._root, self._is_le)



    class Array(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.type = type
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/array")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.size = self._io.read_u4le()
            self.cxx_type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            self.n_shape = self._io.read_u4le()
            self.shape = []
            for i in range(self.n_shape):
                self.shape.append(self._io.read_u4le())

            self.n_elements = self._io.read_u4le()
            self.elements = []
            for i in range(self.n_elements):
                _on = self.type
                if _on == 14:
                    self.elements.append(Dtype.Int1(self._io, self, self._root))
                elif _on == 17:
                    self.elements.append(Dtype.Uint2(self._io, self, self._root))
                elif _on == 24:
                    self.elements.append(Metadata.String(self._io, self, self._root, self._is_le))
                elif _on == 20:
                    self.elements.append(Dtype.Float4(self._io, self, self._root))
                elif _on == 13:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 19:
                    self.elements.append(Dtype.Uint4(self._io, self, self._root))
                elif _on == 23:
                    self.elements.append(Metadata.Complex16(self._io, self, self._root, self._is_le))
                elif _on == 15:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 21:
                    self.elements.append(Dtype.Float8(self._io, self, self._root))
                elif _on == 16:
                    self.elements.append(Dtype.Int2(self._io, self, self._root))
                elif _on == 18:
                    self.elements.append(Dtype.Int4(self._io, self, self._root))
                elif _on == 22:
                    self.elements.append(Metadata.Complex8(self._io, self, self._root, self._is_le))
                elif _on == 30:
                    self.elements.append(Dtype.Int8(self._io, self, self._root))


        def _read_be(self):
            self.size = self._io.read_u4be()
            self.cxx_type = Metadata.String(self._io, self, self._root, self._is_le)
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
                    self.elements.append(Metadata.String(self._io, self, self._root, self._is_le))
                elif _on == 20:
                    self.elements.append(Dtype.Float4(self._io, self, self._root))
                elif _on == 13:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 19:
                    self.elements.append(Dtype.Uint4(self._io, self, self._root))
                elif _on == 23:
                    self.elements.append(Metadata.Complex16(self._io, self, self._root, self._is_le))
                elif _on == 15:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 21:
                    self.elements.append(Dtype.Float8(self._io, self, self._root))
                elif _on == 16:
                    self.elements.append(Dtype.Int2(self._io, self, self._root))
                elif _on == 18:
                    self.elements.append(Dtype.Int4(self._io, self, self._root))
                elif _on == 22:
                    self.elements.append(Metadata.Complex8(self._io, self, self._root, self._is_le))
                elif _on == 30:
                    self.elements.append(Dtype.Int8(self._io, self, self._root))



    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/block")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.n_rows = self._io.read_u4le()
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            self.size = self._io.read_u4le()
            self.elements = []
            for i in range(self.size):
                self.elements.append(self._io.read_u4le())


        def _read_be(self):
            self.n_rows = self._io.read_u4be()
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4be()
            self.size = self._io.read_u4be()
            self.elements = []
            for i in range(self.size):
                self.elements.append(self._io.read_u4be())



    class SsmInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/ssm_info")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.column_offset = Metadata.Block(self._io, self, self._root, self._is_le)
            self.column_index_map = Metadata.Block(self._io, self, self._root, self._is_le)
            self.filler = self._io.read_u4le()

        def _read_be(self):
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.column_offset = Metadata.Block(self._io, self, self._root, self._is_le)
            self.column_index_map = Metadata.Block(self._io, self, self._root, self._is_le)
            self.filler = self._io.read_u4be()


    class ColumnRowDetails32b(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/column_row_details_32b")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.n_maps_base = self._io.read_u4le()
            self.has_row_order = self._io.read_u1()
            self.n_maps = self._io.read_u4le()
            self.maps = []
            for i in range(self.n_maps):
                self.maps.append(self._io.read_u4le())


        def _read_be(self):
            self.n_maps_base = self._io.read_u4be()
            self.has_row_order = self._io.read_u1()
            self.n_maps = self._io.read_u4be()
            self.maps = []
            for i in range(self.n_maps):
                self.maps.append(self._io.read_u4be())



    class DmInfo(KaitaiStruct):
        def __init__(self, ncolumns, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.ncolumns = ncolumns
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/dm_info")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.n_column_sets = Metadata.Array(self.ncolumns, self._io, self, self._root, self._is_le)
            self.column_bucket_offset = Metadata.Array(self.ncolumns, self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.n_column_sets = Metadata.Array(self.ncolumns, self._io, self, self._root, self._is_le)
            self.column_bucket_offset = Metadata.Array(self.ncolumns, self._io, self, self._root, self._is_le)


    class Default(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.type = type
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/default")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            _on = self.type
            if _on == 10:
                self.value = Metadata.Complex16(self._io, self, self._root, self._is_le)
            elif _on == 0:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 4:
                self.value = Dtype.Uint2(self._io, self, self._root)
            elif _on == 6:
                self.value = Dtype.Uint4(self._io, self, self._root)
            elif _on == 7:
                self.value = Dtype.Float4(self._io, self, self._root)
            elif _on == 1:
                self.value = Dtype.Int1(self._io, self, self._root)
            elif _on == 11:
                self.value = Metadata.String(self._io, self, self._root, self._is_le)
            elif _on == 3:
                self.value = Dtype.Int2(self._io, self, self._root)
            elif _on == 5:
                self.value = Dtype.Int4(self._io, self, self._root)
            elif _on == 8:
                self.value = Dtype.Float8(self._io, self, self._root)
            elif _on == 9:
                self.value = Metadata.Complex8(self._io, self, self._root, self._is_le)
            elif _on == 2:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 29:
                self.value = Dtype.Int8(self._io, self, self._root)
            else:
                self.value = Metadata.Array(self.type, self._io, self, self._root, self._is_le)

        def _read_be(self):
            _on = self.type
            if _on == 10:
                self.value = Metadata.Complex16(self._io, self, self._root, self._is_le)
            elif _on == 0:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 4:
                self.value = Dtype.Uint2(self._io, self, self._root)
            elif _on == 6:
                self.value = Dtype.Uint4(self._io, self, self._root)
            elif _on == 7:
                self.value = Dtype.Float4(self._io, self, self._root)
            elif _on == 1:
                self.value = Dtype.Int1(self._io, self, self._root)
            elif _on == 11:
                self.value = Metadata.String(self._io, self, self._root, self._is_le)
            elif _on == 3:
                self.value = Dtype.Int2(self._io, self, self._root)
            elif _on == 5:
                self.value = Dtype.Int4(self._io, self, self._root)
            elif _on == 8:
                self.value = Dtype.Float8(self._io, self, self._root)
            elif _on == 9:
                self.value = Metadata.Complex8(self._io, self, self._root, self._is_le)
            elif _on == 2:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 29:
                self.value = Dtype.Int8(self._io, self, self._root)
            else:
                self.value = Metadata.Array(self.type, self._io, self, self._root, self._is_le)


    class IsmInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/ism_info")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.idk = self._io.read_u4le()

        def _read_be(self):
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.idk = self._io.read_u4be()


    class RegularTableDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/regular_table_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.version = Metadata.String(self._io, self, self._root, self._is_le)
            self.comment = Metadata.String(self._io, self, self._root, self._is_le)
            self.table_keywords = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            self.private_keywords = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            self.columns = Metadata.ColumnSpec(self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.version = Metadata.String(self._io, self, self._root, self._is_le)
            self.comment = Metadata.String(self._io, self, self._root, self._is_le)
            self.table_keywords = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            self.private_keywords = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            self.columns = Metadata.ColumnSpec(self._io, self, self._root, self._is_le)

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = 1
            return getattr(self, '_m_type', None)


    class RecordFieldValue(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.type = type
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/record_field_value")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.value = Metadata.DataValue(self.type, self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.value = Metadata.DataValue(self.type, self._io, self, self._root, self._is_le)


    class StorageDetails(KaitaiStruct):
        def __init__(self, dimensionality, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.dimensionality = dimensionality
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/storage_details")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.version = self._io.read_u4le()
            if self.version == 1:
                self.column_keyword_set = Metadata.TableRecord(self._io, self, self._root, self._is_le)

            self.column_name = Metadata.String(self._io, self, self._root, self._is_le)
            self.column_version = self._io.read_u4le()
            self.manager_number = self._io.read_u4le()
            if self.dimensionality > 0:
                self.array_details = Metadata.ArrayColumnStorageDetails(self._io, self, self._root, self._is_le)

            if self.dimensionality < 0:
                self.array_shape_in_column = self._io.read_u1()


        def _read_be(self):
            self.version = self._io.read_u4be()
            if self.version == 1:
                self.column_keyword_set = Metadata.TableRecord(self._io, self, self._root, self._is_le)

            self.column_name = Metadata.String(self._io, self, self._root, self._is_le)
            self.column_version = self._io.read_u4be()
            self.manager_number = self._io.read_u4be()
            if self.dimensionality > 0:
                self.array_details = Metadata.ArrayColumnStorageDetails(self._io, self, self._root, self._is_le)

            if self.dimensionality < 0:
                self.array_shape_in_column = self._io.read_u1()



    class StorageDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/storage_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.version = self._io.read_s4le()
            _on = self.version
            if _on == -1:
                self.nrows = self._io.read_u4le()
            elif _on == -2:
                self.nrows = self._io.read_u4le()
            elif _on == -3:
                self.nrows = self._io.read_u8le()
            if self.version == -3:
                self.options = Metadata.ColumnsetOptionsType(self._io, self, self._root, self._is_le)

            self.sequence_number = self._io.read_u4le()
            self.n_managers = self._io.read_u4le()
            self.managers = []
            for i in range(self.n_managers):
                self.managers.append(Metadata.ColumnsetManager(self._io, self, self._root, self._is_le))


        def _read_be(self):
            self.version = self._io.read_s4be()
            _on = self.version
            if _on == -1:
                self.nrows = self._io.read_u4be()
            elif _on == -2:
                self.nrows = self._io.read_u4be()
            elif _on == -3:
                self.nrows = self._io.read_u8be()
            if self.version == -3:
                self.options = Metadata.ColumnsetOptionsType(self._io, self, self._root, self._is_le)

            self.sequence_number = self._io.read_u4be()
            self.n_managers = self._io.read_u4be()
            self.managers = []
            for i in range(self.n_managers):
                self.managers.append(Metadata.ColumnsetManager(self._io, self, self._root, self._is_le))



    class TypeName(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self.value = value
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/type_name")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.size = self._io.read_u4le()
            self.name = (self._io.read_bytes(len(self.value))).decode(u"ASCII")
            if not self.name == self.value:
                raise kaitaistruct.ValidationNotEqualError(self.value, self.name, self._io, u"/types/type_name/seq/1")

        def _read_be(self):
            self.size = self._io.read_u4be()
            self.name = (self._io.read_bytes(len(self.value))).decode(u"ASCII")
            if not self.name == self.value:
                raise kaitaistruct.ValidationNotEqualError(self.value, self.name, self._io, u"/types/type_name/seq/1")


    class ColumnDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/column_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.version = self._io.read_u4le()
            self.cxx_type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version_parent = self._io.read_u4le()
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.comment = Metadata.String(self._io, self, self._root, self._is_le)
            self.manager_type = Metadata.String(self._io, self, self._root, self._is_le)
            self.manager_group = Metadata.String(self._io, self, self._root, self._is_le)
            self.data_type = self._io.read_s4le()
            self.options = self._io.read_s4le()
            self.dimensions = self._io.read_s4le()
            self.max_length = self._io.read_s4le()
            if self.dimensions != 0:
                self.shape = Metadata.Iposition(self._io, self, self._root, self._is_le)

            if self.dimensions != 0:
                self.max_length_of_string = self._io.read_u4le()

            self.keywords = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            self.column_template_class_version = self._io.read_u4le()
            if  ((self.dimensions == 0) and (self.data_type != 25)) :
                self.default = Metadata.Default(self.data_type, self._io, self, self._root, self._is_le)

            if  ((self.dimensions != 0) and (self.data_type != 25)) :
                self.dummy_flag = self._io.read_u1()


        def _read_be(self):
            self.version = self._io.read_u4be()
            self.cxx_type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version_parent = self._io.read_u4be()
            self.name = Metadata.String(self._io, self, self._root, self._is_le)
            self.comment = Metadata.String(self._io, self, self._root, self._is_le)
            self.manager_type = Metadata.String(self._io, self, self._root, self._is_le)
            self.manager_group = Metadata.String(self._io, self, self._root, self._is_le)
            self.data_type = self._io.read_s4be()
            self.options = self._io.read_s4be()
            self.dimensions = self._io.read_s4be()
            self.max_length = self._io.read_s4be()
            if self.dimensions != 0:
                self.shape = Metadata.Iposition(self._io, self, self._root, self._is_le)

            if self.dimensions != 0:
                self.max_length_of_string = self._io.read_u4be()

            self.keywords = Metadata.TableRecord(self._io, self, self._root, self._is_le)
            self.column_template_class_version = self._io.read_u4be()
            if  ((self.dimensions == 0) and (self.data_type != 25)) :
                self.default = Metadata.Default(self.data_type, self._io, self, self._root, self._is_le)

            if  ((self.dimensions != 0) and (self.data_type != 25)) :
                self.dummy_flag = self._io.read_u1()



    class ColumnsetManager(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/columnset_manager")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.cxx_type = Metadata.String(self._io, self, self._root, self._is_le)
            self.sequence_number = self._io.read_u4le()

        def _read_be(self):
            self.cxx_type = Metadata.String(self._io, self, self._root, self._is_le)
            self.sequence_number = self._io.read_u4be()


    class Complex16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/complex16")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.real = self._io.read_f8le()
            self.imaginary = self._io.read_f8le()

        def _read_be(self):
            self.real = self._io.read_f8be()
            self.imaginary = self._io.read_f8be()


    class ColumnMap(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/column_map")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.key = Metadata.String(self._io, self, self._root, self._is_le)
            self.val = Metadata.String(self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.key = Metadata.String(self._io, self, self._root, self._is_le)
            self.val = Metadata.String(self._io, self, self._root, self._is_le)


    class RecordDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/record_desc")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.size = self._io.read_u4le()
            self.type = Metadata.TypeName(u"RecordDesc", self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            self.n_keywords = self._io.read_s4le()
            self.fields = []
            for i in range(self.n_keywords):
                self.fields.append(Metadata.RecordFieldDesc(self._io, self, self._root, self._is_le))

            self.record_type = self._io.read_s4le()
            self.values = []
            for i in range(self.n_keywords):
                self.values.append(Metadata.RecordFieldValue(self.fields[i].type, self._io, self, self._root, self._is_le))


        def _read_be(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.TypeName(u"RecordDesc", self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4be()
            self.n_keywords = self._io.read_s4be()
            self.fields = []
            for i in range(self.n_keywords):
                self.fields.append(Metadata.RecordFieldDesc(self._io, self, self._root, self._is_le))

            self.record_type = self._io.read_s4be()
            self.values = []
            for i in range(self.n_keywords):
                self.values.append(Metadata.RecordFieldValue(self.fields[i].type, self._io, self, self._root, self._is_le))



    class TableRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/table_record")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.size = self._io.read_u4le()
            self.type = Metadata.TypeName(u"TableRecord", self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            self.desc = Metadata.RecordDesc(self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.TypeName(u"TableRecord", self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4be()
            self.desc = Metadata.RecordDesc(self._io, self, self._root, self._is_le)


    class DmHeaderInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None, _is_le=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._is_le = _is_le
            self._read()

        def _read(self):
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/dm_header_info")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\xBE\xBE\xBE\xBE":
                raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/types/dm_header_info/seq/0")
            self.size = self._io.read_u4le()
            self.type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4le()
            _on = self.type.value
            if _on == u"ISM":
                self.column_offset = Metadata.IsmInfo(self._io, self, self._root, self._is_le)
            elif _on == u"SSM":
                self.column_offset = Metadata.SsmInfo(self._io, self, self._root, self._is_le)
            else:
                self.column_offset = Metadata.UnknownInfo(self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\xBE\xBE\xBE\xBE":
                raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/types/dm_header_info/seq/0")
            self.size = self._io.read_u4be()
            self.type = Metadata.String(self._io, self, self._root, self._is_le)
            self.version = self._io.read_u4be()
            _on = self.type.value
            if _on == u"ISM":
                self.column_offset = Metadata.IsmInfo(self._io, self, self._root, self._is_le)
            elif _on == u"SSM":
                self.column_offset = Metadata.SsmInfo(self._io, self, self._root, self._is_le)
            else:
                self.column_offset = Metadata.UnknownInfo(self._io, self, self._root, self._is_le)


    @property
    def version_bytes(self):
        if hasattr(self, '_m_version_bytes'):
            return self._m_version_bytes

        _pos = self._io.pos()
        self._io.seek(17)
        if self._is_le:
            self._m_version_bytes = self._io.read_u4be()
        else:
            self._m_version_bytes = self._io.read_u4be()
        self._io.seek(_pos)
        return getattr(self, '_m_version_bytes', None)


