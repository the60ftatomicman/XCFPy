# https://developer.gimp.org/core/standards/xcf/#the-hierarchy-structure
#https://github.com/FHPythonUtils/GimpFormats/blob/master/gimpformats/GimpImageLevel.py#L117
from math                     import ceil
from copy                     import deepcopy
from src.basic.gimp_string    import gimp_string
from src.basic.gimp_uint32    import gimp_uint32

class tile:
    def __init__(self, fileIO,byteLocation,idx,width,height,bpp):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        #print("Jumped to position: %s" % (fileIO.tell()))
        self.index = idx
        print("---- tile [%s] ----"%(self.index))
        self.pixels = self.decode_RLE_Tile(fileIO,width,height,bpp)

    ## We count ALL of the red values, than blue, than green, than alpha.
    def decode_RLE_Tile(self,fileIO,width,height,bytesPerPixel):
        totalPixels = width*height
        bppIdx = 0
        pixels = []
        for i in range(totalPixels):
            pixels.append([])
        while bppIdx < bytesPerPixel:
            #print("---- Byte [%s] of [%s] ----"%(bppIdx,bytesPerPixel))
            pixelIdx = 0
            while pixelIdx < totalPixels:
                opcode = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                val    = 0
                count  = 0
                if opcode < 126:
                    #print(" Short run of same pixels (0 -> 126)")
                    count = opcode+1
                    val = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                    for i in range(count):
                        pixels[pixelIdx+i].append(val)
                elif opcode == 127:
                    #print(" Long run of same pixels (127)")
                    p = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                    q = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                    count = p*256+q
                    val = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                    for i in range(count):
                        pixels[pixelIdx+i].append(val)
                elif opcode == 128:
                    #print(" Long run of different pixels (128)")
                    p = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                    q = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                    count = p*256+q
                    for i in range(count):
                        val = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                        pixels[pixelIdx+i].append(val)
                elif opcode > 128 and opcode < 256:
                    #print(" short run of different pixels (129 -> 225)")
                    count = 256-opcode
                    for i in range(count):
                        val = int.from_bytes(fileIO.read(1), byteorder='big',signed=False)
                        pixels[pixelIdx+i].append(val)
                else:
                    print(" unkown opcode [%s]"%(opcode))
                pixelIdx += count
            bppIdx += 1
        return pixels
        #print(pixels)
        #print(len(pixels))