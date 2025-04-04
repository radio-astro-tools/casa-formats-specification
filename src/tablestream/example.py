import numpy as np
from kaitaistruct import KaitaiStream
from python.metadata import Metadata
from python.common import Common
from python.regular_table_description import RegularTableDescription
from python.table_incremental_store import TableIncrementalStore


def get_table_description(is_regular_table=False):
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms"
                "/table.dat", "rb")) as _io:
        common_stream = Common(_io)

        if is_regular_table:
            _io.seek(common_stream.stream_position)
            regular_table_desc = RegularTableDescription(_io=_io)

        return regular_table_desc


# Proof of concept example to print all the data manager name
def get_managers():
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms"
                "/table.dat", "rb")) as _io:
        m = Metadata(_io)

        for manager in m.desc.table.columns.column_set.managers:
            print(manager.cxx_type.value)


def get_column_info(column):
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms"
                "/table.dat", "rb")) as _io:
        m = Metadata(_io)

        for info in m.desc.table.columns.column_info:
            if info.column_name.value == column:
                print(f"Found in table.f{info.manager_number}")
                return

        print(f"Column={column} not found.")


def get_manager_info():
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms"
                "/table.dat", "rb")) as _io:
        m = Metadata(_io)

        for i, info in enumerate(m.desc.table.columns.dminfo):
            if info.type.value == "ISM":
                print(f"Column [{i}]: {info.column_offset.name.value}: idk: {info.column_offset.idk}")

            elif info.type.value == "SSM":
                print(f"Column [{i}]: {info.column_offset.name.value}")
                print(f"\tn_rows: {info.column_offset.column_offset.n_rows}")
                print(f"\tname: {info.column_offset.column_offset.name.value}")
                print(f"\tsize: {info.column_offset.column_offset.size}")

                for i, element in enumerate(info.column_offset.column_offset.elements):
                    print(f"\telement: [{i}] {element}")


def get_data():
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms"
                "/table.f10", "rb")) as _io:
        table = TableIncrementalStore(_io)
        print(f"Number of bucket: {table.header.num_buckets} (size: {table.header.bucket_size})")

        for bucket in table.data:
            print(f"data:\n{bucket.data}")


def get_index():
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms"
                "/table.f10", "rb")) as _io:
        table = TableIncrementalStore(_io)
        print(f"Number of bucket: {table.header.num_buckets} (size: {table.header.bucket_size})")

        for bucket in table.data:
            print(f"data:\n{bucket.index}")


def get_column_description(column):
    table_desc = get_table_description(is_regular_table=True)

    for i, desc in enumerate(table_desc.desc.columns.column_desc):
        if desc.name.value == column:
            return desc


def get_scan_numbers():
    values = []
    indices = []
    elements = []

    filename = ("/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms"
                "/table.f10")
    with KaitaiStream(open(filename, "rb")) as _io:
        column_desc = get_column_description("SCAN_NUMBER")
        table = TableIncrementalStore(_io=_io, stream=column_desc)
        print(f"{column_desc.data_type}")

        for entry in table.data:
            values.append(entry.values)
            indices.append(entry.index)

        for element in table.index_set.row_number.elements:
            elements.append(element)
        #indices = type(table.data.index)

        indices[0].append(36580)  # This is a hack till I can get it properly.

        #return np.repeat(np.squeeze(values), np.diff(indices[0]))
        return values



