// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

#include "metadata.h"
#include "kaitai/exceptions.h"

metadata_t::metadata_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = this;
    m_type = nullptr;
    m_name = nullptr;
    m_desc = nullptr;
    _read();
}

void metadata_t::_read() {
    m_magic = m__io->read_bytes(4);
    if (!(magic() == std::string("\xBE\xBE\xBE\xBE", 4))) {
        throw kaitai::validation_not_equal_error<std::string>(std::string("\xBE\xBE\xBE\xBE", 4), magic(), _io(), std::string("/seq/0"));
    }
    m_size = m__io->read_u4be();
    m_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_version = m__io->read_u4be();
    n_nrows = true;
    switch (version()) {
    case 1: {
        n_nrows = false;
        m_nrows = m__io->read_u4be();
        break;
    }
    case 2: {
        n_nrows = false;
        m_nrows = m__io->read_u4be();
        break;
    }
    case 3: {
        n_nrows = false;
        m_nrows = m__io->read_u8be();
        break;
    }
    }
    m_little_endian = m__io->read_u4be();
    m_name = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_desc = std::unique_ptr<table_desc_t>(new table_desc_t(m__io, this, m__root));
}

metadata_t::~metadata_t() {
    _clean_up();
}

void metadata_t::_clean_up() {
    if (!n_nrows) {
    }
}

metadata_t::array_column_storage_details_t::array_column_storage_details_t(kaitai::kstream* p__io, metadata_t::storage_details_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_shape = nullptr;
    _read();
}

void metadata_t::array_column_storage_details_t::_read() {
    m_shape_column_definition = m__io->read_u1();
    n_filler = true;
    if (shape_column_definition() > 0) {
        n_filler = false;
        m_filler = m__io->read_u4be();
    }
    n_shape = true;
    if (shape_column_definition() > 0) {
        n_shape = false;
        m_shape = std::unique_ptr<iposition_t>(new iposition_t(m__io, this, m__root));
    }
}

metadata_t::array_column_storage_details_t::~array_column_storage_details_t() {
    _clean_up();
}

void metadata_t::array_column_storage_details_t::_clean_up() {
    if (!n_filler) {
    }
    if (!n_shape) {
    }
}

metadata_t::data_value_t::data_value_t(uint16_t p_type, kaitai::kstream* p__io, metadata_t::record_field_value_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = p_type;
    _read();
}

void metadata_t::data_value_t::_read() {
    switch (type()) {
    case 10: {
        m_value = std::unique_ptr<dtype_t::complex16_t>(new dtype_t::complex16_t(m__io, this, m__root));
        break;
    }
    case 0: {
        m_value = std::unique_ptr<dtype_t::uint1_t>(new dtype_t::uint1_t(m__io, this, m__root));
        break;
    }
    case 4: {
        m_value = std::unique_ptr<dtype_t::uint2_t>(new dtype_t::uint2_t(m__io, this, m__root));
        break;
    }
    case 6: {
        m_value = std::unique_ptr<dtype_t::uint4_t>(new dtype_t::uint4_t(m__io, this, m__root));
        break;
    }
    case 7: {
        m_value = std::unique_ptr<dtype_t::float4_t>(new dtype_t::float4_t(m__io, this, m__root));
        break;
    }
    case 1: {
        m_value = std::unique_ptr<dtype_t::int1_t>(new dtype_t::int1_t(m__io, this, m__root));
        break;
    }
    case 11: {
        m_value = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
        break;
    }
    case 12: {
        m_value = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
        break;
    }
    case 3: {
        m_value = std::unique_ptr<dtype_t::int2_t>(new dtype_t::int2_t(m__io, this, m__root));
        break;
    }
    case 5: {
        m_value = std::unique_ptr<dtype_t::int4_t>(new dtype_t::int4_t(m__io, this, m__root));
        break;
    }
    case 8: {
        m_value = std::unique_ptr<dtype_t::float8_t>(new dtype_t::float8_t(m__io, this, m__root));
        break;
    }
    case 9: {
        m_value = std::unique_ptr<dtype_t::complex8_t>(new dtype_t::complex8_t(m__io, this, m__root));
        break;
    }
    case 2: {
        m_value = std::unique_ptr<dtype_t::uint1_t>(new dtype_t::uint1_t(m__io, this, m__root));
        break;
    }
    case 29: {
        m_value = std::unique_ptr<dtype_t::int8_t>(new dtype_t::int8_t(m__io, this, m__root));
        break;
    }
    case 25: {
        m_value = std::unique_ptr<table_record_t>(new table_record_t(m__io, this, m__root));
        break;
    }
    default: {
        m_value = std::unique_ptr<array_t>(new array_t(type(), m__io, this, m__root));
        break;
    }
    }
}

