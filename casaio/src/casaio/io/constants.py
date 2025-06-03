# Map dictionary of c++ based manager name to katitai manager class
import numpy as np

manager_list = {
        "StandardStMan": {
            "module": "standard",
            "package": "StandardStorageManager"
        },
        "TiledShapeStMan": {
            "module": "tiled",
            "package": "TiledShapeStorageManager"
        },
        "TiledColumnStMan": {
            "module": "tiled",
            "package": "TiledColumnStorageManager"
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

# Until the full set of objects is done I want a text list as a hold over for the view tables
casacore_data_types_list = {
    0: "bool",
    1: "char",
    2: "uchar",
    3: "short",
    4: "ushort",
    5: "int32",
    6: "uint32",
    7: "float32",
    8: "float64",
    9: "complx64",
    10: "complex128",
    11: "string",
    12: "table",
    13: "array[bool]",
    14: "array[char]",
    15: "array[uchar]",
    16: "array[short]",
    17: "array[ushort]",
    18: "array[int]",
    19: "array[uint]",
    20: "array[float]",
    21: "array[double]",
    22: "array[complex]",
    23: "array[dcomplex]",
    24: "array[string]",
    25: "record",
    26: "other",
    27: "quantity",
    28: "array[quantity]",
    29: "int64",
    30: "array[int64]"
}
