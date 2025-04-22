from src.props.base import base
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
        hres = gimp_float(fileIO).val ## TODO -- fix float
        vres = gimp_float(fileIO).val
        self.val = [hres,vres]
        self.print_val()

    def print_val(self):
        print("[%s] is: HRES [%s] VRES [%s]"%(self.name,self.val[0],self.val[1]))