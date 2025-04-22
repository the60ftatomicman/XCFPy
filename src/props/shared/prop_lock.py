from src.props.base import base
from src.enums.lock_unlock import LOCK_UNLOCK
from src.basic.gimp_uint32 import gimp_uint32

## ----------
## Core Class
## ----------
class prop_lock(base):
    payLoadSize = 4
    def __init__(self, fileIO,name,typecode):
        super().__init__(fileIO,name,typecode,prop_lock.payLoadSize)
        ##
        ##
        ##
        self.val = gimp_uint32(fileIO).val
        if self.val < 0 or self.val > 1:
            print("Expected [%s] to be: [%s] or [%s] but got [%s]" % (0,1,self.val))
        self.val = LOCK_UNLOCK(self.val)
        self.print_val()

## ----------
## Child Classes
## ----------

class prop_lock_alpha(prop_lock):
    typecode    = 10
    name        = "PROP_LOCK_ALPHA"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_lock_alpha.name,prop_lock_alpha.typecode)

class prop_lock_content(prop_lock):
    typecode    = 28
    name        = "PROP_LOCK_CONTENT"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_lock_content.name,prop_lock_content.typecode)

class prop_lock_position(prop_lock):
    typecode    = 32
    name        = "PROP_LOCK_POSITION"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_lock_position.name,prop_lock_position.typecode)

class prop_lock_visibility(prop_lock):
    typecode    = 42
    name        = "PROP_LOCK_VISIBILITY"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_lock_visibility.name,prop_lock_visibility.typecode)




