meta:
    id: tsm_binary_data
    title: Casacore Table Data System TSM File
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


seq:
  - id: data
    type: u8le
    repeat: eos

types:
    complex8:
      seq:
        - id: real
          type: f4
        - id: imaginary
          type: f4