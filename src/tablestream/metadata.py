# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Metadata(KaitaiStruct):
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
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\xBE\xBE\xBE\xBE":
            raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBE\xBE\xBE", self.magic, self._io, u"/seq/0")
        self.size = self._io.read_u4be()
        self.type = Metadata.String(self._io, self, self._root)
        self.version = self._io.read_u4be()
        _on = self.version
        if _on == 1:
            self.nrows = self._io.read_u4be()
        elif _on == 2:
            self.nrows = self._io.read_u4be()
        elif _on == 3:
            self.nrows = self._io.read_u8be()
        self.little_endian = self._io.read_u4be()
        self.name = Metadata.String(self._io, self, self._root)
        self.desc = Metadata.TableDesc(self._io, self, self._root)

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
                self.shape = Metadata.Iposition(self._io, self, self._root)



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
                self.value = Metadata.Complex16(self._io, self, self._root)
            elif _on == 0:
                self.value = self._io.read_u1()
            elif _on == 4:
                self.value = self._io.read_u2be()
            elif _on == 6:
                self.value = self._io.read_u4be()
            elif _on == 7:
                self.value = self._io.read_f4be()
            elif _on == 1:
                self.value = self._io.read_s1()
            elif _on == 11:
                self.value = Metadata.String(self._io, self, self._root)
            elif _on == 12:
                self.value = Metadata.String(self._io, self, self._root)
            elif _on == 3:
                self.value = self._io.read_s2be()
            elif _on == 5:
                self.value = self._io.read_s4be()
            elif _on == 8:
                self.value = self._io.read_f8be()
            elif _on == 9:
                self.value = Metadata.Complex8(self._io, self, self._root)
            elif _on == 2:
                self.value = self._io.read_u1()
            elif _on == 29:
                self.value = self._io.read_s8be()
            elif _on == 25:
                self.value = Metadata.TableRecord(self._io, self, self._root)
            else:
                self.value = Metadata.Array(self.type, self._io, self, self._root)


    class ReferenceTableDesc(KaitaiStruct):
        def __init__(self, version, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.version = version
            self._read()

        def _read(self):
            self.column_map_size = self._io.read_u4be()
            self.column_map_type = Metadata.TypeName(u"SimpleOrderedMap", self._io, self, self._root)
            self.column_map_version = self._io.read_u4be()
            self.default_value = self._io.read_u4be()
            self.n_column_maps = self._io.read_u4be()
            self.block_allocation_increment = self._io.read_u4be()
            self.column_maps = []
            for i in range(self.n_column_maps):
                self.column_maps.append(Metadata.ColumnMap(self._io, self, self._root))

            self.column_order_size = self._io.read_u4be()
            self.column_order_type = Metadata.TypeName(u"Array", self._io, self, self._root)
            self.column_order_version = self._io.read_u4be()
            self.n_column_order_shape = self._io.read_u4be()
            self.column_order_shape = []
            for i in range(self.n_column_order_shape):
                self.column_order_shape.append(self._io.read_u4be())

            self.n_column_order = self._io.read_u4be()
            self.column_order = []
            for i in range(self.n_column_order):
                self.column_order.append(Metadata.String(self._io, self, self._root))

            _on = self.version
            if _on == 2:
                self.row_order = Metadata.ColumnRowDetails32b(self._io, self, self._root)
            elif _on == 1:
                self.row_order = Metadata.ColumnRowDetails64b(self._io, self, self._root)

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = 2
            return getattr(self, '_m_type', None)


    class Iposition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = Metadata.String(self._io, self, self._root)
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
            self.type = Metadata.TypeName(u"RecordDesc", self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.n_fields = self._io.read_s4be()
            self.comment = Metadata.String(self._io, self, self._root)


    class ColumnRowDetails64b(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_maps_base = self._io.read_u8be()
            self.has_row_order = self._io.read_u1()
            self.num_maps = self._io.read_u8be()
            self.maps = []
            for i in range(self.num_maps):
                self.maps.append(self._io.read_u4be())



    class TableDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.String(self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.name = Metadata.String(self._io, self, self._root)
            _on = self.type.value
            if _on == u"TableDesc":
                self.table = Metadata.RegularTableDesc(self._io, self, self._root)
            elif _on == u"RefTable":
                self.table = Metadata.ReferenceTableDesc(self.version, self._io, self, self._root)


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
            self.details = []
            for i in range(self.n_cols):
                self.details.append(Metadata.ColumnDetails(self._io, self, self._root))

            self.storage = Metadata.StorageDesc(self._io, self, self._root)
            self.storage_details = []
            for i in range(self.n_cols):
                self.storage_details.append(Metadata.StorageDetails(self.details[i].dimensions, self._io, self, self._root))

            self.n_data_manager_info = self._io.read_u4be()
            self.data_manager_info = []
            for i in range(self.n_data_manager_info):
                self.data_manager_info.append(self._io.read_u1())



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
            self.name = Metadata.String(self._io, self, self._root)
            self.type = self._io.read_s4be()
            if self.type == 12:
                self.subtable_filler = self._io.read_u4be()

            if self.type == 24:
                self.string_array_filler_size = self._io.read_u4be()

            if self.type == 24:
                self.string_array_filler_iposition = Metadata.Iposition(self._io, self, self._root)

            if self.type != 25:
                self.comment = Metadata.String(self._io, self, self._root)

            if self.type == 25:
                self.subrecord = Metadata.SubrecordDesc(self._io, self, self._root)



    class Array(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.cxx_type = Metadata.String(self._io, self, self._root)
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
                    self.elements.append(self._io.read_s1())
                elif _on == 17:
                    self.elements.append(self._io.read_u2be())
                elif _on == 24:
                    self.elements.append(Metadata.String(self._io, self, self._root))
                elif _on == 20:
                    self.elements.append(self._io.read_f4be())
                elif _on == 13:
                    self.elements.append(self._io.read_u1())
                elif _on == 19:
                    self.elements.append(self._io.read_u4be())
                elif _on == 23:
                    self.elements.append(Metadata.Complex16(self._io, self, self._root))
                elif _on == 15:
                    self.elements.append(self._io.read_u1())
                elif _on == 21:
                    self.elements.append(self._io.read_f8be())
                elif _on == 16:
                    self.elements.append(self._io.read_s2be())
                elif _on == 18:
                    self.elements.append(self._io.read_s4be())
                elif _on == 22:
                    self.elements.append(Metadata.Complex8(self._io, self, self._root))
                elif _on == 30:
                    self.elements.append(self._io.read_s8be())



    class Hacky(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.String(self._io, self, self._root)


    class ColumnRowDetails32b(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.n_maps_base = self._io.read_u4be()
            self.has_row_order = self._io.read_u1()
            self.n_maps = self._io.read_u4be()
            self.maps = []
            for i in range(self.n_maps):
                self.maps.append(self._io.read_u4be())



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
                self.value = Metadata.Complex16(self._io, self, self._root)
            elif _on == 0:
                self.value = self._io.read_u1()
            elif _on == 4:
                self.value = self._io.read_u2be()
            elif _on == 6:
                self.value = self._io.read_u4be()
            elif _on == 7:
                self.value = self._io.read_f4be()
            elif _on == 1:
                self.value = self._io.read_s1()
            elif _on == 11:
                self.value = Metadata.String(self._io, self, self._root)
            elif _on == 3:
                self.value = self._io.read_s2be()
            elif _on == 5:
                self.value = self._io.read_s4be()
            elif _on == 8:
                self.value = self._io.read_f8be()
            elif _on == 9:
                self.value = Metadata.Complex8(self._io, self, self._root)
            elif _on == 2:
                self.value = self._io.read_u1()
            elif _on == 29:
                self.value = self._io.read_s8be()
            else:
                self.value = Metadata.Array(self.type, self._io, self, self._root)


    class RegularTableDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.desc_version = Metadata.String(self._io, self, self._root)
            self.comment = Metadata.String(self._io, self, self._root)
            self.user_keywords = Metadata.TableRecord(self._io, self, self._root)
            self.private_keywords = Metadata.TableRecord(self._io, self, self._root)
            self.columns = Metadata.ColumnSpec(self._io, self, self._root)

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = 1
            return getattr(self, '_m_type', None)


    class RecordFieldValue(KaitaiStruct):
        def __init__(self, type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self._read()

        def _read(self):
            self.value = Metadata.DataValue(self.type, self._io, self, self._root)


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
                self.column_keyword_set = Metadata.TableRecord(self._io, self, self._root)

            self.column_name = Metadata.String(self._io, self, self._root)
            self.column_version = self._io.read_u4be()
            self.manager_number = self._io.read_u4be()
            if self.dimensionality > 0:
                self.array_details = Metadata.ArrayColumnStorageDetails(self._io, self, self._root)

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
                self.options = Metadata.ColumnsetOptionsType(self._io, self, self._root)

            self.sequence_number = self._io.read_u4be()
            self.n_managers = self._io.read_u4be()
            self.managers = []
            for i in range(self.n_managers):
                self.managers.append(Metadata.ColumnsetManager(self._io, self, self._root))



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


    class ColumnDetails(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u4be()
            self.cxx_type = Metadata.String(self._io, self, self._root)
            self.version_parent = self._io.read_u4be()
            self.name = Metadata.String(self._io, self, self._root)
            self.comment = Metadata.String(self._io, self, self._root)
            self.manager_type = Metadata.String(self._io, self, self._root)
            self.manager_group = Metadata.String(self._io, self, self._root)
            self.data_type = self._io.read_s4be()
            self.options = self._io.read_s4be()
            self.dimensions = self._io.read_s4be()
            self.max_length = self._io.read_s4be()
            if self.dimensions != 0:
                self.shape = Metadata.Iposition(self._io, self, self._root)

            if self.dimensions != 0:
                self.max_length_of_string = self._io.read_u4be()

            self.keywords = Metadata.TableRecord(self._io, self, self._root)
            self.column_template_class_version = self._io.read_u4be()
            if  ((self.dimensions == 0) and (self.data_type != 25)) :
                self.default = Metadata.Default(self.data_type, self._io, self, self._root)

            if  ((self.dimensions != 0) and (self.data_type != 25)) :
                self.dummy_flag = self._io.read_u1()



    class ColumnsetManager(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cxx_type = Metadata.String(self._io, self, self._root)
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


    class ColumnMap(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = Metadata.String(self._io, self, self._root)
            self.val = Metadata.String(self._io, self, self._root)


    class RecordDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.TypeName(u"RecordDesc", self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.n_fields = self._io.read_s4be()
            self.fields = []
            for i in range(self.n_fields):
                self.fields.append(Metadata.RecordFieldDesc(self._io, self, self._root))

            self.record_type = self._io.read_s4be()
            self.values = []
            for i in range(self.n_fields):
                self.values.append(Metadata.RecordFieldValue(self.fields[i].type, self._io, self, self._root))



    class TableRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.type = Metadata.TypeName(u"TableRecord", self._io, self, self._root)
            self.version = self._io.read_u4be()
            self.desc = Metadata.RecordDesc(self._io, self, self._root)



