from src.props.base import base
from src.enums.layer_mode import LAYER_MODE
from src.basic.gimp_uint32 import gimp_uint32

class prop_mode(base):
    typecode    = 7
    payLoadSize = 4
    name        = "PROP_MODE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_mode.name,prop_mode.typecode,prop_mode.payLoadSize)
        ##
        ##
        ##
        #if prop_mode.oldMode:
        #    self.mode = 0
        #else:
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 61:
            print("Expected mode to be: [%s] or [%s] but got [%s]" % (0,61,self.val))
        self.val = LAYER_MODE(self.val)
        self.print_val()