metadata_t::data_value_t::~data_value_t() {
    _clean_up();
}

void metadata_t::data_value_t::_clean_up() {
}

metadata_t::reference_table_desc_t::reference_table_desc_t(uint32_t p_version, kaitai::kstream* p__io, metadata_t::table_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_version = p_version;
    m_column_map_type = nullptr;
    m_column_maps = nullptr;
    m_column_order_type = nullptr;
    m_column_order_shape = nullptr;
    m_column_order = nullptr;
    f_type = false;
    _read();
}

void metadata_t::reference_table_desc_t::_read() {
    m_column_map_size = m__io->read_u4be();
    m_column_map_type = std::unique_ptr<type_name_t>(new type_name_t(std::string("SimpleOrderedMap"), m__io, this, m__root));
    m_column_map_version = m__io->read_u4be();
    m_default_value = m__io->read_u4be();
    m_n_column_maps = m__io->read_u4be();
    m_block_allocation_increment = m__io->read_u4be();
    m_column_maps = std::unique_ptr<std::vector<std::unique_ptr<column_map_t>>>(new std::vector<std::unique_ptr<column_map_t>>());
    const int l_column_maps = n_column_maps();
    for (int i = 0; i < l_column_maps; i++) {
        m_column_maps->push_back(std::move(std::unique_ptr<column_map_t>(new column_map_t(m__io, this, m__root))));
    }
    m_column_order_size = m__io->read_u4be();
    m_column_order_type = std::unique_ptr<type_name_t>(new type_name_t(std::string("Array"), m__io, this, m__root));
    m_column_order_version = m__io->read_u4be();
    m_n_column_order_shape = m__io->read_u4be();
    m_column_order_shape = std::unique_ptr<std::vector<uint32_t>>(new std::vector<uint32_t>());
    const int l_column_order_shape = n_column_order_shape();
    for (int i = 0; i < l_column_order_shape; i++) {
        m_column_order_shape->push_back(std::move(m__io->read_u4be()));
    }
    m_n_column_order = m__io->read_u4be();
    m_column_order = std::unique_ptr<std::vector<std::unique_ptr<dtype_t::string_t>>>(new std::vector<std::unique_ptr<dtype_t::string_t>>());
    const int l_column_order = n_column_order();
    for (int i = 0; i < l_column_order; i++) {
        m_column_order->push_back(std::move(std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root))));
    }
    n_row_order = true;
    switch (version()) {
    case 2: {
        n_row_order = false;
        m_row_order = std::unique_ptr<column_row_details_32b_t>(new column_row_details_32b_t(m__io, this, m__root));
        break;
    }
    case 1: {
        n_row_order = false;
        m_row_order = std::unique_ptr<column_row_details_64b_t>(new column_row_details_64b_t(m__io, this, m__root));
        break;
    }
    }
}

metadata_t::reference_table_desc_t::~reference_table_desc_t() {
    _clean_up();
}

void metadata_t::reference_table_desc_t::_clean_up() {
    if (!n_row_order) {
    }
}

int8_t metadata_t::reference_table_desc_t::type() {
    if (f_type)
        return m_type;
    m_type = 2;
    f_type = true;
    return m_type;
}

