from src.basic.gimp_unit32 import gimp_uint32

class prop_blend_space:
    typecode    = 37
    payLoadSize = 4
    name        = "PROP_COLOR_TAG"
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type !=prop_blend_space.typecode:
            print("Expected type: [%s] but got [%s]" % (prop_blend_space.typecode,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != prop_blend_space.payLoadSize:
            print("Expected payloadSize: [%s] but got [%s]" % (prop_blend_space.payLoadSize,self.payLoadSize))
        self.space = gimp_uint32(fileIO).val
        if self.space < 1 or self.space > 4:
            print("Expected space to be: [%s] or [%s] but got [%s]" % (0,1,self.space))
        #self.mode = VISIBILITY(self.visible) #TODO -- huuuuge enum
        print("Space is: [%s]"%(self.space))
