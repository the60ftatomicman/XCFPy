from src.basic.gimp_unit32 import gimp_uint32

class base:
    def __init__(self, fileIO,name,typecode,payLoadSize):
        self.name = name
        self.type = gimp_uint32(fileIO).val
        if self.type != typecode:
            print("Expected type: [%s] but got [%s]" % (typecode,self.type))
        if payLoadSize != None:
            self.payLoadSize = gimp_uint32(fileIO).val
            if self.payLoadSize != payLoadSize:
                print("Expected payloadSize: [%s] but got [%s]" % (payLoadSize,self.payLoadSize))
