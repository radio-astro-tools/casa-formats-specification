// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

use std::option::Option;
use std::boxed::Box;
use std::io::Result;
use std::io::Cursor;
use std::vec::Vec;
use std::default::Default;
use kaitai_struct::KaitaiStream;
use kaitai_struct::KaitaiStruct;


/*
 * The [casacore table system](https://casacore.github.io/casacore-notes/255.html) is a binary, table
 * oriented storage system for radio astronoy data. Many systems use it to store, manipulate and process
 * the data collected from radio telescopes. It can be used to store both the raw visibilities as collected
 * from the telescopes and the images that are produced as a final product. This file parses only the
 * table description stored in the table.dat file within the table directory.
 */
#[derive(Default)]
pub struct Metadata {
    pub magic: Vec<u8>,
    pub size: u32,
    pub type: Box<Dtype__String>,
    pub version: u32,
    pub nrows: u64,
    pub littleEndian: u32,
    pub name: Box<Dtype__String>,
    pub desc: Box<Metadata__TableDesc>,
}

impl KaitaiStruct for Metadata {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.magic = self.stream.read_bytes(4)?;
        self.size = self.stream.read_u4be()?;
        self.type = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.version = self.stream.read_u4be()?;
        match self.version {
            1 => {
                self.nrows = self.stream.read_u4be()?;
            },
            2 => {
                self.nrows = self.stream.read_u4be()?;
            },
            3 => {
                self.nrows = self.stream.read_u8be()?;
            },
        }
        self.littleEndian = self.stream.read_u4be()?;
        self.name = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.desc = Box::new(Metadata__TableDesc::new(self.stream, self, _root)?);
    }
}

impl Metadata {

    /*
     * casa magic unsigned int 3200171710  190 190 190 190
     */

    /*
     * expect "PlainTable"
     */

    /*
     * TableDesc
     */
}
#[derive(Default)]
pub struct Metadata__ArrayColumnStorageDetails {
    pub shapeColumnDefinition: u8,
    pub filler: u32,
    pub shape: Box<Metadata__Iposition>,
}

impl KaitaiStruct for Metadata__ArrayColumnStorageDetails {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.shapeColumnDefinition = self.stream.read_u1()?;
        if self.shape_column_definition > 0 {
            self.filler = self.stream.read_u4be()?;
        }
        if self.shape_column_definition > 0 {
            self.shape = Box::new(Metadata__Iposition::new(self.stream, self, _root)?);
        }
    }
}

impl Metadata__ArrayColumnStorageDetails {
}
#[derive(Default)]
pub struct Metadata__DataValue {
    pub value: Option<Box<KaitaiStruct>>,
}

impl KaitaiStruct for Metadata__DataValue {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        match self.type {
            10 => {
                self.value = Box::new(Dtype__Complex16::new(self.stream, self, _root)?);
            },
            0 => {
                self.value = Box::new(Dtype__Uint1::new(self.stream, self, _root)?);
            },
            4 => {
                self.value = Box::new(Dtype__Uint2::new(self.stream, self, _root)?);
            },
            6 => {
                self.value = Box::new(Dtype__Uint4::new(self.stream, self, _root)?);
            },
            7 => {
                self.value = Box::new(Dtype__Float4::new(self.stream, self, _root)?);
            },
            1 => {
                self.value = Box::new(Dtype__Int1::new(self.stream, self, _root)?);
            },
            11 => {
                self.value = Box::new(Dtype__String::new(self.stream, self, _root)?);
            },
            12 => {
                self.value = Box::new(Dtype__String::new(self.stream, self, _root)?);
            },
            3 => {
                self.value = Box::new(Dtype__Int2::new(self.stream, self, _root)?);
            },
            5 => {
                self.value = Box::new(Dtype__Int4::new(self.stream, self, _root)?);
            },
            8 => {
                self.value = Box::new(Dtype__Float8::new(self.stream, self, _root)?);
            },
            9 => {
                self.value = Box::new(Dtype__Complex8::new(self.stream, self, _root)?);
            },
            2 => {
                self.value = Box::new(Dtype__Uint1::new(self.stream, self, _root)?);
            },
            29 => {
                self.value = Box::new(Dtype__Int8::new(self.stream, self, _root)?);
            },
            25 => {
                self.value = Box::new(Metadata__TableRecord::new(self.stream, self, _root)?);
            },
            _ => {
                self.value = Box::new(Metadata__Array::new(self.stream, self, _root)?);
            }
        }
    }
}

