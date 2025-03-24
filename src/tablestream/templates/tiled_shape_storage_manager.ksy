# Copyright (C) 2022
# Associated Universities, Inc. Washington DC, USA.
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Library General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Library General Public
# License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 675 Massachusetts Ave, Cambridge, MA 02139, USA.
#
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
    id: tiled_shape_storage_manager
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
    - id: default_tile_shape
      type: iposition
    - id : number_used_row_map
      type: u4
    - id: last_row
      doc: |
        The data might be split into multiple cubes (TSM<index> files). The
        following three values help us piece these together into the main
        hypercube. Each of the lists has length n_cubes where n_cubes is the
        number of individual cubes.

        The index of the last row in the final hypercube in each section. For
        instance, [9, 19] means that the ten first rows (0-9) are in the first
        subcube and the second set of ten rows (10-19) are in the second cube.
      type: block
    - id: cube_index
      doc: |
        The index of the cube in which the rows are stored - this is the value
        used as a suffix in the TSM filename, e.g. TSM2
      type: block
    - id: last_row_subcube
      doc: |
        The index of the last row of the subcube
      type: block



types:
  block:
        seq:
          - id: n_rows
            type: u4
          - id: name
            type: string
          - id: version
            type: u4
          - id: size
            type: u4
          - id: elements
            type: u4
            repeat: expr
            repeat-expr: size

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
          - id: record
            type: record
          - id: flag
            type: b1
          - id: n_dimensions
            type: u4
          - id: cube_shapes
            type: iposition
          - id: tile_shapes
            type: iposition
          - id: more_unknown
            type: u8


  read_type:
        seq:
          - id: nbytes
            type: u4
          - id: type
            type: string
          - id: version
            type: u4

  record:
        seq:
          - id: type
            type: read_type
          - id: record_description
            type: record_description

  record_description:
        seq:
          - id: header
            type: read_type
          - id: n_records
            type: u4
          - id: sub_record_description
            type: sub_record_description
            repeat: expr
            repeat-expr: n_records
          - id: unknown
            type: u4



  sub_record_description:
        seq:
          - id: name
            type: string
          - id: type
            type: u4
          - id: value
            type:
                switch-on: type
                cases:
                  0:  string                 # bool
                  5:  string                 # int
                  6:  string                 # uint
                  7:  string                 # float
                  8:  string                 # double
                  9:  string                 # complex float
                  10: string                 # complex double
                  11: string                 # string
                  12: sub_record_table       # table
                  25: sub_record_description # record description
                  _:  sub_record_array

  sub_record_table:
        seq:
          - id: value
            size: 8

  sub_record_array:
        seq:
          - id: value
            type: iposition
          - id: unknown
            size: 4

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
          - id: nbytes
            type: u4
          - id: type
            type: string
          - id: version
            type: u4
          - id: n_elements
            type: u4
          - id: elements
            type: u4
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