from src.props.base import base
from src.enums.visibility import VISIBILITY
from src.basic.gimp_uint32 import gimp_uint32

class prop_visible(base):
    typecode    = 8
    payLoadSize = 4
    name        = "PROP_VISIBLE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_visible.name,prop_visible.typecode,prop_visible.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 1:
            print("Expected [%s] to be: [%s] or [%s] but got [%s]" % (self.name,0,1,self.val))
        self.val = VISIBILITY(self.val)
        self.print_val()
