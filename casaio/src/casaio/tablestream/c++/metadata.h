#pragma once

// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

#include "kaitai/kaitaistruct.h"
#include <stdint.h>
#include <memory>
#include <vector>

#if KAITAI_STRUCT_VERSION < 9000L
#error "Incompatible Kaitai Struct C++/STL API: version 0.9 or later is required"
#endif

/**
 * The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
 * oriented storage system for radio astronoy data. Many systems use it to store, manipulate and process
 * the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
 * from the telescopes and the images that are produced as a final product. This file parses only the
 * table description stored in the table.dat file within the table directory.
 */

class metadata_t : public kaitai::kstruct {

public:
    class array_column_storage_details_t;
    class data_value_t;
    class reference_table_desc_t;
    class iposition_t;
    class columnset_options_type_t;
    class subrecord_desc_t;
    class column_row_details_64b_t;
    class table_desc_t;
    class column_spec_t;
    class record_field_desc_t;
    class array_t;
    class hacky_t;
    class column_row_details_32b_t;
    class default_t;
    class regular_table_desc_t;
    class record_field_value_t;
    class storage_details_t;
    class storage_desc_t;
    class type_name_t;
    class column_details_t;
    class columnset_manager_t;
    class column_map_t;
    class record_desc_t;
    class table_record_t;

    metadata_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, metadata_t* p__root = nullptr);

private:
    void _read();
    void _clean_up();

