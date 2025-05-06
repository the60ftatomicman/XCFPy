class gimp_rle_pixel:
    def __init__(self, fileIO):
        print("at position: %s" % (fileIO.tell()))
        self.raw = fileIO.read(1)
        self.opcode = int.from_bytes(self.raw, byteorder='big',signed=True)
        print("RLE Pixel is type: [%s]"%(self.opcode))
        if self.opcode < 126:
            print(" -- Short run of same pixels (0 -> 126)")
            self.raw = fileIO.read(1)
            self.val = int.from_bytes(self.raw, byteorder='big',signed=True)
            print(" -- color [%s] count [%s]"%(self.val,self.opcode+1))
        elif self.opcode == 127:
            print(" -- Long run of same pixels (127)")
        elif self.opcode == 128:
            print(" -- Long run of different pixels (128)")
        elif self.opcode > 128 and self.opcode < 256:
            print(" -- short run of different pixels (129 -> 225)")
        else:
             print(" -- unkown opcode [%s]"%(self.opcode))