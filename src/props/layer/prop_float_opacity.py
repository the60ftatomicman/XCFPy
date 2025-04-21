from src.basic.gimp_unit32 import gimp_uint32
from src.basic.gimp_float import gimp_float

class prop_float_opacity:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 33:
            print("Expected type: [%s] but got [%s]" % (33,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.opacity = gimp_float(fileIO).val
        # TODO -- fix the odd issue with this
        #if self.opacity < 0.0 or self.opacity > 1.0:
        #    print("Expected float opacity to be between: [%s] and [%s] but got [%s]" % (0,255,self.opacity))
        print("Float Opacity is: [%s]"%(self.opacity))
