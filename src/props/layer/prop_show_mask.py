from src.props.base import base
from src.basic.custom_enums import VISIBILITY
from src.basic.gimp_unit32 import gimp_uint32

class prop_show_mask(base):
    typecode    = 13
    payLoadSize = 4
    name        = "PROP_SHOW_MASK"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_show_mask.name,prop_show_mask.typecode,prop_show_mask.payLoadSize)
        ##
        ##
        ##
        self.visibility = gimp_uint32(fileIO).val
        if self.visibility < 0 or self.visibility > 1:
            print("Expected show mask boolean to be: [%s] or [%s] but got [%s]" % (0,1,self.visibility))
        self.visibility = VISIBILITY(self.visibility)
        print("Show Mask is: [%s]"%(self.visibility))

