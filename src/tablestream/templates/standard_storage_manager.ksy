meta:
  id: standard_storage_manager
  endian: le
  file-extension: standard_storage_manager
  imports: dtype

doc: |
    User defined version of base numerical data types. This will allow for the
    compilation of languages like c++ and rust

seq:
  - id: header
    type: header
  - id: header_remains
    size: 512 - _io.pos

types:
  header:
    seq:
      - id: magic
        contents: [ 0xbe, 0xbe, 0xbe, 0xbe ]
        doc: |
          casa magic unsigned int 3200171710  190 190 190 190
      - id: size
        type: u4
      - id: name
        type: string
      - id: version
        type: u4
      - id: is_endian
        type: u1
        enum: is_endian
        if: version > 2
      - id: bucket_size
        type: u4
      - id: n_buckets
        type: u4
      - id: cache_size
        type: u4
        doc: |
          Cache size in buckets
      - id: first_free_bucket
        type: s4
      - id: n_index_buckets
        type: u4
      - id: first_index_bucket
        type: s4
      - id: offset_index
        type: u4
        if: version > 1
      - id: last_string_heap_bucket
        type: s4
      - id: index_length
        type: u4
      - id: n_indicies
        type: u4

  string:
    seq:
      - id: length
        type: u4
      - id: value
        type: str
        encoding: ASCII
        size: length

enums:
  is_endian:
    0: false
    1: true