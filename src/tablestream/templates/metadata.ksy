# Copyright (C) 2022
# Associated Universities, Inc. Washington DC, USA.
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Library General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Library General Public
# License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 675 Massachusetts Ave, Cambridge, MA 02139, USA.
#
###
### casacore data types:
### --------------------------------------------------------------------------------------
###   0           TpBool
###   1           TpChar
###   2           TpUChar
###   3           TpShort
###   4           TpUShort
###   5           TpInt
###   6           TpUInt
###   7           TpFloat
###   8           TpDouble
###   9           TpComplex
###   10          TpDComplex
###   11          TpString
###   12          TpTable
###   13          TpArrayBool
###   14          TpArrayChar
###   15          TpArrayUChar
###   16          TpArrayShort
###   17          TpArrayUShort
###   18          TpArrayInt
###   19          TpArrayUInt
###   20          TpArrayFloat
###   21          TpArrayDouble
###   22          TpArrayComplex
###   23          TpArrayDComplex
###   24          TpArrayString
###   25          TpRecord
###   26          TpOther
###   27          TpQuantity
###   28          TpArrayQuantity
###   29          TpInt64
###   30          TpArrayInt64
###



meta:
    id: metadata
    title: Casacore Table Data System header layout
    application:
      - casacore
      - AIPS++
      - CASA
    file-extension: dat
    tags:
      - scientific
      - astronomy
    license: LGPL-2.0-or-later
    ks-version: 0.10
    endian: be
    imports: dtype


doc: |
  The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
  oriented storage system for radio astronoy data. Many systems use it to store, manipulate and process
  the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
  from the telescopes and the images that are produced as a final product. This file parses only the
  table description stored in the table.dat file within the table directory.

seq:
    - id: magic
      contents: [ 0xbe, 0xbe, 0xbe, 0xbe ]
      doc: |
        casa magic unsigned int 3200171710  190 190 190 190
    - id: size
      type: u4
    - id: type
      type: dtype::string
    - id: version
      type: u4
    - id: nrows
      type:
          switch-on: version
          cases:
            1: u4
            2: u4
            3: u8
    - id: little_endian
      type: u4
    - id: name
      type: dtype::string
      doc: |
        expect "PlainTable"
    - id: desc
      type: table_desc
      doc: |
        TableDesc

