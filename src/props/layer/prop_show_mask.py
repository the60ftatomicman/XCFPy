from src.basic.custom_enums import VISIBILITY
from src.basic.gimp_unit32 import gimp_uint32

class prop_show_mask:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 13:
            print("Expected type: [%s] but got [%s]" % (13,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.visibility = gimp_uint32(fileIO).val
        if self.visibility < 0 or self.visibility > 1:
            print("Expected show mask boolean to be: [%s] or [%s] but got [%s]" % (0,1,self.visibility))
        self.visibility = VISIBILITY(self.visibility)
        print("Show Mask is: [%s]"%(self.visibility))

