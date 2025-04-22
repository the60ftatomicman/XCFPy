from src.props.base import base
from src.basic.gimp_unit32 import gimp_uint32

class prop_tattoo(base):
    typecode    = 20
    payLoadSize = 4
    name        = "PROP_TATTOO"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_tattoo.name,prop_tattoo.typecode,prop_tattoo.payLoadSize)
        ##
        ##
        ##
        self.tattoo = gimp_uint32(fileIO).val
        if self.tattoo == 0:
            print("Expected tattoo to be greater than: [%s] but got [%s]" % (0,self.tattoo))
        print("Tattoo: [%s]" % (self.tattoo))
