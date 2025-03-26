import numpy as np

from kaitaistruct import KaitaiStream

from python.metadata import Metadata
from python.common import Common
from python.regular_table_description import RegularTableDescription
from python.tiled_shape_storage_manager import TiledShapeStorageManager

def get_data(filename):
    values = []
    indices = []
    elements = []

    with KaitaiStream(open(filename, "rb")) as _io:
        column_desc = get_column_description("DATA")
        #table = TableIncrementalStore(_io=_io, stream=column_desc)

        return column_desc

def get_column_description(column):
    table_desc = get_table_description(is_regular_table=True)

    for i, desc in enumerate(table_desc.desc.columns.column_desc):
        if desc.name.value == column:
            return desc

def get_table_description(is_regular_table=False):
    with KaitaiStream(
            open(
                "/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.split.ms"
                "/table.dat", "rb")) as _io:
        common_stream = Common(_io)

        if is_regular_table:
            _io.seek(common_stream.stream_position)
            regular_table_desc = RegularTableDescription(_io=_io)

        return regular_table_desc
def get_info(name="DATA", is_regular_table=True):
    with KaitaiStream(
            open(
                "/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.split.ms"
                "/table.dat", "rb")) as _io:
        common_stream = Common(_io)

        if is_regular_table:
            _io.seek(common_stream.stream_position)
            regular_table_desc = RegularTableDescription(_io=_io)

        for i, entry in enumerate(regular_table_desc.desc.columns.column_info):
            if entry.column_name.value == name:
                print(f"name: {name}, sequence: {entry.manager_number}")

                sequence_number = entry.manager_number
    file = f"/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.split.ms/table.f{sequence_number}"
    with KaitaiStream(
            open(f"/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.split.ms/table.f{sequence_number}", "rb")) as _io:

        print(f"file: {file}")
        tiled_manager = TiledShapeStorageManager(_io)

        print(f"size: {tiled_manager.cube_index.size}")
        print(f"n_rows: {tiled_manager.cube_index.n_rows}")

        for element in tiled_manager.cube_index.elements:
            print(f"cube: {element}")

        print(f"default: {tiled_manager.default_tile_shape.elements}")
        print(f"tsm indicies: {np.unique(tiled_manager.cube_index.elements)}")