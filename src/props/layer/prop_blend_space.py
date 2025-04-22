from src.props.base import base
from src.basic.gimp_unit32 import gimp_uint32

class prop_blend_space(base):
    typecode    = 37
    payLoadSize = 4
    name        = "PROP_BLEND_SPACE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_blend_space.name,prop_blend_space.typecode,prop_blend_space.payLoadSize)
        ##
        ##
        ##
        self.space = gimp_uint32(fileIO).val
        if self.space < 1 or self.space > 4:
            print("Expected space to be: [%s] or [%s] but got [%s]" % (0,1,self.space))
        #self.mode = VISIBILITY(self.visible) #TODO -- huuuuge enum
        print("Space is: [%s]"%(self.space))
