from src.props.base import base
from src.basic.gimp_uint32 import gimp_uint32

class prop_composite_mode(base):
    typecode    = 35
    payLoadSize = 4
    name        = "PROP_COMPOSITE_MODE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_composite_mode.name,prop_composite_mode.typecode,prop_composite_mode.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        # 4294967295 == negative!
        if self.val < 1 or self.val > 4 or self.val == 4294967295:
            print("Expected [%s] to be between: [%s] and [%s] but got [%s]" % (self.name,1,4,self.val))
        self.print_val()
