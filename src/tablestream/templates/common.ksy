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
    id: common
    title: Casacore Table Data System header layout
    application:
      - casacore
      - AIPS++
      - CASA
    file-extension: dat
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
  oriented storage system for radio astronomy data. Many systems use it to store, manipulate and process
  the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
  from the telescopes and the images that are produced as a final product. This file parses only the
  table description stored in the table.dat file within the table directory.


seq:
    - id: magic
      contents: [ 0xbe, 0xbe, 0xbe, 0xbe ]
      doc: |
        casa magic unsigned int 3200171710  190 190 190 190
    - id: size
      type: u4
    - id: type
      type: string
    - id: version
      type: u4
    - id: nrows
      type:
          switch-on: version
          cases:
            1: u4
            2: u4
            3: u8
    - id: little_endian
      type: u4
    - id: name
      type: string
      doc: |
        expect "PlainTable"
    - id: table_desc_info
      type: desc_info

instances:
  stream_position:
    value: _io.pos

types:
    desc_info:
        seq:
            - id: size
              type: u4
            - id: type
              type: string
            - id: version
              type: u4
            - id: name
              type: string

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

    table_desc:
        seq:
          - id: size
            type: u4
          - id: type
            type: string
          - id: version
            type: u4
          - id: name
            type: string