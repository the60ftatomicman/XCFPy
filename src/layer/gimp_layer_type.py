from enum import Enum

class LayerColorMode(Enum):
    RGB_NO_ALPHA         = 0
    RGB_WITH_ALPHA       = 1
    GRAYSCALE_NO_ALPHA   = 2
    GRAYSCALE_WITH_ALPHA = 3
    INDEXED_NO_ALPHA     = 4
    INDEX_WITH_ALPHA     = 5


class gimp_layer_type:
    def __init__(self, fileIO):
        self.raw = fileIO.read(4)
        self.val = int.from_bytes(self.raw, byteorder='big')
        if self.val < 0 or self.val > 5:
            print("Expected layer color mode to be between: [%s] and [%s] but got [%s]" % (0,5,self.val))
        self.val = LayerColorMode(self.val)
