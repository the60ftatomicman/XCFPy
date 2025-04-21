from enum import Enum
from src.basic.gimp_unit32 import gimp_uint32

class prop_active_layer:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 2:
            print("Expected type: [%s] but got [%s]" % (2,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 0:
            print("Expected payloadSize: [%s] but got [%s]" % (0,self.payLoadSize))
