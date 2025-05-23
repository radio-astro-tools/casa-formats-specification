# Map dictionary of c++ based manager name to katitai manager class
import numpy as np

manager_list = {
        "StandardStMan": {
            "module": "standard_storage_manager",
            "package": "StandardStorageManager"
        },
        "TiledShapeStMan": {
            "module": "tiled",
            "package": "TiledShapeStorageManager"
        }
}


# This defines the CASA MS DataTypes
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

casacore_data_types = {
    0: np.bool,
    1: np.char,
###   2           TpUChar
    3: np.short,
    4: np.ushort,
    5: np.int32,
    6: np.uint32,
    7: np.float32,
    8: np.float64,
    9: np.complex64,
    10: np.complex128,
    11: str,
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
    29: np.int64
###   30          TpArrayInt64

}
