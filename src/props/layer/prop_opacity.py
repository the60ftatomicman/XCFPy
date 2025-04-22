from src.props.base import base
from src.basic.gimp_unit32 import gimp_uint32

class prop_opacity(base):
    typecode    = 6
    payLoadSize = 4
    name        = "PROP_BLEND_SPACE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_opacity.name,prop_opacity.typecode,prop_opacity.payLoadSize)
        ##
        ##
        ##
        self.opacity = gimp_uint32(fileIO).val
        if self.opacity < 0 or self.opacity > 255:
            print("Expected opacity to be between: [%s] and [%s] but got [%s]" % (0,255,self.opacity))
        print("Opacity is: [%s]"%(self.opacity))
