from src.props.base import base
from src.basic.custom_enums import LOCKED
from src.basic.gimp_unit32 import gimp_uint32

class prop_lock_alpha(base):
    typecode    = 10
    payLoadSize = 4
    name        = "PROP_LOCK_ALPHA"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_lock_alpha.name,prop_lock_alpha.typecode,prop_lock_alpha.payLoadSize)
        ##
        ##
        ##
        self.locked = gimp_uint32(fileIO).val
        if self.locked < 0 or self.locked > 8:
            print("Expected locked to be: [%s] or [%s] but got [%s]" % (0,1,self.locked))
        self.locked = LOCKED(self.locked)
        print("Locked Alpha is: [%s]"%(self.locked))