impl Metadata__DataValue {
}
#[derive(Default)]
pub struct Metadata__ReferenceTableDesc {
    pub columnMapSize: u32,
    pub columnMapType: Box<Metadata__TypeName>,
    pub columnMapVersion: u32,
    pub defaultValue: u32,
    pub nColumnMaps: u32,
    pub blockAllocationIncrement: u32,
    pub columnMaps: Vec<Box<Metadata__ColumnMap>>,
    pub columnOrderSize: u32,
    pub columnOrderType: Box<Metadata__TypeName>,
    pub columnOrderVersion: u32,
    pub nColumnOrderShape: u32,
    pub columnOrderShape: Vec<u32>,
    pub nColumnOrder: u32,
    pub columnOrder: Vec<Box<Dtype__String>>,
    pub rowOrder: Option<Box<KaitaiStruct>>,
    pub type: Option<i8>,
}

impl KaitaiStruct for Metadata__ReferenceTableDesc {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.columnMapSize = self.stream.read_u4be()?;
        self.columnMapType = Box::new(Metadata__TypeName::new(self.stream, self, _root)?);
        self.columnMapVersion = self.stream.read_u4be()?;
        self.defaultValue = self.stream.read_u4be()?;
        self.nColumnMaps = self.stream.read_u4be()?;
        self.blockAllocationIncrement = self.stream.read_u4be()?;
        self.columnMaps = vec!();
        for i in 0..self.n_column_maps {
            self.columnMaps.append(Box::new(Metadata__ColumnMap::new(self.stream, self, _root)?));
        }
        self.columnOrderSize = self.stream.read_u4be()?;
        self.columnOrderType = Box::new(Metadata__TypeName::new(self.stream, self, _root)?);
        self.columnOrderVersion = self.stream.read_u4be()?;
        self.nColumnOrderShape = self.stream.read_u4be()?;
        self.columnOrderShape = vec!();
        for i in 0..self.n_column_order_shape {
            self.columnOrderShape.append(self.stream.read_u4be()?);
        }
        self.nColumnOrder = self.stream.read_u4be()?;
        self.columnOrder = vec!();
        for i in 0..self.n_column_order {
            self.columnOrder.append(Box::new(Dtype__String::new(self.stream, self, _root)?));
        }
        match self.version {
            2 => {
                self.rowOrder = Box::new(Metadata__ColumnRowDetails32b::new(self.stream, self, _root)?);
            },
            1 => {
                self.rowOrder = Box::new(Metadata__ColumnRowDetails64b::new(self.stream, self, _root)?);
            },
        }
    }
}

impl Metadata__ReferenceTableDesc {
    fn type(&mut self) -> i8 {
        if let Some(x) = self.type {
            return x;
        }

        self.type = 2;
        return self.type;
    }
}
#[derive(Default)]
pub struct Metadata__Iposition {
    pub type: Box<Dtype__String>,
    pub version: u32,
    pub nElements: u32,
    pub elements: Vec<u64>,
}

impl KaitaiStruct for Metadata__Iposition {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.type = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.version = self.stream.read_u4be()?;
        self.nElements = self.stream.read_u4be()?;
        self.elements = vec!();
        for i in 0..self.n_elements {
            match self.version {
                1 => {
                    self.elements.append(self.stream.read_u4be()?);
                },
                2 => {
                    self.elements.append(self.stream.read_u8be()?);
                },
            }
        }
    }
}

impl Metadata__Iposition {

    /*
     * 1 implies 4 byte shape numbers but 2 implies 8 byte shape numbers
     */
}
#[derive(Default)]
pub struct Metadata__ColumnsetOptionsType {
    pub value: i32,
    pub blockSize: u32,
}