metadata_t::iposition_t::iposition_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = nullptr;
    m_elements = nullptr;
    _read();
}

void metadata_t::iposition_t::_read() {
    m_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_version = m__io->read_u4be();
    m_n_elements = m__io->read_u4be();
    m_elements = std::unique_ptr<std::vector<uint64_t>>(new std::vector<uint64_t>());
    const int l_elements = n_elements();
    for (int i = 0; i < l_elements; i++) {
        switch (version()) {
        case 1: {
            m_elements->push_back(std::move(m__io->read_u4be()));
            break;
        }
        case 2: {
            m_elements->push_back(std::move(m__io->read_u8be()));
            break;
        }
        }
    }
}

metadata_t::iposition_t::~iposition_t() {
    _clean_up();
}

void metadata_t::iposition_t::_clean_up() {
}

metadata_t::columnset_options_type_t::columnset_options_type_t(kaitai::kstream* p__io, metadata_t::storage_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void metadata_t::columnset_options_type_t::_read() {
    m_value = m__io->read_s4be();
    m_block_size = m__io->read_u4be();
}

metadata_t::columnset_options_type_t::~columnset_options_type_t() {
    _clean_up();
}

void metadata_t::columnset_options_type_t::_clean_up() {
}

metadata_t::subrecord_desc_t::subrecord_desc_t(kaitai::kstream* p__io, metadata_t::record_field_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = nullptr;
    m_comment = nullptr;
    _read();
}

void metadata_t::subrecord_desc_t::_read() {
    m_size = m__io->read_u4be();
    m_type = std::unique_ptr<type_name_t>(new type_name_t(std::string("RecordDesc"), m__io, this, m__root));
    m_version = m__io->read_u4be();
    m_n_fields = m__io->read_s4be();
    m_comment = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
}

metadata_t::subrecord_desc_t::~subrecord_desc_t() {
    _clean_up();
}

void metadata_t::subrecord_desc_t::_clean_up() {
}

metadata_t::column_row_details_64b_t::column_row_details_64b_t(kaitai::kstream* p__io, metadata_t::reference_table_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_maps = nullptr;
    _read();
}

void metadata_t::column_row_details_64b_t::_read() {
    m_num_maps_base = m__io->read_u8be();
    m_has_row_order = m__io->read_u1();
    m_num_maps = m__io->read_u8be();
    m_maps = std::unique_ptr<std::vector<uint32_t>>(new std::vector<uint32_t>());
    const int l_maps = num_maps();
    for (int i = 0; i < l_maps; i++) {
        m_maps->push_back(std::move(m__io->read_u4be()));
    }
}

metadata_t::column_row_details_64b_t::~column_row_details_64b_t() {
    _clean_up();
}

void metadata_t::column_row_details_64b_t::_clean_up() {
}

metadata_t::table_desc_t::table_desc_t(kaitai::kstream* p__io, metadata_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = nullptr;
    m_name = nullptr;
    _read();
}

void metadata_t::table_desc_t::_read() {
    m_size = m__io->read_u4be();
    m_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_version = m__io->read_u4be();
    m_name = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    n_table = true;
    {
        std::string on = type()->value();
        if (on == std::string("TableDesc")) {
            n_table = false;
            m_table = std::unique_ptr<regular_table_desc_t>(new regular_table_desc_t(m__io, this, m__root));
        }
        else if (on == std::string("RefTable")) {
            n_table = false;
            m_table = std::unique_ptr<reference_table_desc_t>(new reference_table_desc_t(version(), m__io, this, m__root));
        }
    }
}

metadata_t::table_desc_t::~table_desc_t() {
    _clean_up();
}

void metadata_t::table_desc_t::_clean_up() {
    if (!n_table) {
    }
}

metadata_t::column_spec_t::column_spec_t(kaitai::kstream* p__io, metadata_t::regular_table_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_details = nullptr;
    m_storage = nullptr;
    m_storage_details = nullptr;
    m_data_manager_info = nullptr;
    _read();
}

void metadata_t::column_spec_t::_read() {
    m_n_cols = m__io->read_u4be();
    m_details = std::unique_ptr<std::vector<std::unique_ptr<column_details_t>>>(new std::vector<std::unique_ptr<column_details_t>>());
    const int l_details = n_cols();
    for (int i = 0; i < l_details; i++) {
        m_details->push_back(std::move(std::unique_ptr<column_details_t>(new column_details_t(m__io, this, m__root))));
    }
    m_storage = std::unique_ptr<storage_desc_t>(new storage_desc_t(m__io, this, m__root));
    m_storage_details = std::unique_ptr<std::vector<std::unique_ptr<storage_details_t>>>(new std::vector<std::unique_ptr<storage_details_t>>());
    const int l_storage_details = n_cols();
    for (int i = 0; i < l_storage_details; i++) {
        m_storage_details->push_back(std::move(std::unique_ptr<storage_details_t>(new storage_details_t(details()->at(i)->dimensions(), m__io, this, m__root))));
    }
    m_n_data_manager_info = m__io->read_u4be();
    m_data_manager_info = std::unique_ptr<std::vector<uint8_t>>(new std::vector<uint8_t>());
    const int l_data_manager_info = n_data_manager_info();
    for (int i = 0; i < l_data_manager_info; i++) {
        m_data_manager_info->push_back(std::move(m__io->read_u1()));
    }
}

metadata_t::column_spec_t::~column_spec_t() {
    _clean_up();
}

void metadata_t::column_spec_t::_clean_up() {
}

metadata_t::record_field_desc_t::record_field_desc_t(kaitai::kstream* p__io, metadata_t::record_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_name = nullptr;
    m_string_array_filler_iposition = nullptr;
    m_comment = nullptr;
    m_subrecord = nullptr;
    _read();
}

void metadata_t::record_field_desc_t::_read() {
    m_name = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_type = m__io->read_s4be();
    n_subtable_filler = true;
    if (type() == 12) {
        n_subtable_filler = false;
        m_subtable_filler = m__io->read_u4be();
    }
    n_string_array_filler_size = true;
    if (type() == 24) {
        n_string_array_filler_size = false;
        m_string_array_filler_size = m__io->read_u4be();
    }
    n_string_array_filler_iposition = true;
    if (type() == 24) {
        n_string_array_filler_iposition = false;
        m_string_array_filler_iposition = std::unique_ptr<iposition_t>(new iposition_t(m__io, this, m__root));
    }
    n_comment = true;
    if (type() != 25) {
        n_comment = false;
        m_comment = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    }
    n_subrecord = true;
    if (type() == 25) {
        n_subrecord = false;
        m_subrecord = std::unique_ptr<subrecord_desc_t>(new subrecord_desc_t(m__io, this, m__root));
    }
}

metadata_t::record_field_desc_t::~record_field_desc_t() {
    _clean_up();
}

void metadata_t::record_field_desc_t::_clean_up() {
    if (!n_subtable_filler) {
    }
    if (!n_string_array_filler_size) {
    }
    if (!n_string_array_filler_iposition) {
    }
    if (!n_comment) {
    }
    if (!n_subrecord) {
    }
}

metadata_t::array_t::array_t(uint16_t p_type, kaitai::kstream* p__io, kaitai::kstruct* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = p_type;
    m_cxx_type = nullptr;
    m_shape = nullptr;
    m_elements = nullptr;
    _read();
}

void metadata_t::array_t::_read() {
    m_size = m__io->read_u4be();
    m_cxx_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_version = m__io->read_u4be();
    m_n_shape = m__io->read_u4be();
    m_shape = std::unique_ptr<std::vector<uint32_t>>(new std::vector<uint32_t>());
    const int l_shape = n_shape();
    for (int i = 0; i < l_shape; i++) {
        m_shape->push_back(std::move(m__io->read_u4be()));
    }
    m_n_elements = m__io->read_u4be();
    m_elements = std::unique_ptr<std::vector<std::unique_ptr<kaitai::kstruct>>>(new std::vector<std::unique_ptr<kaitai::kstruct>>());
    const int l_elements = n_elements();
    for (int i = 0; i < l_elements; i++) {
        switch (type()) {
        case 14: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::int1_t>(new dtype_t::int1_t(m__io, this, m__root))));
            break;
        }
        case 17: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::uint2_t>(new dtype_t::uint2_t(m__io, this, m__root))));
            break;
        }
        case 24: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root))));
            break;
        }
        case 20: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::float4_t>(new dtype_t::float4_t(m__io, this, m__root))));
            break;
        }
        case 13: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::uint1_t>(new dtype_t::uint1_t(m__io, this, m__root))));
            break;
        }
        case 19: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::uint4_t>(new dtype_t::uint4_t(m__io, this, m__root))));
            break;
        }
        case 23: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::complex16_t>(new dtype_t::complex16_t(m__io, this, m__root))));
            break;
        }
        case 15: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::uint1_t>(new dtype_t::uint1_t(m__io, this, m__root))));
            break;
        }
        case 21: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::float8_t>(new dtype_t::float8_t(m__io, this, m__root))));
            break;
        }
        case 16: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::int2_t>(new dtype_t::int2_t(m__io, this, m__root))));
            break;
        }
        case 18: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::int4_t>(new dtype_t::int4_t(m__io, this, m__root))));
            break;
        }
        case 22: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::complex8_t>(new dtype_t::complex8_t(m__io, this, m__root))));
            break;
        }
        case 30: {
            m_elements->push_back(std::move(std::unique_ptr<dtype_t::int8_t>(new dtype_t::int8_t(m__io, this, m__root))));
            break;
        }
        }
    }
}

