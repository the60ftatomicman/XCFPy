from enum import Enum
from src.basic.custom_enums import COMPRESSION_INDICATOR
from src.basic.gimp_unit32 import gimp_uint32

class prop_compression:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 17:
            print("Expected type: [%s] but got [%s]" % (17,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 1:
            print("Expected payloadSize: [%s] but got [%s]" % (1,self.payLoadSize))
        self.compressionIndicator = int.from_bytes(fileIO.read(1), byteorder='big')
        if self.compressionIndicator < 0 or self.compressionIndicator > 3:
            print("Expected compressionIndicator to be between: [%s] and [%s] but got [%s]" % (0,3,self.compressionIndicator))
        self.compressionIndicator = COMPRESSION_INDICATOR(self.compressionIndicator)
        print("COMPRESSION [%s]"%(self.compressionIndicator))
