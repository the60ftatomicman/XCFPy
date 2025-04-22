from src.props.base import base
from src.basic.gimp_uint32 import gimp_uint32

class prop_opacity(base):
    typecode    = 6
    payLoadSize = 4
    name        = "PROP_BLEND_SPACE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_opacity.name,prop_opacity.typecode,prop_opacity.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 255:
            print("Expected [%s] to be between: [%s] and [%s] but got [%s]" % (self.name,0,255,self.val))
        self.print_val()