impl KaitaiStruct for Metadata__ColumnsetOptionsType {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.value = self.stream.read_s4be()?;
        self.blockSize = self.stream.read_u4be()?;
    }
}

impl Metadata__ColumnsetOptionsType {
}
#[derive(Default)]
pub struct Metadata__SubrecordDesc {
    pub size: u32,
    pub type: Box<Metadata__TypeName>,
    pub version: u32,
    pub nFields: i32,
    pub comment: Box<Dtype__String>,
}

impl KaitaiStruct for Metadata__SubrecordDesc {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.size = self.stream.read_u4be()?;
        self.type = Box::new(Metadata__TypeName::new(self.stream, self, _root)?);
        self.version = self.stream.read_u4be()?;
        self.nFields = self.stream.read_s4be()?;
        self.comment = Box::new(Dtype__String::new(self.stream, self, _root)?);
    }
}

impl Metadata__SubrecordDesc {
}
#[derive(Default)]
pub struct Metadata__ColumnRowDetails64b {
    pub numMapsBase: u64,
    pub hasRowOrder: u8,
    pub numMaps: u64,
    pub maps: Vec<u32>,
}

impl KaitaiStruct for Metadata__ColumnRowDetails64b {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.numMapsBase = self.stream.read_u8be()?;
        self.hasRowOrder = self.stream.read_u1()?;
        self.numMaps = self.stream.read_u8be()?;
        self.maps = vec!();
        for i in 0..self.num_maps {
            self.maps.append(self.stream.read_u4be()?);
        }
    }
}

impl Metadata__ColumnRowDetails64b {
}
#[derive(Default)]
pub struct Metadata__TableDesc {
    pub size: u32,
    pub type: Box<Dtype__String>,
    pub version: u32,
    pub name: Box<Dtype__String>,
    pub table: Option<Box<KaitaiStruct>>,
}

impl KaitaiStruct for Metadata__TableDesc {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.size = self.stream.read_u4be()?;
        self.type = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.version = self.stream.read_u4be()?;
        self.name = Box::new(Dtype__String::new(self.stream, self, _root)?);
        match self.type.value {
            "TableDesc" => {
                self.table = Box::new(Metadata__RegularTableDesc::new(self.stream, self, _root)?);
            },
            "RefTable" => {
                self.table = Box::new(Metadata__ReferenceTableDesc::new(self.stream, self, _root)?);
            },
        }
    }
}

impl Metadata__TableDesc {
}
#[derive(Default)]
pub struct Metadata__ColumnSpec {
    pub nCols: u32,
    pub details: Vec<Box<Metadata__ColumnDetails>>,
    pub storage: Box<Metadata__StorageDesc>,
    pub storageDetails: Vec<Box<Metadata__StorageDetails>>,
    pub nDataManagerInfo: u32,
    pub dataManagerInfo: Vec<u8>,
}

impl KaitaiStruct for Metadata__ColumnSpec {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.nCols = self.stream.read_u4be()?;
        self.details = vec!();
        for i in 0..self.n_cols {
            self.details.append(Box::new(Metadata__ColumnDetails::new(self.stream, self, _root)?));
        }
        self.storage = Box::new(Metadata__StorageDesc::new(self.stream, self, _root)?);
        self.storageDetails = vec!();
        for i in 0..self.n_cols {
            self.storageDetails.append(Box::new(Metadata__StorageDetails::new(self.stream, self, _root)?));
        }
        self.nDataManagerInfo = self.stream.read_u4be()?;
        self.dataManagerInfo = vec!();
        for i in 0..self.n_data_manager_info {
            self.dataManagerInfo.append(self.stream.read_u1()?);
        }
    }
}

impl Metadata__ColumnSpec {
}
#[derive(Default)]
pub struct Metadata__RecordFieldDesc {
    pub name: Box<Dtype__String>,
    pub type: i32,
    pub subtableFiller: u32,
    pub stringArrayFillerSize: u32,
    pub stringArrayFillerIposition: Box<Metadata__Iposition>,
    pub comment: Box<Dtype__String>,
    pub subrecord: Box<Metadata__SubrecordDesc>,
}

