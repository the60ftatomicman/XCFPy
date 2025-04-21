from enum import Enum

class APPLY_MASK(Enum):
    NO_APPLY = 0
    APPLY    = 1

class EDITING_MASK(Enum):
    NO_APPLY = 0
    APPLY    = 1

class COLOR_TAGS(Enum):
    NONE   = 0
    BLUE   = 1
    GREEN  = 2
    YELLOW = 3
    ORANGE = 4
    BROWN  = 5
    RED    = 6
    VIOLET = 7
    GRAY   = 8

class COMPRESSION_INDICATOR(Enum):
    NO_COMPRESSION   = 0
    RLE_ENCODING     = 1
    ZLIB_COMPRESSION = 2
    FRACTAL_UNUSED   = 3

class LOCKED(Enum):
    UNLOCKED = 0
    LOCKED   = 1

class VISIBILITY(Enum):
    INVISIBLE = 0
    VISIBLE   = 1

class UNIT_IDENTIFIER(Enum):
    INCHES      = 1
    MILLIMETERS = 2
    POINTS      = 3
    PICAS       = 4