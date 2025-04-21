from enum import Enum
from src.basic.custom_enums import COLOR_TAGS
from src.basic.gimp_unit32 import gimp_uint32

class prop_color_tag:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 34:
            print("Expected type: [%s] but got [%s]" % (34,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.tag = gimp_uint32(fileIO).val
        if self.tag < 0 or self.tag > 8:
            print("Expected colotar tag to be between: [%s] or [%s] but got [%s]" % (0,8,self.tag))
        self.tag = COLOR_TAGS(self.tag)
        print("Color Tag is: [%s]"%(self.tag))

