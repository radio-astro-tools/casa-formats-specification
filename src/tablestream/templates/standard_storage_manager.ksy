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
  - id: bucket
    type: bucket(header.bucket_size)


types:
  bucket:
    params:
      - id: bucket_size
        type: u4
    seq:
      - id: offset
        type: u4
      - id: data
        size: offset - 4
      - id: index
        size: bucket_size - offset
    instances:
        columns:
          pos: offset
          type: one_col

  string_bucket_header:
    seq:
      - id: free_bucket_list
        type: u4
      - id: n_bytes_used
        type: u4
        doc: |
          The number of bytes used, including gaps.
      - id: n_deleted
        type: u4
        doc: |
          Total length of the gaps arising from deletion or updating with a
          shorter string.
      - id: next_bucket
        type: u4
        doc: |
          The bucket containing the continuation of the last string in the bucket.
          If value is -1 there is no continuation.


  one_col:
    seq:
      - id: rows_stored
        type: u4
      - id: rows_populated
        type: u4
        repeat: expr
        repeat-expr: 2 #rows_stored
      - id: some_int
        type: u4
        repeat: expr
        repeat-expr: 1 #50


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
      - id: n_index_buckets
        type: u4
      - id: first_free_bucket
        type: s4
      - id: index_of_bucket
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