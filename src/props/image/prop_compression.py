from src.props.base import base
from src.enums.compression_indicator import COMPRESSION_INDICATOR

class prop_compression(base):
    typecode    = 17
    payLoadSize = 1
    name        = "PROP_COMPRESSION"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_compression.name,prop_compression.typecode,prop_compression.payLoadSize)
        ##
        ##
        ##
        self.val = int.from_bytes(fileIO.read(1), byteorder='big')
        if self.val < 0 or self.val > 3:
            print("Expected compressionIndicator to be between: [%s] and [%s] but got [%s]" % (0,3,self.val))
        self.val = COMPRESSION_INDICATOR(self.val)
        self.print_val()
