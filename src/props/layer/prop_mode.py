from src.props.base import base
from src.basic.gimp_unit32 import gimp_uint32

class prop_mode(base):
    typecode    = 7
    payLoadSize = 4
    name        = "PROP_MODE"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_mode.name,prop_mode.typecode,prop_mode.payLoadSize)
        ##
        ##
        ##
        self.mode = gimp_uint32(fileIO).val
        if self.mode < 0 or self.mode > 61:
            print("Expected mode to be: [%s] or [%s] but got [%s]" % (0,1,self.mode))
        #self.mode = VISIBILITY(self.visible) #TODO -- huuuuge enum
        print("Mode is: [%s]"%(self.mode))
