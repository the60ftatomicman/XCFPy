from src.props.base import base
from src.enums.linked import LINKED
from src.basic.gimp_uint32 import gimp_uint32

class prop_linked(base):
    typecode    = 9
    payLoadSize = 4
    name        = "PROP_LINKED"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_linked.name,prop_linked.typecode,prop_linked.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 1:
            print("Expected linked to be: [%s] or [%s] but got [%s]" % (0,1,self.val))
        self.val = LINKED(self.val)
        self.print_val()
