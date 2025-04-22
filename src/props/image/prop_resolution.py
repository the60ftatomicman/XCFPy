from src.props.base import base
from src.basic.gimp_unit32 import gimp_uint32
from src.basic.gimp_float import gimp_float

class prop_resolution(base):
    typecode    = 19
    payLoadSize = 8
    name        = "PROP_RESOLUTION"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_resolution.name,prop_resolution.typecode,prop_resolution.payLoadSize)
        ##
        ##
        ##
        self.hres = gimp_float(fileIO).val
        self.vres = gimp_float(fileIO).val
        print("HRES [%s] VRES [%s]"%(self.hres,self.vres))