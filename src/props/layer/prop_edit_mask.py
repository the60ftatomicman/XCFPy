from src.props.base import base
from src.basic.custom_enums import EDITING_MASK
from src.basic.gimp_unit32 import gimp_uint32

class prop_edit_mask(base):
    typecode    = 12
    payLoadSize = 4
    name        = "PROP_EDIT_MASK"

    def __init__(self, fileIO):
        super().__init__(fileIO,prop_edit_mask.name,prop_edit_mask.typecode,prop_edit_mask.payLoadSize)
        ##
        ##
        ##
        self.editMask = gimp_uint32(fileIO).val
        if self.editMask < 0 or self.editMask > 1:
            print("Expected edit mask boolean to be: [%s] or [%s] but got [%s]" % (0,1,self.applyMeditMaskask))
        self.editMask = EDITING_MASK(self.editMask)
        print("Edit Mask is: [%s]"%(self.editMask))