types:
    array:
        params:
          - id: type
            type: u2
        seq:
          - id: size
            type: u4
          - id: cxx_type
            type: dtype::string
          - id: version
            type: u4
          - id: n_shape
            type: u4
          - id: shape
            type: u4
            repeat: expr
            repeat-expr: n_shape
          - id: n_elements
            type: u4
          - id: elements
            repeat: expr
            repeat-expr: n_elements
            type:
                switch-on: type
                cases:
                  13: dtype::uint1
                  14: dtype::int1
                  15: dtype::uint1
                  16: dtype::int2
                  17: dtype::uint2
                  18: dtype::int4
                  19: dtype::uint4
                  20: dtype::float4
                  21: dtype::float8
                  22: dtype::complex8
                  23: dtype::complex16
                  24: dtype::string
                  30: dtype::int8

    default:
        params:
          - id: type
            type: u2
        seq:
          - id: value
            type:
                switch-on: type
                cases:
                  0:  dtype::uint1
                  1:  dtype::int1
                  2:  dtype::uint1
                  3:  dtype::int2
                  4:  dtype::uint2
                  5:  dtype::int4
                  6:  dtype::uint4
                  7:  dtype::float4
                  8:  dtype::float8
                  9:  dtype::complex8
                  10: dtype::complex16
                  11: dtype::string
                  29: dtype::int8
                  _: array(type)

    data_value:
        params:
          - id: type
            type: u2
        seq:
          - id: value
            type:
                switch-on: type
                cases:
                  0:  dtype::uint1
                  1:  dtype::int1
                  2:  dtype::uint1
                  3:  dtype::int2
                  4:  dtype::uint2
                  5:  dtype::int4
                  6:  dtype::uint4
                  7:  dtype::float4
                  8:  dtype::float8
                  9:  dtype::complex8
                  10: dtype::complex16
                  11: dtype::string
                  12: dtype::string
                  25: table_record
                  29: dtype::int8
                  _: array(type)

    type_name:
        params:
          - id: value
            type: str
        seq:
          - id: size
            type: u4
          - id: name
            size: value.length # `str.length` gives the number of *characters*, not bytes as we would need here; but in ASCII they're equal
            type: str
            encoding: ASCII
            valid:
              eq: value
    record_field_desc:
        seq:
          - id: name
            type: dtype::string
          - id: type
            type: s4
          - id: subtable_filler
            type: u4
            if: type == 12
          - id: string_array_filler_size
            type: u4
            if: type == 24
          - id: string_array_filler_iposition   # for some reason this is always IPosition( 1, -1 ), single dim containing -1
            type: iposition
            if: type == 24
          - id: comment
            type: dtype::string
            if: type != 25
          - id: subrecord
            type: subrecord_desc
            if: type == 25
    record_field_value:
        params:
          - id: type
            type: s4
        seq:
          - id: value
            type: data_value(type)

    hacky:
        seq:
          - id: size
            type: u4
          - id: type
            type: dtype::string

    subrecord_desc:
        seq:
          - id: size
            type: u4
          - id: type
            type: type_name("RecordDesc")
          - id: version
            type: u4
          - id: n_fields
            type: s4
          - id: comment
            type: dtype::string

    record_desc:
        seq:
          - id: size
            type: u4
          - id: type
            type: type_name("RecordDesc")
          - id: version
            type: u4
          - id: n_fields
            type: s4
          - id: fields
            type: record_field_desc
            repeat: expr
            repeat-expr: n_fields
          - id: record_type
            type: s4
          - id: values
            type: record_field_value(fields[_index].type)
            repeat: expr
            repeat-expr: n_fields

    iposition:
        seq:
          - id: type
            type: dtype::string
          - id: version
            doc: |
              1 implies 4 byte shape numbers but 2 implies 8 byte shape numbers
            type: u4
          - id: n_elements
            type: u4
          - id: elements
            type:
                switch-on: version
                cases:
                  1: u4
                  2: u8
            repeat: expr
            repeat-expr: n_elements

    table_record:
        seq:
          - id: size
            type: u4
          - id: type
            type: type_name("TableRecord")
          - id: version
            type: u4
          - id: desc
            type: record_desc
    column_details:
        seq:
          - id: version
            type: u4
          - id: cxx_type
            type: dtype::string
          - id: version_parent
            type: u4
          - id: name
            type: dtype::string
          - id: comment
            type: dtype::string
          - id: manager_type
            type: dtype::string
          - id: manager_group
            type: dtype::string
          - id: data_type
            type: s4
          - id: options
            type: s4
          - id: dimensions
            type: s4
            doc: |
              MAY HAVE SHAPE NEXT to be done
          - id: max_length
            type: s4
          - id: shape
            type: iposition
            if: dimensions != 0
          - id: max_length_of_string
            type: u4
            if: dimensions != 0
          - id: keywords
            type: table_record
          - id: column_template_class_version
            doc: |
              e.g. ScalarColumnDesc<T> putDesc, ScaColDesc.tcc line 149
            type: u4
          - id: default # ArrayColumnDesc; docs are switched I think
            type: default(data_type)
            if: dimensions == 0 and data_type != 25
          - id: dummy_flag # ScalarColumnDesc; docs are switched I think
            type: u1
            if: dimensions != 0 and data_type != 25

    table_desc:
        seq:
          - id: size
            type: u4
          - id: type
            type: dtype::string
          - id: version
            type: u4
          - id: name
            type: dtype::string
          - id: table
            type:
                ###
                ### there seems to be no enum that can be used to distinguish
                ### reference tables from regular tables
                ###
                switch-on: type.value
                cases:
                    '"TableDesc"': regular_table_desc
                    '"RefTable"': reference_table_desc(version)

    ###
    ### column mapping found in reference table
    ###
    column_map:
        seq:
          - id: key
            type: dtype::string
          - id: val
            type: dtype::string

    ###
    ### details for tables with 32bit row specs
    ###
    column_row_details_32b:
        seq:
          - id: n_maps_base
            type: u4
          - id: has_row_order
            type: u1
          - id: n_maps
            type: u4
          - id: maps
            type: u4
            repeat: expr
            repeat-expr: n_maps

    ###
    ### details for tables with 64bit row specs
    ###
    column_row_details_64b:
        seq:
          - id: num_maps_base
            type: u8
          - id: has_row_order
            type: u1
          - id: num_maps
            type: u8
          - id: maps
            type: u4
            repeat: expr
            repeat-expr: num_maps

    ###
    ### reference table description
    ###
    reference_table_desc:
        params:
          - id: version
            type: u4
        seq:
          - id: column_map_size
            type: u4
          - id: column_map_type
            type: type_name("SimpleOrderedMap")
          - id: column_map_version
            type: u4
          - id: default_value
            type: u4
          - id: n_column_maps
            type: u4
          - id: block_allocation_increment
            type: u4
          - id: column_maps
            type: column_map
            repeat: expr
            repeat-expr: n_column_maps
          - id: column_order_size
            type: u4
          - id: column_order_type
            type: type_name("Array")
          - id: column_order_version
            type: u4
          - id: n_column_order_shape
            type: u4
          - id: column_order_shape
            type: u4
            repeat: expr
            repeat-expr: n_column_order_shape
          - id: n_column_order
            type: u4
          - id: column_order
            type: dtype::string
            repeat: expr
            repeat-expr: n_column_order
          - id: row_order
            type:
                switch-on: version
                cases:
                    2: column_row_details_32b
                    1: column_row_details_64b
        instances:
          type:
            value: 2

    ###
    ### standard table description
    ###
    regular_table_desc:
        seq:
          - id: desc_version
            type: dtype::string
          - id: comment
            type: dtype::string
          - id: user_keywords
            type: table_record
          - id: private_keywords
            type: table_record
          - id: columns
            type: column_spec
        instances:
          type:
            value: 1

    columnset_options_type:
        seq:
          - id: value
            type: s4
          - id: block_size
            type: u4

    columnset_manager:
        seq:
          - id: cxx_type
            type: dtype::string
          - id: sequence_number
            type: u4
    storage_desc:
        seq:
          - id: version
            type: s4
            doc: |
              Version was not output for version == 1, so there may be problems for very old tables. Per the docs, in early
              versions the Version number was not written and instead the number of rows was first. Later it was added and
              written as a negative number.
          - id: nrows
            type:
                switch-on: version
                cases:
                  -1: u4
                  -2: u4
                  -3: u8
          - id: options
            type: columnset_options_type
            if: version == -3
          - id: sequence_number
            type: u4
            doc: |
              Highest datamanager sequence used.
          - id: n_managers
            type: u4
          - id: managers
            type: columnset_manager
            repeat: expr
            repeat-expr: n_managers

    array_column_storage_details:
        seq:
          - id: shape_column_definition
            type: u1
          - id: filler
            type: u4
            if: shape_column_definition > 0
          - id: shape
            type: iposition
            if: shape_column_definition > 0

    storage_details:
        params:
          - id: dimensionality
            type: u4
        seq:
          - id: version
            type: u4
          - id: column_keyword_set
            type: table_record
            if: version == 1
          - id: column_name
            type: dtype::string
          - id: column_version
            type: u4
            doc: |
              casacore::ScalarColumnData<unsigned char>::putFileDerived
          - id: manager_number
            type: u4
            doc: |
              casacore::ScalarColumnData<unsigned char>::putFileDerived
          - id: array_details
            type: array_column_storage_details
            if: dimensionality > 0
          - id: array_shape_in_column
            doc: |
              encountered with refim_point_withline.ms/SOURCE/table.dat
            type: u1
            if: dimensionality < 0

    column_spec: # In TableDesc: @ ncol + ColumnDesc[ncol]
       seq:
          - id: n_cols
            type: u4
          - id: details
            type: column_details  # ColumnDesc
            repeat: expr
            repeat-expr: n_cols
          - id: storage           # ColumnSet
            type: storage_desc
          - id: storage_details   # ColumnInfo
            type: storage_details(details[_index].dimensions) # Parameter stored in TableDesc
            repeat: expr
            repeat-expr: n_cols
          - id: n_data_manager_info
            type: u4
          - id: data_manager_info
            type: u1
            repeat: expr
            repeat-expr: n_data_manager_info