
from src.basic.gimp_unit32 import gimp_uint32
from src.basic.gimp_float import gimp_float

class prop_resolution:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 19:
            print("Expected type: [%s] but got [%s]" % (19,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 8:
            print("Expected payloadSize: [%s] but got [%s]" % (1,self.payLoadSize))
        self.hres = gimp_float(fileIO).val
        self.vres = gimp_float(fileIO).val
        print("HRES [%s] VRES [%s]"%(self.hres,self.vres))