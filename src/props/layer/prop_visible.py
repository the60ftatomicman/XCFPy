from src.props.base import base
from src.basic.custom_enums import VISIBILITY
from src.basic.gimp_unit32 import gimp_uint32

class prop_visible(base):
    typecode    = 8
    payLoadSize = 4
    name        = "PROP_VISIBLE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_visible.name,prop_visible.typecode,prop_visible.payLoadSize)
        ##
        ##
        ##
        self.visible = gimp_uint32(fileIO).val
        if self.visible < 0 or self.visible > 1:
            print("Expected opacity to be: [%s] or [%s] but got [%s]" % (0,1,self.visible))
        self.visible = VISIBILITY(self.visible)
        print("Visibility is: [%s]"%(self.visible))
