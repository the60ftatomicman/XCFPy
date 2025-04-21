from enum import Enum
from src.basic.gimp_unit32 import gimp_uint32

class prop_end:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 0:
            print("Expected type: [%s] but got [%s]" % (0,self.type))
        self.end_byte = gimp_uint32(fileIO).val
        if self.end_byte != 0:
            print("Expected a second: [%s] but got [%s]" % (0,self.end_byte))
