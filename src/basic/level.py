# https://developer.gimp.org/core/standards/xcf/#the-hierarchy-structure
from math                   import ceil
from src.basic.gimp_pointer import gimp_pointer
from src.basic.gimp_uint32  import gimp_uint32
from src.basic.tile         import tile

class level:
    def __init__(self, fileIO,byteLocation,bpp):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        #print("Jumped to position: %s" % (fileIO.tell()))
        self.width     = gimp_uint32(fileIO).val
        self.height    = gimp_uint32(fileIO).val
        self.tileCount = ceil(self.width/64)*ceil(self.height/64)
        print("---- Level ----")
        print("-- Width x Height [%s x %s] " % (self.width,self.height))
        print("-- tiles [%s] " % (self.tileCount))
        #Skip
        gimp_uint32(fileIO).val

        tilePointers = []
        self.tiles   = []
        pointer = gimp_pointer(fileIO).val
        while pointer != 0:
            tilePointers.append(pointer)
            pointer = gimp_pointer(fileIO).val

        if len(tilePointers) != self.tileCount:
            print("Expected there to be: [%s] tiles but got [%s]" % (self.tileCount,len(tilePointers)))

        currentTile = 0
        for tilePointer in tilePointers:
            t = tile(fileIO,tilePointer,currentTile,self.width,self.height,bpp)
            self.tiles.append(t)
            currentTile+=1
        
    def get_pixels(self):
        #pixels = []
        #tile: tile
        #for tile in self.tiles:
        #    pixels.append(tile.pixels)
        return self.tiles[0].pixels