impl KaitaiStruct for Metadata__RecordFieldDesc {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.name = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.type = self.stream.read_s4be()?;
        if self.type == 12 {
            self.subtableFiller = self.stream.read_u4be()?;
        }
        if self.type == 24 {
            self.stringArrayFillerSize = self.stream.read_u4be()?;
        }
        if self.type == 24 {
            self.stringArrayFillerIposition = Box::new(Metadata__Iposition::new(self.stream, self, _root)?);
        }
        if self.type != 25 {
            self.comment = Box::new(Dtype__String::new(self.stream, self, _root)?);
        }
        if self.type == 25 {
            self.subrecord = Box::new(Metadata__SubrecordDesc::new(self.stream, self, _root)?);
        }
    }
}

impl Metadata__RecordFieldDesc {
}
#[derive(Default)]
pub struct Metadata__Array {
    pub size: u32,
    pub cxxType: Box<Dtype__String>,
    pub version: u32,
    pub nShape: u32,
    pub shape: Vec<u32>,
    pub nElements: u32,
    pub elements: Vec<Option<Box<KaitaiStruct>>>,
}

impl KaitaiStruct for Metadata__Array {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.size = self.stream.read_u4be()?;
        self.cxxType = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.version = self.stream.read_u4be()?;
        self.nShape = self.stream.read_u4be()?;
        self.shape = vec!();
        for i in 0..self.n_shape {
            self.shape.append(self.stream.read_u4be()?);
        }
        self.nElements = self.stream.read_u4be()?;
        self.elements = vec!();
        for i in 0..self.n_elements {
            match self.type {
                14 => {
                    self.elements.append(Box::new(Dtype__Int1::new(self.stream, self, _root)?));
                },
                17 => {
                    self.elements.append(Box::new(Dtype__Uint2::new(self.stream, self, _root)?));
                },
                24 => {
                    self.elements.append(Box::new(Dtype__String::new(self.stream, self, _root)?));
                },
                20 => {
                    self.elements.append(Box::new(Dtype__Float4::new(self.stream, self, _root)?));
                },
                13 => {
                    self.elements.append(Box::new(Dtype__Uint1::new(self.stream, self, _root)?));
                },
                19 => {
                    self.elements.append(Box::new(Dtype__Uint4::new(self.stream, self, _root)?));
                },
                23 => {
                    self.elements.append(Box::new(Dtype__Complex16::new(self.stream, self, _root)?));
                },
                15 => {
                    self.elements.append(Box::new(Dtype__Uint1::new(self.stream, self, _root)?));
                },
                21 => {
                    self.elements.append(Box::new(Dtype__Float8::new(self.stream, self, _root)?));
                },
                16 => {
                    self.elements.append(Box::new(Dtype__Int2::new(self.stream, self, _root)?));
                },
                18 => {
                    self.elements.append(Box::new(Dtype__Int4::new(self.stream, self, _root)?));
                },
                22 => {
                    self.elements.append(Box::new(Dtype__Complex8::new(self.stream, self, _root)?));
                },
                30 => {
                    self.elements.append(Box::new(Dtype__Int8::new(self.stream, self, _root)?));
                },
            }
        }
    }
}

impl Metadata__Array {
}
#[derive(Default)]
pub struct Metadata__Hacky {
    pub size: u32,
    pub type: Box<Dtype__String>,
}

impl KaitaiStruct for Metadata__Hacky {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.size = self.stream.read_u4be()?;
        self.type = Box::new(Dtype__String::new(self.stream, self, _root)?);
    }
}

impl Metadata__Hacky {
}
#[derive(Default)]
pub struct Metadata__ColumnRowDetails32b {
    pub nMapsBase: u32,
    pub hasRowOrder: u8,
    pub nMaps: u32,
    pub maps: Vec<u32>,
}

