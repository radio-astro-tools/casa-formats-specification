from kaitaistruct import KaitaiStream
from python.metadata import Metadata
from python.table_incremental_store import TableIncrementalStore


# Proof of concept example to print all the data manager name

def get_managers():
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms/table.dat",
                "rb")) as _io:
        m = Metadata(_io)

        for manager in m.desc.table.columns.column_set.managers:
            print(manager.cxx_type.value)


def get_column_info(column):
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms/table.dat",
                "rb")) as _io:
        m = Metadata(_io)

        for info in m.desc.table.columns.column_info:
            if info.column_name.value == column:
                print(f"Found in table.f{info.manager_number}")
                return

        print(f"Column={column} not found.")


def get_manager_info():
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms/table.dat",
                "rb")) as _io:
        m = Metadata(_io)

        for info in m.desc.table.columns.dminfo:
            if info.type.value == "ISM":
                print(f"Column: {info.column_offset.name.value}: idk: {info.column_offset.idk}")

            elif info.type.value == "SSM":
                print(f"Column: {info.column_offset.name.value}")
                print(f"\tn_rows: {info.column_offset.column_offset.n_rows}")
                print(f"\tname: {info.column_offset.column_offset.name.value}")
                print(f"\tsize: {info.column_offset.column_offset.size}")

                for i, element in enumerate(info.column_offset.column_offset.elements):
                    print(f"\telement: [{i}] {element}")


def get_data():
    with KaitaiStream(
            open(
                "/users/jhoskins/fornax/Development/casa-formats-specification/ea25_cal_small_before_fixed.split.ms/table.f10",
                "rb")) as _io:

        table = TableIncrementalStore(_io)
        print(f"Number of bucket: {table.header.num_buckets} (size: {table.header.bucket_size})")

        for bucket in table.data:
            print(f"data:\n{bucket.data}")
