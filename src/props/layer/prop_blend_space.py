from src.props.base import base
from src.basic.gimp_int32 import gimp_int32

class prop_blend_space(base):
    typecode    = 37
    payLoadSize = 4
    name        = "PROP_BLEND_SPACE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_blend_space.name,prop_blend_space.typecode,prop_blend_space.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_int32(fileIO).val
        if self.val < 1 or self.val > 4:
            print("Expected [%s] to be: [%s] or [%s] but got [%s]" % (self.name,1,4,self.val))
        self.print_val()