metadata_t::array_t::~array_t() {
    _clean_up();
}

void metadata_t::array_t::_clean_up() {
}

metadata_t::hacky_t::hacky_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = nullptr;
    _read();
}

void metadata_t::hacky_t::_read() {
    m_size = m__io->read_u4be();
    m_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
}

metadata_t::hacky_t::~hacky_t() {
    _clean_up();
}

void metadata_t::hacky_t::_clean_up() {
}

metadata_t::column_row_details_32b_t::column_row_details_32b_t(kaitai::kstream* p__io, metadata_t::reference_table_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_maps = nullptr;
    _read();
}

void metadata_t::column_row_details_32b_t::_read() {
    m_n_maps_base = m__io->read_u4be();
    m_has_row_order = m__io->read_u1();
    m_n_maps = m__io->read_u4be();
    m_maps = std::unique_ptr<std::vector<uint32_t>>(new std::vector<uint32_t>());
    const int l_maps = n_maps();
    for (int i = 0; i < l_maps; i++) {
        m_maps->push_back(std::move(m__io->read_u4be()));
    }
}

metadata_t::column_row_details_32b_t::~column_row_details_32b_t() {
    _clean_up();
}

void metadata_t::column_row_details_32b_t::_clean_up() {
}

metadata_t::default_t::default_t(uint16_t p_type, kaitai::kstream* p__io, metadata_t::column_details_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = p_type;
    _read();
}

