from src.basic.custom_enums import APPLY_MASK
from src.basic.gimp_unit32 import gimp_uint32

class prop_apply_mask:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 42:
            print("Expected type: [%s] but got [%s]" % (42,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.applyMask = gimp_uint32(fileIO).val
        if self.applyMask < 0 or self.applyMask > 1:
            print("Expected apply mask boolean to be: [%s] or [%s] but got [%s]" % (0,1,self.applyMask))
        self.applyMask = APPLY_MASK(self.applyMask)
        print("Apply Mask is: [%s]"%(self.applyMask))

