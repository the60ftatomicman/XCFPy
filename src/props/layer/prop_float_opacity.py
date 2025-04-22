from src.props.base import base
from src.basic.gimp_float import gimp_float

class prop_float_opacity(base):
    typecode    = 33
    payLoadSize = 4
    name        = "PROP_FLOAT_OPACITY"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_float_opacity.name,prop_float_opacity.typecode,prop_float_opacity.payLoadSize)
        ##
        ##
        ##
        self.opacity = gimp_float(fileIO).val
        # TODO -- fix the odd issue with this
        #if self.opacity < 0.0 or self.opacity > 1.0:
        #    print("Expected float opacity to be between: [%s] and [%s] but got [%s]" % (0,255,self.opacity))
        print("Float Opacity is: [%s]"%(self.opacity))
