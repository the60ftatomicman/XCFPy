from enum import Enum

class COMPRESSION_INDICATOR(Enum):
    NO_COMPRESSION   = 0
    RLE_ENCODING     = 1
    ZLIB_COMPRESSION = 2
    FRACTAL_UNUSED   = 3