void metadata_t::default_t::_read() {
    switch (type()) {
    case 10: {
        m_value = std::unique_ptr<dtype_t::complex16_t>(new dtype_t::complex16_t(m__io, this, m__root));
        break;
    }
    case 0: {
        m_value = std::unique_ptr<dtype_t::uint1_t>(new dtype_t::uint1_t(m__io, this, m__root));
        break;
    }
    case 4: {
        m_value = std::unique_ptr<dtype_t::uint2_t>(new dtype_t::uint2_t(m__io, this, m__root));
        break;
    }
    case 6: {
        m_value = std::unique_ptr<dtype_t::uint4_t>(new dtype_t::uint4_t(m__io, this, m__root));
        break;
    }
    case 7: {
        m_value = std::unique_ptr<dtype_t::float4_t>(new dtype_t::float4_t(m__io, this, m__root));
        break;
    }
    case 1: {
        m_value = std::unique_ptr<dtype_t::int1_t>(new dtype_t::int1_t(m__io, this, m__root));
        break;
    }
    case 11: {
        m_value = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
        break;
    }
    case 3: {
        m_value = std::unique_ptr<dtype_t::int2_t>(new dtype_t::int2_t(m__io, this, m__root));
        break;
    }
    case 5: {
        m_value = std::unique_ptr<dtype_t::int4_t>(new dtype_t::int4_t(m__io, this, m__root));
        break;
    }
    case 8: {
        m_value = std::unique_ptr<dtype_t::float8_t>(new dtype_t::float8_t(m__io, this, m__root));
        break;
    }
    case 9: {
        m_value = std::unique_ptr<dtype_t::complex8_t>(new dtype_t::complex8_t(m__io, this, m__root));
        break;
    }
    case 2: {
        m_value = std::unique_ptr<dtype_t::uint1_t>(new dtype_t::uint1_t(m__io, this, m__root));
        break;
    }
    case 29: {
        m_value = std::unique_ptr<dtype_t::int8_t>(new dtype_t::int8_t(m__io, this, m__root));
        break;
    }
    default: {
        m_value = std::unique_ptr<array_t>(new array_t(type(), m__io, this, m__root));
        break;
    }
    }
}

