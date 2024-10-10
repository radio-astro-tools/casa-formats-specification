meta:
  id: meta_data
  endian: be

seq:
  - id: magic_code
    contents: [0xbe, 0xbe, 0xbe, 0xbe]
  - id: aipsio_header
    type: header
  - id: number_of_table_rows
    type: u4
  - id: endianess
    type: u4
  - id: table_type
    type: string
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
      - id: table_description_header
        type: header
      - id: table_description_name
        type: string
      - id: table_description_version
        type: string
      - id: table_description_comment
        type: string
      - id: table_keyword_set
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



  keyword_data:
    seq:
      - id: keyword_name
        type: string
      - id: data_type
        type: s4