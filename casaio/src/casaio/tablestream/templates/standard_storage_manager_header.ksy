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
  id: standard
  file-extension: standard
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
            doc: >= 3 is little endian, else big endian
            type: u4
          - id: isbigendian
            type: u1
            if: version >= 3
          - id: bucket_size
            type: u4
          - id: n_buckets
            type: u4
          - id: persistent_chache
            type: u4
          - id: n_free_buckets
            type: u4
          - id: first_free_bucket
            type: u4
          - id: n_bucket_index
            type: u4
          - id: first_index_bucket_number
            type: u4
          - id: bucket_offset_index
            type: u4
          - id: last_string_bucket
            type: u4
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