metadata_t::default_t::~default_t() {
    _clean_up();
}

void metadata_t::default_t::_clean_up() {
}

metadata_t::regular_table_desc_t::regular_table_desc_t(kaitai::kstream* p__io, metadata_t::table_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_desc_version = nullptr;
    m_comment = nullptr;
    m_user_keywords = nullptr;
    m_private_keywords = nullptr;
    m_columns = nullptr;
    f_type = false;
    _read();
}

void metadata_t::regular_table_desc_t::_read() {
    m_desc_version = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_comment = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_user_keywords = std::unique_ptr<table_record_t>(new table_record_t(m__io, this, m__root));
    m_private_keywords = std::unique_ptr<table_record_t>(new table_record_t(m__io, this, m__root));
    m_columns = std::unique_ptr<column_spec_t>(new column_spec_t(m__io, this, m__root));
}

metadata_t::regular_table_desc_t::~regular_table_desc_t() {
    _clean_up();
}

void metadata_t::regular_table_desc_t::_clean_up() {
}

int8_t metadata_t::regular_table_desc_t::type() {
    if (f_type)
        return m_type;
    m_type = 1;
    f_type = true;
    return m_type;
}

metadata_t::record_field_value_t::record_field_value_t(int32_t p_type, kaitai::kstream* p__io, metadata_t::record_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = p_type;
    m_value = nullptr;
    _read();
}

void metadata_t::record_field_value_t::_read() {
    m_value = std::unique_ptr<data_value_t>(new data_value_t(type(), m__io, this, m__root));
}

metadata_t::record_field_value_t::~record_field_value_t() {
    _clean_up();
}

void metadata_t::record_field_value_t::_clean_up() {
}

metadata_t::storage_details_t::storage_details_t(uint32_t p_dimensionality, kaitai::kstream* p__io, metadata_t::column_spec_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_dimensionality = p_dimensionality;
    m_column_keyword_set = nullptr;
    m_column_name = nullptr;
    m_array_details = nullptr;
    _read();
}

void metadata_t::storage_details_t::_read() {
    m_version = m__io->read_u4be();
    n_column_keyword_set = true;
    if (version() == 1) {
        n_column_keyword_set = false;
        m_column_keyword_set = std::unique_ptr<table_record_t>(new table_record_t(m__io, this, m__root));
    }
    m_column_name = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_column_version = m__io->read_u4be();
    m_manager_number = m__io->read_u4be();
    n_array_details = true;
    if (dimensionality() > 0) {
        n_array_details = false;
        m_array_details = std::unique_ptr<array_column_storage_details_t>(new array_column_storage_details_t(m__io, this, m__root));
    }
    n_array_shape_in_column = true;
    if (dimensionality() < 0) {
        n_array_shape_in_column = false;
        m_array_shape_in_column = m__io->read_u1();
    }
}