public:
    ~metadata_t();

    class array_column_storage_details_t : public kaitai::kstruct {

    public:

        array_column_storage_details_t(kaitai::kstream* p__io, metadata_t::storage_details_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~array_column_storage_details_t();

    private:
        uint8_t m_shape_column_definition;
        uint32_t m_filler;
        bool n_filler;

    public:
        bool _is_null_filler() { filler(); return n_filler; };

    private:
        std::unique_ptr<iposition_t> m_shape;
        bool n_shape;

    public:
        bool _is_null_shape() { shape(); return n_shape; };

    private:
        metadata_t* m__root;
        metadata_t::storage_details_t* m__parent;

    public:
        uint8_t shape_column_definition() const { return m_shape_column_definition; }
        uint32_t filler() const { return m_filler; }
        iposition_t* shape() const { return m_shape.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::storage_details_t* _parent() const { return m__parent; }
    };

    class data_value_t : public kaitai::kstruct {

    public:

        data_value_t(uint16_t p_type, kaitai::kstream* p__io, metadata_t::record_field_value_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~data_value_t();

    private:
        std::unique_ptr<kaitai::kstruct> m_value;
        uint16_t m_type;
        metadata_t* m__root;
        metadata_t::record_field_value_t* m__parent;

    public:
        kaitai::kstruct* value() const { return m_value.get(); }
        uint16_t type() const { return m_type; }
        metadata_t* _root() const { return m__root; }
        metadata_t::record_field_value_t* _parent() const { return m__parent; }
    };

    class reference_table_desc_t : public kaitai::kstruct {

    public:

        reference_table_desc_t(uint32_t p_version, kaitai::kstream* p__io, metadata_t::table_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~reference_table_desc_t();

    private:
        bool f_type;
        int8_t m_type;

    public:
        int8_t type();

    private:
        uint32_t m_column_map_size;
        std::unique_ptr<type_name_t> m_column_map_type;
        uint32_t m_column_map_version;
        uint32_t m_default_value;
        uint32_t m_n_column_maps;
        uint32_t m_block_allocation_increment;
        std::unique_ptr<std::vector<std::unique_ptr<column_map_t>>> m_column_maps;
        uint32_t m_column_order_size;
        std::unique_ptr<type_name_t> m_column_order_type;
        uint32_t m_column_order_version;
        uint32_t m_n_column_order_shape;
        std::unique_ptr<std::vector<uint32_t>> m_column_order_shape;
        uint32_t m_n_column_order;
        std::unique_ptr<std::vector<std::unique_ptr<dtype_t::string_t>>> m_column_order;
        std::unique_ptr<kaitai::kstruct> m_row_order;
        bool n_row_order;

    public:
        bool _is_null_row_order() { row_order(); return n_row_order; };

    private:
        uint32_t m_version;
        metadata_t* m__root;
        metadata_t::table_desc_t* m__parent;

    public:
        uint32_t column_map_size() const { return m_column_map_size; }
        type_name_t* column_map_type() const { return m_column_map_type.get(); }
        uint32_t column_map_version() const { return m_column_map_version; }
        uint32_t default_value() const { return m_default_value; }
        uint32_t n_column_maps() const { return m_n_column_maps; }
        uint32_t block_allocation_increment() const { return m_block_allocation_increment; }
        std::vector<std::unique_ptr<column_map_t>>* column_maps() const { return m_column_maps.get(); }
        uint32_t column_order_size() const { return m_column_order_size; }
        type_name_t* column_order_type() const { return m_column_order_type.get(); }
        uint32_t column_order_version() const { return m_column_order_version; }
        uint32_t n_column_order_shape() const { return m_n_column_order_shape; }
        std::vector<uint32_t>* column_order_shape() const { return m_column_order_shape.get(); }
        uint32_t n_column_order() const { return m_n_column_order; }
        std::vector<std::unique_ptr<dtype_t::string_t>>* column_order() const { return m_column_order.get(); }
        kaitai::kstruct* row_order() const { return m_row_order.get(); }
        uint32_t version() const { return m_version; }
        metadata_t* _root() const { return m__root; }
        metadata_t::table_desc_t* _parent() const { return m__parent; }
    };

    class iposition_t : public kaitai::kstruct {

    public:

        iposition_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~iposition_t();

    private:
        std::unique_ptr<dtype_t::string_t> m_type;
        uint32_t m_version;
        uint32_t m_n_elements;
        std::unique_ptr<std::vector<uint64_t>> m_elements;
        metadata_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        dtype_t::string_t* type() const { return m_type.get(); }

        /**
         * 1 implies 4 byte shape numbers but 2 implies 8 byte shape numbers
         */
        uint32_t version() const { return m_version; }
        uint32_t n_elements() const { return m_n_elements; }
        std::vector<uint64_t>* elements() const { return m_elements.get(); }
        metadata_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class columnset_options_type_t : public kaitai::kstruct {

    public:

        columnset_options_type_t(kaitai::kstream* p__io, metadata_t::storage_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~columnset_options_type_t();

    private:
        int32_t m_value;
        uint32_t m_block_size;
        metadata_t* m__root;
        metadata_t::storage_desc_t* m__parent;

    public:
        int32_t value() const { return m_value; }
        uint32_t block_size() const { return m_block_size; }
        metadata_t* _root() const { return m__root; }
        metadata_t::storage_desc_t* _parent() const { return m__parent; }
    };

    class subrecord_desc_t : public kaitai::kstruct {

    public:

        subrecord_desc_t(kaitai::kstream* p__io, metadata_t::record_field_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~subrecord_desc_t();

    private:
        uint32_t m_size;
        std::unique_ptr<type_name_t> m_type;
        uint32_t m_version;
        int32_t m_n_fields;
        std::unique_ptr<dtype_t::string_t> m_comment;
        metadata_t* m__root;
        metadata_t::record_field_desc_t* m__parent;

    public:
        uint32_t size() const { return m_size; }
        type_name_t* type() const { return m_type.get(); }
        uint32_t version() const { return m_version; }
        int32_t n_fields() const { return m_n_fields; }
        dtype_t::string_t* comment() const { return m_comment.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::record_field_desc_t* _parent() const { return m__parent; }
    };

    class column_row_details_64b_t : public kaitai::kstruct {

    public:

        column_row_details_64b_t(kaitai::kstream* p__io, metadata_t::reference_table_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~column_row_details_64b_t();

    private:
        uint64_t m_num_maps_base;
        uint8_t m_has_row_order;
        uint64_t m_num_maps;
        std::unique_ptr<std::vector<uint32_t>> m_maps;
        metadata_t* m__root;
        metadata_t::reference_table_desc_t* m__parent;

    public:
        uint64_t num_maps_base() const { return m_num_maps_base; }
        uint8_t has_row_order() const { return m_has_row_order; }
        uint64_t num_maps() const { return m_num_maps; }
        std::vector<uint32_t>* maps() const { return m_maps.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::reference_table_desc_t* _parent() const { return m__parent; }
    };

    class table_desc_t : public kaitai::kstruct {

    public:

        table_desc_t(kaitai::kstream* p__io, metadata_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~table_desc_t();

    private:
        uint32_t m_size;
        std::unique_ptr<dtype_t::string_t> m_type;
        uint32_t m_version;
        std::unique_ptr<dtype_t::string_t> m_name;
        std::unique_ptr<kaitai::kstruct> m_table;
        bool n_table;

    public:
        bool _is_null_table() { table(); return n_table; };

    private:
        metadata_t* m__root;
        metadata_t* m__parent;

    public:
        uint32_t size() const { return m_size; }
        dtype_t::string_t* type() const { return m_type.get(); }
        uint32_t version() const { return m_version; }
        dtype_t::string_t* name() const { return m_name.get(); }
        kaitai::kstruct* table() const { return m_table.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t* _parent() const { return m__parent; }
    };

    class column_spec_t : public kaitai::kstruct {

    public:

        column_spec_t(kaitai::kstream* p__io, metadata_t::regular_table_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~column_spec_t();

    private:
        uint32_t m_n_cols;
        std::unique_ptr<std::vector<std::unique_ptr<column_details_t>>> m_details;
        std::unique_ptr<storage_desc_t> m_storage;
        std::unique_ptr<std::vector<std::unique_ptr<storage_details_t>>> m_storage_details;
        uint32_t m_n_data_manager_info;
        std::unique_ptr<std::vector<uint8_t>> m_data_manager_info;
        metadata_t* m__root;
        metadata_t::regular_table_desc_t* m__parent;

    public:
        uint32_t n_cols() const { return m_n_cols; }
        std::vector<std::unique_ptr<column_details_t>>* details() const { return m_details.get(); }
        storage_desc_t* storage() const { return m_storage.get(); }
        std::vector<std::unique_ptr<storage_details_t>>* storage_details() const { return m_storage_details.get(); }
        uint32_t n_data_manager_info() const { return m_n_data_manager_info; }
        std::vector<uint8_t>* data_manager_info() const { return m_data_manager_info.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::regular_table_desc_t* _parent() const { return m__parent; }
    };

    class record_field_desc_t : public kaitai::kstruct {

    public:

        record_field_desc_t(kaitai::kstream* p__io, metadata_t::record_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~record_field_desc_t();

    private:
        std::unique_ptr<dtype_t::string_t> m_name;
        int32_t m_type;
        uint32_t m_subtable_filler;
        bool n_subtable_filler;

    public:
        bool _is_null_subtable_filler() { subtable_filler(); return n_subtable_filler; };

    private:
        uint32_t m_string_array_filler_size;
        bool n_string_array_filler_size;

    public:
        bool _is_null_string_array_filler_size() { string_array_filler_size(); return n_string_array_filler_size; };

    private:
        std::unique_ptr<iposition_t> m_string_array_filler_iposition;
        bool n_string_array_filler_iposition;

    public:
        bool _is_null_string_array_filler_iposition() { string_array_filler_iposition(); return n_string_array_filler_iposition; };

    private:
        std::unique_ptr<dtype_t::string_t> m_comment;
        bool n_comment;

    public:
        bool _is_null_comment() { comment(); return n_comment; };

    private:
        std::unique_ptr<subrecord_desc_t> m_subrecord;
        bool n_subrecord;

    public:
        bool _is_null_subrecord() { subrecord(); return n_subrecord; };

    private:
        metadata_t* m__root;
        metadata_t::record_desc_t* m__parent;

    public:
        dtype_t::string_t* name() const { return m_name.get(); }
        int32_t type() const { return m_type; }
        uint32_t subtable_filler() const { return m_subtable_filler; }
        uint32_t string_array_filler_size() const { return m_string_array_filler_size; }
        iposition_t* string_array_filler_iposition() const { return m_string_array_filler_iposition.get(); }
        dtype_t::string_t* comment() const { return m_comment.get(); }
        subrecord_desc_t* subrecord() const { return m_subrecord.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::record_desc_t* _parent() const { return m__parent; }
    };

    class array_t : public kaitai::kstruct {

    public:

        array_t(uint16_t p_type, kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~array_t();

    private:
        uint32_t m_size;
        std::unique_ptr<dtype_t::string_t> m_cxx_type;
        uint32_t m_version;
        uint32_t m_n_shape;
        std::unique_ptr<std::vector<uint32_t>> m_shape;
        uint32_t m_n_elements;
        std::unique_ptr<std::vector<std::unique_ptr<kaitai::kstruct>>> m_elements;
        uint16_t m_type;
        metadata_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint32_t size() const { return m_size; }
        dtype_t::string_t* cxx_type() const { return m_cxx_type.get(); }
        uint32_t version() const { return m_version; }
        uint32_t n_shape() const { return m_n_shape; }
        std::vector<uint32_t>* shape() const { return m_shape.get(); }
        uint32_t n_elements() const { return m_n_elements; }
        std::vector<std::unique_ptr<kaitai::kstruct>>* elements() const { return m_elements.get(); }
        uint16_t type() const { return m_type; }
        metadata_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class hacky_t : public kaitai::kstruct {

    public:

        hacky_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~hacky_t();

    private:
        uint32_t m_size;
        std::unique_ptr<dtype_t::string_t> m_type;
        metadata_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint32_t size() const { return m_size; }
        dtype_t::string_t* type() const { return m_type.get(); }
        metadata_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class column_row_details_32b_t : public kaitai::kstruct {

    public:

        column_row_details_32b_t(kaitai::kstream* p__io, metadata_t::reference_table_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~column_row_details_32b_t();

    private:
        uint32_t m_n_maps_base;
        uint8_t m_has_row_order;
        uint32_t m_n_maps;
        std::unique_ptr<std::vector<uint32_t>> m_maps;
        metadata_t* m__root;
        metadata_t::reference_table_desc_t* m__parent;

    public:
        uint32_t n_maps_base() const { return m_n_maps_base; }
        uint8_t has_row_order() const { return m_has_row_order; }
        uint32_t n_maps() const { return m_n_maps; }
        std::vector<uint32_t>* maps() const { return m_maps.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::reference_table_desc_t* _parent() const { return m__parent; }
    };

    class default_t : public kaitai::kstruct {

    public:

        default_t(uint16_t p_type, kaitai::kstream* p__io, metadata_t::column_details_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~default_t();

    private:
        std::unique_ptr<kaitai::kstruct> m_value;
        uint16_t m_type;
        metadata_t* m__root;
        metadata_t::column_details_t* m__parent;

    public:
        kaitai::kstruct* value() const { return m_value.get(); }
        uint16_t type() const { return m_type; }
        metadata_t* _root() const { return m__root; }
        metadata_t::column_details_t* _parent() const { return m__parent; }
    };

    class regular_table_desc_t : public kaitai::kstruct {

    public:

        regular_table_desc_t(kaitai::kstream* p__io, metadata_t::table_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~regular_table_desc_t();

    private:
        bool f_type;
        int8_t m_type;

    public:
        int8_t type();

    private:
        std::unique_ptr<dtype_t::string_t> m_desc_version;
        std::unique_ptr<dtype_t::string_t> m_comment;
        std::unique_ptr<table_record_t> m_user_keywords;
        std::unique_ptr<table_record_t> m_private_keywords;
        std::unique_ptr<column_spec_t> m_columns;
        metadata_t* m__root;
        metadata_t::table_desc_t* m__parent;

    public:
        dtype_t::string_t* desc_version() const { return m_desc_version.get(); }
        dtype_t::string_t* comment() const { return m_comment.get(); }
        table_record_t* user_keywords() const { return m_user_keywords.get(); }
        table_record_t* private_keywords() const { return m_private_keywords.get(); }
        column_spec_t* columns() const { return m_columns.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::table_desc_t* _parent() const { return m__parent; }
    };

    class record_field_value_t : public kaitai::kstruct {

    public:

        record_field_value_t(int32_t p_type, kaitai::kstream* p__io, metadata_t::record_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~record_field_value_t();

    private:
        std::unique_ptr<data_value_t> m_value;
        int32_t m_type;
        metadata_t* m__root;
        metadata_t::record_desc_t* m__parent;

    public:
        data_value_t* value() const { return m_value.get(); }
        int32_t type() const { return m_type; }
        metadata_t* _root() const { return m__root; }
        metadata_t::record_desc_t* _parent() const { return m__parent; }
    };

    class storage_details_t : public kaitai::kstruct {

    public:

        storage_details_t(uint32_t p_dimensionality, kaitai::kstream* p__io, metadata_t::column_spec_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~storage_details_t();

    private:
        uint32_t m_version;
        std::unique_ptr<table_record_t> m_column_keyword_set;
        bool n_column_keyword_set;

    public:
        bool _is_null_column_keyword_set() { column_keyword_set(); return n_column_keyword_set; };

    private:
        std::unique_ptr<dtype_t::string_t> m_column_name;
        uint32_t m_column_version;
        uint32_t m_manager_number;
        std::unique_ptr<array_column_storage_details_t> m_array_details;
        bool n_array_details;

    public:
        bool _is_null_array_details() { array_details(); return n_array_details; };

    private:
        uint8_t m_array_shape_in_column;
        bool n_array_shape_in_column;

    public:
        bool _is_null_array_shape_in_column() { array_shape_in_column(); return n_array_shape_in_column; };

    private:
        uint32_t m_dimensionality;
        metadata_t* m__root;
        metadata_t::column_spec_t* m__parent;

    public:
        uint32_t version() const { return m_version; }
        table_record_t* column_keyword_set() const { return m_column_keyword_set.get(); }
        dtype_t::string_t* column_name() const { return m_column_name.get(); }

        /**
         * casacore::ScalarColumnData<unsigned char>::putFileDerived
         */
        uint32_t column_version() const { return m_column_version; }

        /**
         * casacore::ScalarColumnData<unsigned char>::putFileDerived
         */
        uint32_t manager_number() const { return m_manager_number; }
        array_column_storage_details_t* array_details() const { return m_array_details.get(); }

        /**
         * encountered with refim_point_withline.ms/SOURCE/table.dat
         */
        uint8_t array_shape_in_column() const { return m_array_shape_in_column; }
        uint32_t dimensionality() const { return m_dimensionality; }
        metadata_t* _root() const { return m__root; }
        metadata_t::column_spec_t* _parent() const { return m__parent; }
    };

    class storage_desc_t : public kaitai::kstruct {

    public:

        storage_desc_t(kaitai::kstream* p__io, metadata_t::column_spec_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~storage_desc_t();

    private:
        int32_t m_version;
        uint64_t m_nrows;
        bool n_nrows;

    public:
        bool _is_null_nrows() { nrows(); return n_nrows; };

    private:
        std::unique_ptr<columnset_options_type_t> m_options;
        bool n_options;

    public:
        bool _is_null_options() { options(); return n_options; };

    private:
        uint32_t m_sequence_number;
        uint32_t m_n_managers;
        std::unique_ptr<std::vector<std::unique_ptr<columnset_manager_t>>> m_managers;
        metadata_t* m__root;
        metadata_t::column_spec_t* m__parent;

    public:

        /**
         * Version was not output for version == 1, so there may be problems for very old tables. Per the docs, in early
         * versions the Version number was not written and instead the number of rows was first. Later it was added and
         * written as a negative number.
         */
        int32_t version() const { return m_version; }
        uint64_t nrows() const { return m_nrows; }
        columnset_options_type_t* options() const { return m_options.get(); }

        /**
         * Highest datamanager sequence used.
         */
        uint32_t sequence_number() const { return m_sequence_number; }
        uint32_t n_managers() const { return m_n_managers; }
        std::vector<std::unique_ptr<columnset_manager_t>>* managers() const { return m_managers.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::column_spec_t* _parent() const { return m__parent; }
    };

    class type_name_t : public kaitai::kstruct {

    public:

        type_name_t(std::string p_value, kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~type_name_t();

    private:
        uint32_t m_size;
        std::string m_name;
        std::string m_value;
        metadata_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint32_t size() const { return m_size; }
        std::string name() const { return m_name; }
        std::string value() const { return m_value; }
        metadata_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class column_details_t : public kaitai::kstruct {

    public:

        column_details_t(kaitai::kstream* p__io, metadata_t::column_spec_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~column_details_t();

    private:
        uint32_t m_version;
        std::unique_ptr<dtype_t::string_t> m_cxx_type;
        uint32_t m_version_parent;
        std::unique_ptr<dtype_t::string_t> m_name;
        std::unique_ptr<dtype_t::string_t> m_comment;
        std::unique_ptr<dtype_t::string_t> m_manager_type;
        std::unique_ptr<dtype_t::string_t> m_manager_group;
        int32_t m_data_type;
        int32_t m_options;
        int32_t m_dimensions;
        int32_t m_max_length;
        std::unique_ptr<iposition_t> m_shape;
        bool n_shape;

    public:
        bool _is_null_shape() { shape(); return n_shape; };

    private:
        uint32_t m_max_length_of_string;
        bool n_max_length_of_string;

    public:
        bool _is_null_max_length_of_string() { max_length_of_string(); return n_max_length_of_string; };

    private:
        std::unique_ptr<table_record_t> m_keywords;
        uint32_t m_column_template_class_version;
        std::unique_ptr<default_t> m_default;
        bool n_default;

    public:
        bool _is_null_default() { default(); return n_default; };

    private:
        uint8_t m_dummy_flag;
        bool n_dummy_flag;

    public:
        bool _is_null_dummy_flag() { dummy_flag(); return n_dummy_flag; };

    private:
        metadata_t* m__root;
        metadata_t::column_spec_t* m__parent;

    public:
        uint32_t version() const { return m_version; }
        dtype_t::string_t* cxx_type() const { return m_cxx_type.get(); }
        uint32_t version_parent() const { return m_version_parent; }
        dtype_t::string_t* name() const { return m_name.get(); }
        dtype_t::string_t* comment() const { return m_comment.get(); }
        dtype_t::string_t* manager_type() const { return m_manager_type.get(); }
        dtype_t::string_t* manager_group() const { return m_manager_group.get(); }
        int32_t data_type() const { return m_data_type; }
        int32_t options() const { return m_options; }

        /**
         * MAY HAVE SHAPE NEXT to be done
         */
        int32_t dimensions() const { return m_dimensions; }
        int32_t max_length() const { return m_max_length; }
        iposition_t* shape() const { return m_shape.get(); }
        uint32_t max_length_of_string() const { return m_max_length_of_string; }
        table_record_t* keywords() const { return m_keywords.get(); }

        /**
         * e.g. ScalarColumnDesc<T> putDesc, ScaColDesc.tcc line 149
         */
        uint32_t column_template_class_version() const { return m_column_template_class_version; }
        default_t* default() const { return m_default.get(); }
        uint8_t dummy_flag() const { return m_dummy_flag; }
        metadata_t* _root() const { return m__root; }
        metadata_t::column_spec_t* _parent() const { return m__parent; }
    };

    class columnset_manager_t : public kaitai::kstruct {

    public:

        columnset_manager_t(kaitai::kstream* p__io, metadata_t::storage_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~columnset_manager_t();

    private:
        std::unique_ptr<dtype_t::string_t> m_cxx_type;
        uint32_t m_sequence_number;
        metadata_t* m__root;
        metadata_t::storage_desc_t* m__parent;

    public:
        dtype_t::string_t* cxx_type() const { return m_cxx_type.get(); }
        uint32_t sequence_number() const { return m_sequence_number; }
        metadata_t* _root() const { return m__root; }
        metadata_t::storage_desc_t* _parent() const { return m__parent; }
    };

    class column_map_t : public kaitai::kstruct {

    public:

        column_map_t(kaitai::kstream* p__io, metadata_t::reference_table_desc_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~column_map_t();

    private:
        std::unique_ptr<dtype_t::string_t> m_key;
        std::unique_ptr<dtype_t::string_t> m_val;
        metadata_t* m__root;
        metadata_t::reference_table_desc_t* m__parent;

    public:
        dtype_t::string_t* key() const { return m_key.get(); }
        dtype_t::string_t* val() const { return m_val.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::reference_table_desc_t* _parent() const { return m__parent; }
    };

    class record_desc_t : public kaitai::kstruct {

    public:

        record_desc_t(kaitai::kstream* p__io, metadata_t::table_record_t* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~record_desc_t();

    private:
        uint32_t m_size;
        std::unique_ptr<type_name_t> m_type;
        uint32_t m_version;
        int32_t m_n_fields;
        std::unique_ptr<std::vector<std::unique_ptr<record_field_desc_t>>> m_fields;
        int32_t m_record_type;
        std::unique_ptr<std::vector<std::unique_ptr<record_field_value_t>>> m_values;
        metadata_t* m__root;
        metadata_t::table_record_t* m__parent;

    public:
        uint32_t size() const { return m_size; }
        type_name_t* type() const { return m_type.get(); }
        uint32_t version() const { return m_version; }
        int32_t n_fields() const { return m_n_fields; }
        std::vector<std::unique_ptr<record_field_desc_t>>* fields() const { return m_fields.get(); }
        int32_t record_type() const { return m_record_type; }
        std::vector<std::unique_ptr<record_field_value_t>>* values() const { return m_values.get(); }
        metadata_t* _root() const { return m__root; }
        metadata_t::table_record_t* _parent() const { return m__parent; }
    };

    class table_record_t : public kaitai::kstruct {

    public:

        table_record_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, metadata_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~table_record_t();

    private:
        uint32_t m_size;
        std::unique_ptr<type_name_t> m_type;
        uint32_t m_version;
        std::unique_ptr<record_desc_t> m_desc;
        metadata_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint32_t size() const { return m_size; }
        type_name_t* type() const { return m_type.get(); }
        uint32_t version() const { return m_version; }
        record_desc_t* desc() const { return m_desc.get(); }
        metadata_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

private:
    std::string m_magic;
    uint32_t m_size;
    std::unique_ptr<dtype_t::string_t> m_type;
    uint32_t m_version;
    uint64_t m_nrows;
    bool n_nrows;

public:
    bool _is_null_nrows() { nrows(); return n_nrows; };

private:
    uint32_t m_little_endian;
    std::unique_ptr<dtype_t::string_t> m_name;
    std::unique_ptr<table_desc_t> m_desc;
    metadata_t* m__root;
    kaitai::kstruct* m__parent;

public:

    /**
     * casa magic unsigned int 3200171710  190 190 190 190
     */
    std::string magic() const { return m_magic; }
    uint32_t size() const { return m_size; }
    dtype_t::string_t* type() const { return m_type.get(); }
    uint32_t version() const { return m_version; }
    uint64_t nrows() const { return m_nrows; }
    uint32_t little_endian() const { return m_little_endian; }

    /**
     * expect "PlainTable"
     */
    dtype_t::string_t* name() const { return m_name.get(); }

    /**
     * TableDesc
     */
    table_desc_t* desc() const { return m_desc.get(); }
    metadata_t* _root() const { return m__root; }
    kaitai::kstruct* _parent() const { return m__parent; }
};
