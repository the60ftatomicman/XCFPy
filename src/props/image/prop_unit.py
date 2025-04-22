from src.basic.gimp_uint32 import gimp_uint32
from src.props.base import base
from src.enums.unit_identifier import UNIT_IDENTIFIER

class prop_unit(base):
    typecode    = 22
    payLoadSize = 4
    name        = "PROP_UNIT"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_unit.name,prop_unit.typecode,prop_unit.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 1 or self.val > 4:
            print("Expected [%s] to be between: [%s] and [%s] but got [%s]" % (self.name,1,4,self.val))
        self.val = UNIT_IDENTIFIER(self.val)
        self.print_val()