metadata_t::storage_details_t::~storage_details_t() {
    _clean_up();
}

void metadata_t::storage_details_t::_clean_up() {
    if (!n_column_keyword_set) {
    }
    if (!n_array_details) {
    }
    if (!n_array_shape_in_column) {
    }
}

metadata_t::storage_desc_t::storage_desc_t(kaitai::kstream* p__io, metadata_t::column_spec_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_options = nullptr;
    m_managers = nullptr;
    _read();
}

void metadata_t::storage_desc_t::_read() {
    m_version = m__io->read_s4be();
    n_nrows = true;
    switch (version()) {
    case -1: {
        n_nrows = false;
        m_nrows = m__io->read_u4be();
        break;
    }
    case -2: {
        n_nrows = false;
        m_nrows = m__io->read_u4be();
        break;
    }
    case -3: {
        n_nrows = false;
        m_nrows = m__io->read_u8be();
        break;
    }
    }
    n_options = true;
    if (version() == -3) {
        n_options = false;
        m_options = std::unique_ptr<columnset_options_type_t>(new columnset_options_type_t(m__io, this, m__root));
    }
    m_sequence_number = m__io->read_u4be();
    m_n_managers = m__io->read_u4be();
    m_managers = std::unique_ptr<std::vector<std::unique_ptr<columnset_manager_t>>>(new std::vector<std::unique_ptr<columnset_manager_t>>());
    const int l_managers = n_managers();
    for (int i = 0; i < l_managers; i++) {
        m_managers->push_back(std::move(std::unique_ptr<columnset_manager_t>(new columnset_manager_t(m__io, this, m__root))));
    }
}

metadata_t::storage_desc_t::~storage_desc_t() {
    _clean_up();
}

void metadata_t::storage_desc_t::_clean_up() {
    if (!n_nrows) {
    }
    if (!n_options) {
    }
}

metadata_t::type_name_t::type_name_t(std::string p_value, kaitai::kstream* p__io, kaitai::kstruct* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_value = p_value;
    _read();
}

void metadata_t::type_name_t::_read() {
    m_size = m__io->read_u4be();
    m_name = kaitai::kstream::bytes_to_str(m__io->read_bytes(value().length()), std::string("ASCII"));
    if (!(name() == (value()))) {
        throw kaitai::validation_not_equal_error<std::string>(value(), name(), _io(), std::string("/types/type_name/seq/1"));
    }
}

metadata_t::type_name_t::~type_name_t() {
    _clean_up();
}

void metadata_t::type_name_t::_clean_up() {
}

metadata_t::column_details_t::column_details_t(kaitai::kstream* p__io, metadata_t::column_spec_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_cxx_type = nullptr;
    m_name = nullptr;
    m_comment = nullptr;
    m_manager_type = nullptr;
    m_manager_group = nullptr;
    m_shape = nullptr;
    m_keywords = nullptr;
    m_default = nullptr;
    _read();
}

void metadata_t::column_details_t::_read() {
    m_version = m__io->read_u4be();
    m_cxx_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_version_parent = m__io->read_u4be();
    m_name = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_comment = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_manager_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_manager_group = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_data_type = m__io->read_s4be();
    m_options = m__io->read_s4be();
    m_dimensions = m__io->read_s4be();
    m_max_length = m__io->read_s4be();
    n_shape = true;
    if (dimensions() != 0) {
        n_shape = false;
        m_shape = std::unique_ptr<iposition_t>(new iposition_t(m__io, this, m__root));
    }
    n_max_length_of_string = true;
    if (dimensions() != 0) {
        n_max_length_of_string = false;
        m_max_length_of_string = m__io->read_u4be();
    }
    m_keywords = std::unique_ptr<table_record_t>(new table_record_t(m__io, this, m__root));
    m_column_template_class_version = m__io->read_u4be();
    n_default = true;
    if ( ((dimensions() == 0) && (data_type() != 25)) ) {
        n_default = false;
        m_default = std::unique_ptr<default_t>(new default_t(data_type(), m__io, this, m__root));
    }
    n_dummy_flag = true;
    if ( ((dimensions() != 0) && (data_type() != 25)) ) {
        n_dummy_flag = false;
        m_dummy_flag = m__io->read_u1();
    }
}

