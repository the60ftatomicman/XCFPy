from src.props.base import base
from src.enums.visibility import VISIBILITY
from src.basic.gimp_uint32 import gimp_uint32

class prop_show_mask(base):
    typecode    = 13
    payLoadSize = 4
    name        = "PROP_SHOW_MASK"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_show_mask.name,prop_show_mask.typecode,prop_show_mask.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 1:
            print("Expected [%s] to be: [%s] or [%s] but got [%s]" % (self.name,0,1,self.val))
        self.val = VISIBILITY(self.val)
        self.print_val()

