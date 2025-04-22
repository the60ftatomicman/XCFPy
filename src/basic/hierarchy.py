# https://developer.gimp.org/core/standards/xcf/#the-hierarchy-structure
from src.basic.gimp_uint32  import gimp_uint32
from src.basic.gimp_pointer import gimp_pointer
from src.basic.level        import level

class hierarchy:
    def __init__(self, fileIO,byteLocation):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        print("Jumped to position: %s" % (fileIO.tell()))
        self.width         = gimp_uint32(fileIO).val
        self.height        = gimp_uint32(fileIO).val
        self.bytesPerPixel = gimp_uint32(fileIO).val
        print("---- Hierarchy ----")
        print("-- Width x Height [%s x %s] " % (self.width,self.height))
        print("-- BPP [%s] " % (self.bytesPerPixel))

        levelStructure = level(fileIO,gimp_pointer(fileIO).val)