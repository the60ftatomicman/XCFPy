# https://developer.gimp.org/core/standards/xcf/#the-hierarchy-structure
from math                   import ceil
from src.basic.gimp_string  import gimp_string
from src.basic.gimp_uint32  import gimp_uint32

class level:
    def __init__(self, fileIO,byteLocation):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        print("Jumped to position: %s" % (fileIO.tell()))
        self.width         = gimp_uint32(fileIO).val
        self.height        = gimp_uint32(fileIO).val
        self.tileCount     = ceil(self.width/64)*ceil(self.height/64)
        print("---- Level ----")
        print("-- Width x Height [%s x %s] " % (self.width,self.height))
        print("-- tiles [%s] " % (self.tileCount))