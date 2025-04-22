from src.props.base import base
from src.basic.gimp_int32 import gimp_int32

class prop_offsets(base):
    typecode    = 15
    payLoadSize = 8
    name        = "PROP_OFFSETS"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_offsets.name,prop_offsets.typecode,prop_offsets.payLoadSize)
        ##
        ##
        ##
        xOffset = gimp_int32(fileIO).val
        yOffset = gimp_int32(fileIO).val
        self.val = [xOffset,yOffset]
        self.print_val()

    def print_val(self):
        print("[%s] are: x [%s] y [%s]"%(self.name,self.val[0],self.val[1]))