metadata_t::column_details_t::~column_details_t() {
    _clean_up();
}

void metadata_t::column_details_t::_clean_up() {
    if (!n_shape) {
    }
    if (!n_max_length_of_string) {
    }
    if (!n_default) {
    }
    if (!n_dummy_flag) {
    }
}

metadata_t::columnset_manager_t::columnset_manager_t(kaitai::kstream* p__io, metadata_t::storage_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_cxx_type = nullptr;
    _read();
}

void metadata_t::columnset_manager_t::_read() {
    m_cxx_type = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_sequence_number = m__io->read_u4be();
}

metadata_t::columnset_manager_t::~columnset_manager_t() {
    _clean_up();
}

void metadata_t::columnset_manager_t::_clean_up() {
}

metadata_t::column_map_t::column_map_t(kaitai::kstream* p__io, metadata_t::reference_table_desc_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_key = nullptr;
    m_val = nullptr;
    _read();
}

void metadata_t::column_map_t::_read() {
    m_key = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
    m_val = std::unique_ptr<dtype_t::string_t>(new dtype_t::string_t(m__io, this, m__root));
}

metadata_t::column_map_t::~column_map_t() {
    _clean_up();
}

void metadata_t::column_map_t::_clean_up() {
}

metadata_t::record_desc_t::record_desc_t(kaitai::kstream* p__io, metadata_t::table_record_t* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = nullptr;
    m_fields = nullptr;
    m_values = nullptr;
    _read();
}

void metadata_t::record_desc_t::_read() {
    m_size = m__io->read_u4be();
    m_type = std::unique_ptr<type_name_t>(new type_name_t(std::string("RecordDesc"), m__io, this, m__root));
    m_version = m__io->read_u4be();
    m_n_fields = m__io->read_s4be();
    m_fields = std::unique_ptr<std::vector<std::unique_ptr<record_field_desc_t>>>(new std::vector<std::unique_ptr<record_field_desc_t>>());
    const int l_fields = n_fields();
    for (int i = 0; i < l_fields; i++) {
        m_fields->push_back(std::move(std::unique_ptr<record_field_desc_t>(new record_field_desc_t(m__io, this, m__root))));
    }
    m_record_type = m__io->read_s4be();
    m_values = std::unique_ptr<std::vector<std::unique_ptr<record_field_value_t>>>(new std::vector<std::unique_ptr<record_field_value_t>>());
    const int l_values = n_fields();
    for (int i = 0; i < l_values; i++) {
        m_values->push_back(std::move(std::unique_ptr<record_field_value_t>(new record_field_value_t(fields()->at(i)->type(), m__io, this, m__root))));
    }
}

metadata_t::record_desc_t::~record_desc_t() {
    _clean_up();
}

void metadata_t::record_desc_t::_clean_up() {
}

metadata_t::table_record_t::table_record_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, metadata_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    m_type = nullptr;
    m_desc = nullptr;
    _read();
}

void metadata_t::table_record_t::_read() {
    m_size = m__io->read_u4be();
    m_type = std::unique_ptr<type_name_t>(new type_name_t(std::string("TableRecord"), m__io, this, m__root));
    m_version = m__io->read_u4be();
    m_desc = std::unique_ptr<record_desc_t>(new record_desc_t(m__io, this, m__root));
}

metadata_t::table_record_t::~table_record_t() {
    _clean_up();
}

void metadata_t::table_record_t::_clean_up() {
}
