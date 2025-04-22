from src.basic.gimp_uint32 import gimp_uint32

class base:
    def __init__(self, fileIO,name,typecode,payLoadSize):
        self.name = name
        self.type = gimp_uint32(fileIO).val
        self.val  = None
        if self.type != typecode:
            print("Expected [%s] type: [%s] but got [%s]" % (self.name,typecode,self.type))
        if payLoadSize != None:
            self.payLoadSize = gimp_uint32(fileIO).val
            if self.payLoadSize != payLoadSize:
                print("Expected [%s] payloadSize: [%s] but got [%s]" % (self.name,payLoadSize,self.payLoadSize))
    def print_val(self):
        print("[%s] is: [%s]"%(self.name,self.val))

