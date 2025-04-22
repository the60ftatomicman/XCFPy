from enum import Enum

class LAYER_COLOR_MODE(Enum):
    RGB_NO_ALPHA         = 0
    RGB_WITH_ALPHA       = 1
    GRAYSCALE_NO_ALPHA   = 2
    GRAYSCALE_WITH_ALPHA = 3
    INDEXED_NO_ALPHA     = 4
    INDEX_WITH_ALPHA     = 5