impl KaitaiStruct for Metadata__ColumnRowDetails32b {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.nMapsBase = self.stream.read_u4be()?;
        self.hasRowOrder = self.stream.read_u1()?;
        self.nMaps = self.stream.read_u4be()?;
        self.maps = vec!();
        for i in 0..self.n_maps {
            self.maps.append(self.stream.read_u4be()?);
        }
    }
}

impl Metadata__ColumnRowDetails32b {
}
#[derive(Default)]
pub struct Metadata__Default {
    pub value: Option<Box<KaitaiStruct>>,
}

impl KaitaiStruct for Metadata__Default {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        match self.type {
            10 => {
                self.value = Box::new(Dtype__Complex16::new(self.stream, self, _root)?);
            },
            0 => {
                self.value = Box::new(Dtype__Uint1::new(self.stream, self, _root)?);
            },
            4 => {
                self.value = Box::new(Dtype__Uint2::new(self.stream, self, _root)?);
            },
            6 => {
                self.value = Box::new(Dtype__Uint4::new(self.stream, self, _root)?);
            },
            7 => {
                self.value = Box::new(Dtype__Float4::new(self.stream, self, _root)?);
            },
            1 => {
                self.value = Box::new(Dtype__Int1::new(self.stream, self, _root)?);
            },
            11 => {
                self.value = Box::new(Dtype__String::new(self.stream, self, _root)?);
            },
            3 => {
                self.value = Box::new(Dtype__Int2::new(self.stream, self, _root)?);
            },
            5 => {
                self.value = Box::new(Dtype__Int4::new(self.stream, self, _root)?);
            },
            8 => {
                self.value = Box::new(Dtype__Float8::new(self.stream, self, _root)?);
            },
            9 => {
                self.value = Box::new(Dtype__Complex8::new(self.stream, self, _root)?);
            },
            2 => {
                self.value = Box::new(Dtype__Uint1::new(self.stream, self, _root)?);
            },
            29 => {
                self.value = Box::new(Dtype__Int8::new(self.stream, self, _root)?);
            },
            _ => {
                self.value = Box::new(Metadata__Array::new(self.stream, self, _root)?);
            }
        }
    }
}

impl Metadata__Default {
}
#[derive(Default)]
pub struct Metadata__RegularTableDesc {
    pub descVersion: Box<Dtype__String>,
    pub comment: Box<Dtype__String>,
    pub userKeywords: Box<Metadata__TableRecord>,
    pub privateKeywords: Box<Metadata__TableRecord>,
    pub columns: Box<Metadata__ColumnSpec>,
    pub type: Option<i8>,
}

impl KaitaiStruct for Metadata__RegularTableDesc {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.descVersion = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.comment = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.userKeywords = Box::new(Metadata__TableRecord::new(self.stream, self, _root)?);
        self.privateKeywords = Box::new(Metadata__TableRecord::new(self.stream, self, _root)?);
        self.columns = Box::new(Metadata__ColumnSpec::new(self.stream, self, _root)?);
    }
}

impl Metadata__RegularTableDesc {
    fn type(&mut self) -> i8 {
        if let Some(x) = self.type {
            return x;
        }

        self.type = 1;
        return self.type;
    }
}
#[derive(Default)]
pub struct Metadata__RecordFieldValue {
    pub value: Box<Metadata__DataValue>,
}

impl KaitaiStruct for Metadata__RecordFieldValue {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.value = Box::new(Metadata__DataValue::new(self.stream, self, _root)?);
    }
}

impl Metadata__RecordFieldValue {
}
#[derive(Default)]
pub struct Metadata__StorageDetails {
    pub version: u32,
    pub columnKeywordSet: Box<Metadata__TableRecord>,
    pub columnName: Box<Dtype__String>,
    pub columnVersion: u32,
    pub managerNumber: u32,
    pub arrayDetails: Box<Metadata__ArrayColumnStorageDetails>,
    pub arrayShapeInColumn: u8,
}

