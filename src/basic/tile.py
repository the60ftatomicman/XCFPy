# https://developer.gimp.org/core/standards/xcf/#the-hierarchy-structure
#https://github.com/FHPythonUtils/GimpFormats/blob/master/gimpformats/GimpImageLevel.py#L117
from math                     import ceil
from src.basic.gimp_string    import gimp_string
from src.basic.gimp_uint32    import gimp_uint32
from src.basic.gimp_pixel     import gimp_rle_pixel

class tile:
    def __init__(self, fileIO,byteLocation,idx):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        print("Jumped to position: %s" % (fileIO.tell()))
        self.index = idx
        print("---- tile [%s] ----"%(self.index))
        #self.pixels = [gimp_rle_pixel(fileIO),gimp_rle_pixel(fileIO),gimp_rle_pixel(fileIO)]
        