meta:
  id: lock
  endian: be
  file-extension: lock
  imports:
    - dtype

doc: |
    There are some issues with this, I need to figure them out but it is at least partly correct...

seq:
    - id: n_processes
      type: u4
    - id: lock_info
      type: list
      repeat: expr
      repeat-expr: 32
    - id: stream_length
      type: u4
    - id: apsio_header
      type: header
    - id: number_rows
      type:
        switch-on: apsio_header.version
        cases:
          0: u4
          1: u4
          2: u8
    - id: number_columns
      type: u4
    - id: modify_column
      type: u4
    - id: change_counter
      type: u4
      doc: |
        Counter incremented if the table.dat has changed.
    - id: data_block
      type: data_block

types:
  header:
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
        type: u1

  list:
    seq:
      - id: fcntl
        type: u1
        doc: |
          Acquire/release of lock can be shared (read) or exclusive (write)
      - id: proc
        type: u1
        doc: |
          Tells other processes that table is open. Creates a shared lock.
      - id: lock_type
        type: u1
        doc: |
          Permanent or shared lock.
      - id: special
        type: u1
        repeat: expr
        repeat-expr: 3
        doc: |
          Special internal lock usage.
      - id: host_id
        type: u1
      - id: process_id
        type: u1


  data_block:
    seq:
      - id: block
        type: u4
        repeat: eos