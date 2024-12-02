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

doc: |
  The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
  oriented storage system for radio astronoy data. Many systems use it to store, manipulate and process
  the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
  from the telescopes and the images that are produced as a final product. This file parses only the
  table description stored in the table.dat file within the table directory.

seq:
    - id: header
      type: header
    - id: trash
      size: 512 - _io.pos
    - id: data
      type: bucket(header.bucket_size)
      repeat: expr
      repeat-expr: header.num_buckets
    - id: index_set
      type: index_set

types:

    bucket:
        params:
          - id: bucket_size
            type: u4
        seq:
          - id: index_offset
            type: u4
          - id: data
            size: index_offset - 4
          - id: index
            size: bucket_size - index_offset
        instances:
          first_col:
            pos: 28977
            type: one_col

    one_col:
        seq:
          - id: rows_stored
            type: u4
          - id: rows_populated
            type: u4
            repeat: expr
            repeat-expr: rows_stored
          - id: some_int
            type: u4
            repeat: expr
            repeat-expr: 50

    onex_col:
        seq:
          - id: num_rows
            type: u4
          - id: row_numbers_of_values_stored_in_row
            type: u4
          - id: offset_in_data_part_of_values_stored
            type: u4
            repeat: expr
            repeat-expr: num_rows

    data_block:
        params:
          - id: block_size
            type: u4
        seq:
          - id: block
            size: block_size

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

    header:
        seq:
          - id: magic
            contents: [ 0xbe, 0xbe, 0xbe, 0xbe ]
            doc: casa magic unsigned int 3200171710  190 190 190 190
          - id: number01
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
          - id: index_2_row
            doc: rows_p in ISMIndex.cc
            type: index_map(version)
          - id: index_2_bucket
            doc: bucketNr_p in ISMIndex.cc, row number index_2_row[i] starts in bucket number index_2_bucket[i]
            type: index_map(version)

    index_map:
        params:
          - id: index_version
            type: u4
        seq:
          - id: number
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


    string:
        seq:
          - id: len
            type: u4
          - id: value
            type: str
            encoding: ASCII
            size: len