from src.props.base import base
from src.basic.custom_enums import COLOR_TAGS
from src.basic.gimp_unit32 import gimp_uint32

class prop_color_tag(base):
    typecode    = 34
    payLoadSize = 4
    name        = "PROP_COLOR_TAG"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_color_tag.name,prop_color_tag.typecode,prop_color_tag.payLoadSize)
        ##
        ##
        ##
        self.tag = gimp_uint32(fileIO).val
        if self.tag < 0 or self.tag > 8:
            print("Expected colotar tag to be between: [%s] or [%s] but got [%s]" % (0,8,self.tag))
        self.tag = COLOR_TAGS(self.tag)
        print("Color Tag is: [%s]"%(self.tag))

