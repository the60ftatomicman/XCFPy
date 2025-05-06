# https://developer.gimp.org/core/standards/xcf/#the-hierarchy-structure
# https://github.com/FHPythonUtils/GimpFormats/blob/26ee17287e694777b0e8df17aee1a4b8cf9fe8e4/xcfSpec.txt#L276
from src.basic.gimp_uint32  import gimp_uint32
from src.basic.gimp_pointer import gimp_pointer
from src.basic.level        import level

class hierarchy:
    def __init__(self, fileIO, byteLocation):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        print("Jumped to position: %s" % (fileIO.tell()))
        self.width         = gimp_uint32(fileIO).val
        self.height        = gimp_uint32(fileIO).val
        self.bytesPerPixel = gimp_uint32(fileIO).val
        print("---- Hierarchy ----")
        print("-- Width x Height [%s x %s] " % (self.width,self.height))
        print("-- BPP [%s] " % (self.bytesPerPixel))
        # Skip
        gimp_uint32(fileIO)
        # Do ALL the level pointers
        levelPointer = gimp_pointer(fileIO).val
        levelStructure = level(fileIO,levelPointer)