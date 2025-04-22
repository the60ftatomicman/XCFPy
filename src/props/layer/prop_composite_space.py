from src.props.base import base
from src.basic.gimp_uint32 import gimp_uint32

class prop_composite_space(base):
    typecode    = 36
    payLoadSize = 4
    name        = "PROP_COMPOSITE_SPACE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_composite_space.name,prop_composite_space.typecode,prop_composite_space.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 1 or self.val > 4:
            print("Expected [%s] to be: [%s] or [%s] but got [%s]" % (self.name,1,4,self.val))
        #TODO -- this is NOT pulling properly.
        #self.space = COMPOSITE_SPACE(self.space)
        self.print_val()
