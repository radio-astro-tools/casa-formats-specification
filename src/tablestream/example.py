from kaitaistruct import KaitaiStream
from metadata import Metadata

# Proof of concept example to print all the data manager name

with KaitaiStream(open("data/ea25_cal_small_before_fixed.split.ms/table.dat", "rb")) as _io:
    m = Metadata(_io)
    for manager in m.desc.table.columns.storage.managers:
        print(manager.cxx_type.value)