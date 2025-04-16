# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from .dtype import Dtype

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class RegularTableDescription(KaitaiStruct):
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
        self.desc = RegularTableDescription.TableDesc(self._io, self, self._root)

    class ArrayColumnStorageDetails(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.shape_column_definition = self._io.read_u1()
            if self.shape_column_definition > 0:
                self.filler = self._io.read_u4be()

            if self.shape_column_definition > 0:
                self.shape = RegularTableDescription.Iposition(self._io, self, self._root)



    class DataValue(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self._read()

        def _read(self):
            _on = self.type
            if _on == 10:
                self.value = RegularTableDescription.Complex16(self._io, self, self._root)
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
                self.value = RegularTableDescription.String(self._io, self, self._root)
            elif _on == 12:
                self.value = RegularTableDescription.String(self._io, self, self._root)
            elif _on == 3:
                self.value = Dtype.Int2(self._io, self, self._root)
            elif _on == 5:
                self.value = Dtype.Int4(self._io, self, self._root)
            elif _on == 8:
                self.value = Dtype.Float8(self._io, self, self._root)
            elif _on == 9:
                self.value = RegularTableDescription.Complex8(self._io, self, self._root)
            elif _on == 2:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 29:
                self.value = Dtype.Int8(self._io, self, self._root)
            elif _on == 25:
                self.value = RegularTableDescription.TableRecord(self._io, self, self._root)
            else:
                self.value = RegularTableDescription.Array(self.type, self._io, self, self._root)


    class UnknownInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.idk = self._io.read_u1()


    class Iposition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = RegularTableDescription.String(self._io, self, self._root)
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
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s4be()
            self.block_size = self._io.read_u4be()


    class SubrecordDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = RegularTableDescription.TypeName(u"RecordDesc", self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.n_fields = self._io.read_s4be()
            self.comment = RegularTableDescription.String(self._io, self, self._root)


    class TableDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = RegularTableDescription.String(self._io, self, self._root)
            self.comment = RegularTableDescription.String(self._io, self, self._root)
            self.table_keywords = RegularTableDescription.TableRecord(self._io, self, self._root)
            self.private_keywords = RegularTableDescription.TableRecord(self._io, self, self._root)
            self.columns = RegularTableDescription.ColumnSpec(self._io, self, self._root)


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4be()
            self.value = (self._io.read_bytes(self.length)).decode(u"ASCII")


    class ColumnSpec(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.n_cols = self._io.read_u4be()
            self.column_desc = []
            for i in range(self.n_cols):
                self.column_desc.append(RegularTableDescription.ColumnDesc(self._io, self, self._root))

            self.column_set = RegularTableDescription.StorageDesc(self._io, self, self._root)
            self.column_info = []
            for i in range(self.n_cols):
                self.column_info.append(RegularTableDescription.StorageDetails(self.column_desc[i].dimensions, self._io, self, self._root))

            self.n_dm_info = self._io.read_u4be()
            self.dminfo = []
            for i in range(16):
                self.dminfo.append(RegularTableDescription.DmHeaderInfo(self._io, self, self._root))



    class Complex8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.real = self._io.read_f4be()
            self.imaginary = self._io.read_f4be()


    class RecordFieldDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = RegularTableDescription.String(self._io, self, self._root)
            self.type = self._io.read_s4be()
            if self.type == 12:
                self.subtable_filler = self._io.read_u4be()

            if self.type == 24:
                self.string_array_filler_size = self._io.read_u4be()

            if self.type == 24:
                self.string_array_filler_iposition = RegularTableDescription.Iposition(self._io, self, self._root)

            if self.type != 25:
                self.comment = RegularTableDescription.String(self._io, self, self._root)

            if self.type == 25:
                self.subrecord = RegularTableDescription.SubrecordDesc(self._io, self, self._root)



    class Array(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.cxx_type = RegularTableDescription.String(self._io, self, self._root)
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
                    self.elements.append(RegularTableDescription.String(self._io, self, self._root))
                elif _on == 20:
                    self.elements.append(Dtype.Float4(self._io, self, self._root))
                elif _on == 13:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 19:
                    self.elements.append(Dtype.Uint4(self._io, self, self._root))
                elif _on == 23:
                    self.elements.append(RegularTableDescription.Complex16(self._io, self, self._root))
                elif _on == 15:
                    self.elements.append(Dtype.Uint1(self._io, self, self._root))
                elif _on == 21:
                    self.elements.append(Dtype.Float8(self._io, self, self._root))
                elif _on == 16:
                    self.elements.append(Dtype.Int2(self._io, self, self._root))
                elif _on == 18:
                    self.elements.append(Dtype.Int4(self._io, self, self._root))
                elif _on == 22:
                    self.elements.append(RegularTableDescription.Complex8(self._io, self, self._root))
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
            self.name = RegularTableDescription.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.size = self._io.read_u4be()
            self.elements = []
            for i in range(self.size):
                self.elements.append(self._io.read_u4be())



    class SsmInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = RegularTableDescription.String(self._io, self, self._root)
            self.column_offset = RegularTableDescription.Block(self._io, self, self._root)
            self.column_index_map = RegularTableDescription.Block(self._io, self, self._root)
            self.filler = self._io.read_u4be()


    class Default(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self._read()

        def _read(self):
            _on = self.type
            if _on == 10:
                self.value = RegularTableDescription.Complex16(self._io, self, self._root)
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
                self.value = RegularTableDescription.String(self._io, self, self._root)
            elif _on == 3:
                self.value = Dtype.Int2(self._io, self, self._root)
            elif _on == 5:
                self.value = Dtype.Int4(self._io, self, self._root)
            elif _on == 8:
                self.value = Dtype.Float8(self._io, self, self._root)
            elif _on == 9:
                self.value = RegularTableDescription.Complex8(self._io, self, self._root)
            elif _on == 2:
                self.value = Dtype.Uint1(self._io, self, self._root)
            elif _on == 29:
                self.value = Dtype.Int8(self._io, self, self._root)
            else:
                self.value = RegularTableDescription.Array(self.type, self._io, self, self._root)


    class IsmInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = RegularTableDescription.String(self._io, self, self._root)
            self.idk = self._io.read_u4be()


    class RecordFieldValue(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self._read()

        def _read(self):
            self.value = RegularTableDescription.DataValue(self.type, self._io, self, self._root)


    class StorageDetails(KaitaiStruct):
        def __init__(self, dimensionality, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.dimensionality = dimensionality
            self._read()

        def _read(self):
            self.version = self._io.read_u4be()
            if self.version == 1:
                self.column_keyword_set = RegularTableDescription.TableRecord(self._io, self, self._root)

            self.column_name = RegularTableDescription.String(self._io, self, self._root)
            self.column_version = self._io.read_u4be()
            self.manager_number = self._io.read_u4be()
            if self.dimensionality > 0:
                self.array_details = RegularTableDescription.ArrayColumnStorageDetails(self._io, self, self._root)

            if self.dimensionality < 0:
                self.array_shape_in_column = self._io.read_u1()



    class StorageDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_s4be()
            _on = self.version
            if _on == -1:
                self.nrows = self._io.read_u4be()
            elif _on == -2:
                self.nrows = self._io.read_u4be()
            elif _on == -3:
                self.nrows = self._io.read_u8be()
            if self.version == -3:
                self.options = RegularTableDescription.ColumnsetOptionsType(self._io, self, self._root)

            self.sequence_number = self._io.read_u4be()
            self.n_managers = self._io.read_u4be()
            self.managers = []
            for i in range(self.n_managers):
                self.managers.append(RegularTableDescription.ColumnsetManager(self._io, self, self._root))



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


    class ColumnDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u4be()
            self.cxx_type = RegularTableDescription.String(self._io, self, self._root)
            self.version_parent = self._io.read_u4be()
            self.name = RegularTableDescription.String(self._io, self, self._root)
            self.comment = RegularTableDescription.String(self._io, self, self._root)
            self.manager_type = RegularTableDescription.String(self._io, self, self._root)
            self.manager_group = RegularTableDescription.String(self._io, self, self._root)
            self.data_type = self._io.read_s4be()
            self.options = self._io.read_s4be()
            self.dimensions = self._io.read_s4be()
            self.max_length = self._io.read_s4be()
            if self.dimensions != 0:
                self.shape = RegularTableDescription.Iposition(self._io, self, self._root)

            if self.dimensions != 0:
                self.max_length_of_string = self._io.read_u4be()

            self.keywords = RegularTableDescription.TableRecord(self._io, self, self._root)
            self.column_template_class_version = self._io.read_u4be()
            if  ((self.dimensions == 0) and (self.data_type != 25)) :
                self.default = RegularTableDescription.Default(self.data_type, self._io, self, self._root)

            if  ((self.dimensions != 0) and (self.data_type != 25)) :
                self.dummy_flag = self._io.read_u1()



    class ColumnsetManager(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cxx_type = RegularTableDescription.String(self._io, self, self._root)
            self.sequence_number = self._io.read_u4be()


    class Complex16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.real = self._io.read_f8be()
            self.imaginary = self._io.read_f8be()


    class RecordDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = RegularTableDescription.TypeName(u"RecordDesc", self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.n_keywords = self._io.read_s4be()
            self.fields = []
            for i in range(self.n_keywords):
                self.fields.append(RegularTableDescription.RecordFieldDesc(self._io, self, self._root))

            self.record_type = self._io.read_s4be()
            self.values = []
            for i in range(self.n_keywords):
                self.values.append(RegularTableDescription.RecordFieldValue(self.fields[i].type, self._io, self, self._root))



    class TableRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = RegularTableDescription.TypeName(u"TableRecord", self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.desc = RegularTableDescription.RecordDesc(self._io, self, self._root)


    class DmHeaderInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\xBE\xBE\xBE\xBE":
                raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/types/dm_header_info/seq/0")
            self.size = self._io.read_u4be()
            self.type = RegularTableDescription.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            _on = self.type.value
            if _on == u"ISM":
                self.column_offset = RegularTableDescription.IsmInfo(self._io, self, self._root)
            elif _on == u"SSM":
                self.column_offset = RegularTableDescription.SsmInfo(self._io, self, self._root)
            else:
                self.column_offset = RegularTableDescription.UnknownInfo(self._io, self, self._root)



