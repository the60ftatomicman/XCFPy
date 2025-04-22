from src.props.base import base
from src.enums.color_tags import COLOR_TAGS
from src.basic.gimp_uint32 import gimp_uint32

class prop_color_tag(base):
    typecode    = 34
    payLoadSize = 4
    name        = "PROP_COLOR_TAG"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_color_tag.name,prop_color_tag.typecode,prop_color_tag.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 8:
            print("Expected [%s] to be between: [%s] or [%s] but got [%s]" % (self.name,0,8,self.val))
        self.val = COLOR_TAGS(self.val)
        self.print_val()

