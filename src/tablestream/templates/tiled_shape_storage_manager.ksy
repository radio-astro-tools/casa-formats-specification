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
      repeat: expr
      repeat-expr: n_record_files

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
          # Read record here line #92 tiled.py
          - id: flag
            type: b1

  itsms_cube_size:
        seq:
          - id: flag
            type: b1
          - id: mode
            type: u4
            if: flag == true
          - id: unknown
            type: u4
            if: flag == true
          - id: total_cube_size
            type:
              switch-on: mode
              cases:
                1: u4
                2: u8
            if: flag == true



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