impl KaitaiStruct for Metadata__StorageDetails {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.version = self.stream.read_u4be()?;
        if self.version == 1 {
            self.columnKeywordSet = Box::new(Metadata__TableRecord::new(self.stream, self, _root)?);
        }
        self.columnName = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.columnVersion = self.stream.read_u4be()?;
        self.managerNumber = self.stream.read_u4be()?;
        if self.dimensionality > 0 {
            self.arrayDetails = Box::new(Metadata__ArrayColumnStorageDetails::new(self.stream, self, _root)?);
        }
        if self.dimensionality < 0 {
            self.arrayShapeInColumn = self.stream.read_u1()?;
        }
    }
}

impl Metadata__StorageDetails {

    /*
     * casacore::ScalarColumnData<unsigned char>::putFileDerived
     */

    /*
     * casacore::ScalarColumnData<unsigned char>::putFileDerived
     */

    /*
     * encountered with refim_point_withline.ms/SOURCE/table.dat
     */
}
#[derive(Default)]
pub struct Metadata__StorageDesc {
    pub version: i32,
    pub nrows: u64,
    pub options: Box<Metadata__ColumnsetOptionsType>,
    pub sequenceNumber: u32,
    pub nManagers: u32,
    pub managers: Vec<Box<Metadata__ColumnsetManager>>,
}

impl KaitaiStruct for Metadata__StorageDesc {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.version = self.stream.read_s4be()?;
        match self.version {
            -1 => {
                self.nrows = self.stream.read_u4be()?;
            },
            -2 => {
                self.nrows = self.stream.read_u4be()?;
            },
            -3 => {
                self.nrows = self.stream.read_u8be()?;
            },
        }
        if self.version == -3 {
            self.options = Box::new(Metadata__ColumnsetOptionsType::new(self.stream, self, _root)?);
        }
        self.sequenceNumber = self.stream.read_u4be()?;
        self.nManagers = self.stream.read_u4be()?;
        self.managers = vec!();
        for i in 0..self.n_managers {
            self.managers.append(Box::new(Metadata__ColumnsetManager::new(self.stream, self, _root)?));
        }
    }
}

impl Metadata__StorageDesc {

    /*
     * Version was not output for version == 1, so there may be problems for very old tables. Per the docs, in early
     * versions the Version number was not written and instead the number of rows was first. Later it was added and
     * written as a negative number.
     */

    /*
     * Highest datamanager sequence used.
     */
}
#[derive(Default)]
pub struct Metadata__TypeName {
    pub size: u32,
    pub name: String,
}

impl KaitaiStruct for Metadata__TypeName {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.size = self.stream.read_u4be()?;
        self.name = String::from_utf8_lossy(self.stream.read_bytes(self.value.len())?);
    }
}

impl Metadata__TypeName {
}
#[derive(Default)]
pub struct Metadata__ColumnDetails {
    pub version: u32,
    pub cxxType: Box<Dtype__String>,
    pub versionParent: u32,
    pub name: Box<Dtype__String>,
    pub comment: Box<Dtype__String>,
    pub managerType: Box<Dtype__String>,
    pub managerGroup: Box<Dtype__String>,
    pub dataType: i32,
    pub options: i32,
    pub dimensions: i32,
    pub maxLength: i32,
    pub shape: Box<Metadata__Iposition>,
    pub maxLengthOfString: u32,
    pub keywords: Box<Metadata__TableRecord>,
    pub columnTemplateClassVersion: u32,
    pub default: Box<Metadata__Default>,
    pub dummyFlag: u8,
}

