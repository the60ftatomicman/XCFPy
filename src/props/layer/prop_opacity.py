from src.basic.gimp_unit32 import gimp_uint32

class prop_opacity:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 6:
            print("Expected type: [%s] but got [%s]" % (6,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.opacity = gimp_uint32(fileIO).val
        if self.opacity < 0 or self.opacity > 255:
            print("Expected opacity to be between: [%s] and [%s] but got [%s]" % (0,255,self.opacity))
        print("Opacity is: [%s]"%(self.opacity))
