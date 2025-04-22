from src.props.base import base
from src.enums.mask import MASK
from src.basic.gimp_uint32 import gimp_uint32

class prop_apply_mask(base):
    typecode    = 11
    payLoadSize = 4
    name        = "PROP_APPLY_MASK"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_apply_mask.name,prop_apply_mask.typecode,prop_apply_mask.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 1:
            print("Expected apply mask boolean to be: [%s] or [%s] but got [%s]" % (0,1,self.val))
        self.val = MASK(self.val)
        self.print_val()