impl KaitaiStruct for Metadata__ColumnDetails {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.version = self.stream.read_u4be()?;
        self.cxxType = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.versionParent = self.stream.read_u4be()?;
        self.name = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.comment = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.managerType = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.managerGroup = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.dataType = self.stream.read_s4be()?;
        self.options = self.stream.read_s4be()?;
        self.dimensions = self.stream.read_s4be()?;
        self.maxLength = self.stream.read_s4be()?;
        if self.dimensions != 0 {
            self.shape = Box::new(Metadata__Iposition::new(self.stream, self, _root)?);
        }
        if self.dimensions != 0 {
            self.maxLengthOfString = self.stream.read_u4be()?;
        }
        self.keywords = Box::new(Metadata__TableRecord::new(self.stream, self, _root)?);
        self.columnTemplateClassVersion = self.stream.read_u4be()?;
        if  ((self.dimensions == 0) && (self.data_type != 25))  {
            self.default = Box::new(Metadata__Default::new(self.stream, self, _root)?);
        }
        if  ((self.dimensions != 0) && (self.data_type != 25))  {
            self.dummyFlag = self.stream.read_u1()?;
        }
    }
}

impl Metadata__ColumnDetails {

    /*
     * MAY HAVE SHAPE NEXT to be done
     */

    /*
     * e.g. ScalarColumnDesc<T> putDesc, ScaColDesc.tcc line 149
     */
}
#[derive(Default)]
pub struct Metadata__ColumnsetManager {
    pub cxxType: Box<Dtype__String>,
    pub sequenceNumber: u32,
}

impl KaitaiStruct for Metadata__ColumnsetManager {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.cxxType = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.sequenceNumber = self.stream.read_u4be()?;
    }
}

impl Metadata__ColumnsetManager {
}
#[derive(Default)]
pub struct Metadata__ColumnMap {
    pub key: Box<Dtype__String>,
    pub val: Box<Dtype__String>,
}

impl KaitaiStruct for Metadata__ColumnMap {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.key = Box::new(Dtype__String::new(self.stream, self, _root)?);
        self.val = Box::new(Dtype__String::new(self.stream, self, _root)?);
    }
}

impl Metadata__ColumnMap {
}
#[derive(Default)]
pub struct Metadata__RecordDesc {
    pub size: u32,
    pub type: Box<Metadata__TypeName>,
    pub version: u32,
    pub nFields: i32,
    pub fields: Vec<Box<Metadata__RecordFieldDesc>>,
    pub recordType: i32,
    pub values: Vec<Box<Metadata__RecordFieldValue>>,
}

impl KaitaiStruct for Metadata__RecordDesc {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.size = self.stream.read_u4be()?;
        self.type = Box::new(Metadata__TypeName::new(self.stream, self, _root)?);
        self.version = self.stream.read_u4be()?;
        self.nFields = self.stream.read_s4be()?;
        self.fields = vec!();
        for i in 0..self.n_fields {
            self.fields.append(Box::new(Metadata__RecordFieldDesc::new(self.stream, self, _root)?));
        }
        self.recordType = self.stream.read_s4be()?;
        self.values = vec!();
        for i in 0..self.n_fields {
            self.values.append(Box::new(Metadata__RecordFieldValue::new(self.stream, self, _root)?));
        }
    }
}

impl Metadata__RecordDesc {
}
#[derive(Default)]
pub struct Metadata__TableRecord {
    pub size: u32,
    pub type: Box<Metadata__TypeName>,
    pub version: u32,
    pub desc: Box<Metadata__RecordDesc>,
}

impl KaitaiStruct for Metadata__TableRecord {
    fn new<S: KaitaiStream>(stream: &mut S,
                            _parent: &Option<Box<KaitaiStruct>>,
                            _root: &Option<Box<KaitaiStruct>>)
                            -> Result<Self>
        where Self: Sized {
        let mut s: Self = Default::default();

        s.stream = stream;
        s.read(stream, _parent, _root)?;

        Ok(s)
    }


    fn read<S: KaitaiStream>(&mut self,
                             stream: &mut S,
                             _parent: &Option<Box<KaitaiStruct>>,
                             _root: &Option<Box<KaitaiStruct>>)
                             -> Result<()>
        where Self: Sized {
        self.size = self.stream.read_u4be()?;
        self.type = Box::new(Metadata__TypeName::new(self.stream, self, _root)?);
        self.version = self.stream.read_u4be()?;
        self.desc = Box::new(Metadata__RecordDesc::new(self.stream, self, _root)?);
    }
}

impl Metadata__TableRecord {
}
