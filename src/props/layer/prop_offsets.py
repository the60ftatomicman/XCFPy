from src.basic.custom_enums import VISIBILITY
from src.basic.gimp_unit32 import gimp_uint32

class prop_offsets:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 15:
            print("Expected type: [%s] but got [%s]" % (15,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 8:
            print("Expected payloadSize: [%s] but got [%s]" % (8,self.payLoadSize))
        self.xOffset = gimp_uint32(fileIO).val
        self.yOffset = gimp_uint32(fileIO).val
        print("Offsets (x,y) are: [%s,%s]"%(self.xOffset,self.yOffset))

