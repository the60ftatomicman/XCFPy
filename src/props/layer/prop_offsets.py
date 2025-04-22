from src.props.base import base
from src.basic.gimp_unit32 import gimp_uint32

class prop_offsets(base):
    typecode    = 15
    payLoadSize = 8
    name        = "PROP_OFFSETS"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_offsets.name,prop_offsets.typecode,prop_offsets.payLoadSize)
        ##
        ##
        ##
        self.xOffset = gimp_uint32(fileIO).val
        self.yOffset = gimp_uint32(fileIO).val
        print("Offsets (x,y) are: [%s,%s]"%(self.xOffset,self.yOffset))

