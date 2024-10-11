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
  id: meta_data
  endian: be

seq:
  - id: magic_code
    contents: [0xbe, 0xbe, 0xbe, 0xbe]
  - id: aipsio_header
    type: header
  - id: number_of_table_rows
    type:
          switch-on: aipsio_header.version
          cases:
            1: u4
            2: u4
            3: u8

  - id: endianess
    type: u4
  - id: table_type
    type: string
    doc: expect "PlainTable"
  - id: table_description
    type: table_description

types:
  string:
    seq:
      - id: string_length
        type: u4
      - id: body
        type: str
        size: string_length
        encoding: ASCII

  header:
    seq:
      - id: size
        type: u4
      - id: object_type
        type: string
      - id: version
        type: u4

  table_description:
    seq:
      - id: header
        type: header
      - id: name
        type: string
      - id: version
        type: string
      - id: comment
        type: string
      - id: keyword_set
        type: table_record

  table_record:
    seq:
      - id: table_record_header
        type: header
      - id: record_description
        type: record_description
      - id: record_type
        type: s4

  record_description:
    seq:
      - id: record_description_header
        type: header
      - id: number_of_keywords
        type: u4
      - id: record_description_subfield
        type: record_description_subfield


  record_description_subfield:
    seq:
      - id: name
        type: string
      - id: data_type
        type: s4
      - id: subtable_filler
        type: u4
        if: data_type == 12
      - id: string_array_filler_size
        type: u4
        if: data_type == 24
      - id: comment
        type: string
        if: data_type != 25

  keyword_data:
    seq:
      - id: keyword_name
        type: string
      - id: data_type
        type: s4