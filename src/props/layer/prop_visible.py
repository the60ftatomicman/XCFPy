from enum import Enum
from src.basic.custom_enums import VISIBILITY
from src.basic.gimp_unit32 import gimp_uint32

class prop_visible:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 8:
            print("Expected type: [%s] but got [%s]" % (8,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.visible = gimp_uint32(fileIO).val
        if self.visible < 0 or self.visible > 1:
            print("Expected opacity to be: [%s] or [%s] but got [%s]" % (0,1,self.visible))
        self.visible = VISIBILITY(self.visible)
        print("Visibility is: [%s]"%(self.visible))
