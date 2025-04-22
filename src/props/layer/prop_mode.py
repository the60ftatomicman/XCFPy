from src.basic.gimp_unit32 import gimp_uint32

class prop_mode:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 7:
            print("Expected type: [%s] but got [%s]" % (7,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.mode = gimp_uint32(fileIO).val
        if self.mode < 0 or self.mode > 61:
            print("Expected mode to be: [%s] or [%s] but got [%s]" % (0,1,self.mode))
        #self.mode = VISIBILITY(self.visible) #TODO -- huuuuge enum
        print("Mode is: [%s]"%(self.mode))
