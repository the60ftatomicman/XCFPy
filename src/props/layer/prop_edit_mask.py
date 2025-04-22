from src.props.base import base
from src.enums.mask import MASK
from src.basic.gimp_uint32 import gimp_uint32

class prop_edit_mask(base):
    typecode    = 12
    payLoadSize = 4
    name        = "PROP_EDIT_MASK"

    def __init__(self, fileIO):
        super().__init__(fileIO,prop_edit_mask.name,prop_edit_mask.typecode,prop_edit_mask.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 1:
            print("Expected [%s] to be: [%s] or [%s] but got [%s]" % (self.name,0,1,self.val))
        self.val = MASK(self.val)
        self.print_val()

