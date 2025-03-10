meta:
    id: tiled_shape
    title: Casacore Table Data System StandardStMan layout
    application:
      - casacore
      - AIPS++
      - CASA
    tags:
      - scientific
      - astronomy
    license: LGPL-2.0-or-later
    ks-version: 0.10
    endian: be
    imports:
      - dtype

doc: |
  The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
  oriented storage system for radio astronoy data. Many systems use it to store, manipulate and process
  the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
  from the telescopes and the images that are produced as a final product. This file parses only the
  table description stored in the table.dat file within the table directory.

#params:
#    - id: stream
#      type: regular_table_description::table_desc::column_spec::column_desc

seq:
    - id: header
      type: header
    - id: number
      type: u4
    - id: type
      type: string
    - id: version
      doc: 4 is big endian while 5 is little endian
      type: u4
    - id: isbigendian
      type: u1
      if: version == 5
    - id: idk
      type: u1
    - id: sequence_numer
      type: u4
    - id: n_rows
      type: u4
    - id: n_columns
      type: u4
    - id: dtype
      type: u4
    - id: column_name
      type: string
    - id: max_cache
      type: u4
    - id: n_dimensions
      type: u4
    - id: n_record_files
      type: u4
    - id: itsm_cube_size
      type: itsms_cube_size
      repeat: expr
      repeat-expr: n_record_files
    - id: unknown
      type: u4
    - id: itsm_dimension
      type: itsms_dimension
#      repeat: expr
#      repeat-expr: n_record_files

#    - id: tile_size
#      type: iposition


types:
  header:
        seq:
          - id: magic
            contents: [ 0xbe, 0xbe, 0xbe, 0xbe ]
            doc: casa magic unsigned int 3200171710  190 190 190 190
          - id: number
            type: u4
          - id: type
            type: string
          - id: version
            doc: 4 is big endian while 5 is little endian
            type: u4
          - id: isbigendian
            type: u1
            if: version == 5

  itsms_dimension:
        seq:
          - id: unknown
            type: u4
          - id: type
            type: string
          #- id: record
          #  type: t_record
          # Read record here ln #92 tiled.py
          - id: flag
            type: b1

  t_record:
        seq:
          - id: record_header
            type: u1

  itsms_cube_size:
        seq:
          - id: flag
            type: u1
          - id: mode
            type: u4
            if: flag == 0x1
          - id: unknown
            type: u4
            if: flag == 0x1
          - id: total_cube_size
            type:
              switch-on: mode
              cases:
                1: u4
                2: u8
            if: flag == 0x1



  string:
        seq:
          - id: length
            type: u4
          - id: value
            type: str
            encoding: ASCII
            size: length

  iposition:
        seq:
          - id: type
            type: string
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
  complex8:
        seq:
          - id: real
            type: f4
          - id: imaginary
            type: f4

  complex16:
        seq:
          - id: real
            type: f8
          - id: imaginary
            type: f8

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
                  9:  complex8
                  10: complex16
                  11: string
                  12: string
                  25: table_record
                  29: dtype::int8
                  _: array(type)
  array:
        params:
          - id: type
            type: u2
        seq:
          - id: size
            type: u4
          - id: cxx_type
            type: string
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
                  22: complex8
                  23: complex16
                  24: string
                  30: dtype::int8

  # ======== Table record ======== #

  table_record:
        seq:
          - id: size
            type: u4
#          - id: type
#            type: type_name("TableRecord")
#          - id: version
#            type: u4
#          - id: desc
#            type: record_desc

  record_field_desc:
        seq:
          - id: name
            type: string
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
            type: string
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
            type: string

  record_desc:
        seq:
          - id: size
            type: u4
          - id: type
            type: type_name("RecordDesc")
          - id: version
            type: u4
          - id: n_keywords
            type: s4
          - id: fields
            type: record_field_desc
            repeat: expr
            repeat-expr: n_keywords
          - id: record_type
            type: s4
          - id: values
            type: record_field_value(fields[_index].type)
            repeat: expr
            repeat-expr: n_keywords