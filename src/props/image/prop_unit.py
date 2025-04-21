from enum import Enum
from src.basic.custom_enums import COLOR_TAGS
from src.basic.gimp_unit32 import gimp_uint32

class prop_unit:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 22:
            print("Expected type: [%s] but got [%s]" % (22,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.unitIdentifier = int.from_bytes(fileIO.read(4), byteorder='big')
        if self.unitIdentifier < 1 or self.unitIdentifier > 4:
            print("Expected unitIdentifier to be between: [%s] and [%s] but got [%s]" % (1,4,self.unitIdentifier))
        self.unitIdentifier = COLOR_TAGS(self.unitIdentifier)
        print("Units: [%s]"%(self.unitIdentifier))
