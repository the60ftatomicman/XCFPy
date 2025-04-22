from src.props.base import base

from src.basic.custom_enums import APPLY_MASK
from src.basic.gimp_unit32 import gimp_uint32

class prop_apply_mask(base):
    typecode    = 11
    payLoadSize = 4
    name        = "PROP_APPLY_MASK"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_apply_mask.name,prop_apply_mask.typecode,prop_apply_mask.payLoadSize)
        ##
        ##
        ##
        self.applyMask = gimp_uint32(fileIO).val
        if self.applyMask < 0 or self.applyMask > 1:
            print("Expected apply mask boolean to be: [%s] or [%s] but got [%s]" % (0,1,self.applyMask))
        self.applyMask = APPLY_MASK(self.applyMask)
        print("Apply Mask is: [%s]"%(self.applyMask))

