from src.basic.custom_enums import EDITING_MASK
from src.basic.gimp_unit32 import gimp_uint32

class prop_edit_mask:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 12:
            print("Expected type: [%s] but got [%s]" % (12,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.editMask = gimp_uint32(fileIO).val
        if self.editMask < 0 or self.editMask > 1:
            print("Expected edit mask boolean to be: [%s] or [%s] but got [%s]" % (0,1,self.applyMeditMaskask))
        self.editMask = EDITING_MASK(self.editMask)
        print("Edit Mask is: [%s]"%(self.editMask))

