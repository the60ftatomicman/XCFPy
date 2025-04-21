from enum import Enum
from src.basic.gimp_unit32 import gimp_uint32

class prop_tattoo:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 20:
            print("Expected type: [%s] but got [%s]" % (20,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.tattoo = gimp_uint32(fileIO).val
        if self.tattoo == 0:
            print("Expected tattoo to be greater than: [%s] but got [%s]" % (0,self.tattoo))
        print("Tattoo: [%s]" % (self.tattoo))
