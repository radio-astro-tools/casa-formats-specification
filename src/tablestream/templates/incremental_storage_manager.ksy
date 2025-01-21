meta:
    id: table_incremental_store
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
    endian: le
    imports:
      - dtype
      - metadata

doc: |
  The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
  oriented storage system for radio astronoy data. Many systems use it to store, manipulate and process
  the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
  from the telescopes and the images that are produced as a final product. This file parses only the
  table description stored in the table.dat file within the table directory.

params:
    - id: stream
      type: io[]

seq:
    - id: header
      type: header
    - id: trash
      size: 512 - _io.pos
    - id: data
      type: block(header.bucket_size)
      repeat: expr
      repeat-expr: header.num_buckets

instances:
  index_set:
    pos: header.bucket_size + 0x0200    # 512 = 0x0200 or the header size
    type: index_set


types:
    block:
        params:
          - id: bucket_size
            type: u4

        seq:
          - id: index_offset                  # This is length in astropy
            type: u4
          - id: data
            size: index_offset - 4
          - id: n_indices
            type: u4
          - id: index
            type: u4
            repeat: expr
            repeat-expr: n_indices
          - id: offsets
            type: u4
            repeat: expr
            repeat-expr: n_indices

        instances:
            n_indicies:
              pos: 0x0200
              type: u4

            values:
              io: _root.stream
              pos: 0x0204
              type: data_value(_io.desc.table.columns.column_desc[_index].data_type)
              repeat: expr
              repeat-expr: n_indices

    data_block:
        params:
          - id: block_size
            type: u4
        seq:
          - id: block
            size: block_size

    #################### Data types #######################

    data_value:
        params:
          - id: type
            type: s4
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
                  29: dtype::int8
                  _: array(type)

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

    string:
        seq:
          - id: length
            type: u4
          - id: value
            type: str
            encoding: ASCII
            size: length

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

    ####################################

    type_name:
        params:
          - id: value
            type: str
        seq:
          - id: size
            type: u4
          - id: name
            size: value.length      # `str.length` gives the number of *characters*, not bytes as we would need here; but in ASCII they're equal
            type: str
            encoding: ASCII
            valid:
              eq: value

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
          - id: bucket_size
            type: u4
          - id: num_buckets
            type: u4
          - id: persistent_cache_size
            type: u4
          - id: unique_column_number
            type: u4
          - id: number_free_buckets
            type: u4
          - id: first_free_bucket
            type: s4

    index_set:
        seq:
          - id: magic
            contents: [ 0xbe, 0xbe, 0xbe, 0xbe ]
            doc: casa magic unsigned int 3200171710  190 190 190 190
          - id: size
            type: u4
          - id: type
            type: type_name("ISMIndex")
          - id: version
            type: u4
          - id: blocks_in_use
            type: u4
          - id: row_number
            doc: rows_p in ISMIndex.cc
            type: index_map(version)
          - id: bucket_number
            doc: bucketNr_p in ISMIndex.cc, row number index_2_row[i] starts in bucket number index_2_bucket[i]
            type: index_map(version)

    index_map:
        params:
          - id: index_version
            type: u4
        seq:
          - id: n_rows
            type: u4
          - id: type
            type: type_name("Block")
          - id: version
            type: u4
          - id: size
            type: u4
          - id: elements
            type:
              switch-on: index_version
              cases:
                1: u4
                _: u8
            repeat: expr
            repeat-expr: size