from src.basic.custom_enums import LOCKED
from src.basic.gimp_unit32 import gimp_uint32

class prop_lock_position:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 32:
            print("Expected type: [%s] but got [%s]" % (32,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize != 4:
            print("Expected payloadSize: [%s] but got [%s]" % (4,self.payLoadSize))
        self.locked = gimp_uint32(fileIO).val
        if self.locked < 0 or self.locked > 8:
            print("Expected locked to be: [%s] or [%s] but got [%s]" % (0,1,self.locked))
        self.locked = LOCKED(self.locked)
        print("Locked Position is: [%s]"%(self.locked))

