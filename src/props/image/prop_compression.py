from src.props.base import base
from src.basic.custom_enums import COMPRESSION_INDICATOR
from src.basic.gimp_unit32 import gimp_uint32

class prop_compression(base):
    typecode    = 17
    payLoadSize = 1
    name        = "PROP_COMPRESSION"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_compression.name,prop_compression.typecode,prop_compression.payLoadSize)
        ##
        ##
        ##
        self.compressionIndicator = int.from_bytes(fileIO.read(1), byteorder='big')
        if self.compressionIndicator < 0 or self.compressionIndicator > 3:
            print("Expected compressionIndicator to be between: [%s] and [%s] but got [%s]" % (0,3,self.compressionIndicator))
        self.compressionIndicator = COMPRESSION_INDICATOR(self.compressionIndicator)
        print("COMPRESSION [%s]"%(self.compressionIndicator))
