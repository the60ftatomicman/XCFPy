from src.props.base import base
from src.basic.custom_enums import COLOR_TAGS
from src.basic.gimp_unit32 import gimp_uint32

class prop_unit(base):
    typecode    = 22
    payLoadSize = 4
    name        = "PROP_UNIT"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_unit.name,prop_unit.typecode,prop_unit.payLoadSize)
        ##
        ##
        ##
        self.unitIdentifier = int.from_bytes(fileIO.read(4), byteorder='big')
        if self.unitIdentifier < 1 or self.unitIdentifier > 4:
            print("Expected unitIdentifier to be between: [%s] and [%s] but got [%s]" % (1,4,self.unitIdentifier))
        self.unitIdentifier = COLOR_TAGS(self.unitIdentifier)
        print("Units: [%s]"%(self.unitIdentifier))
