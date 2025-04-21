class gimp_pointer:
    def __init__(self, fileIO,version = None):
        self.raw = fileIO.read(4)
        #if '11' in version:
        #    fileIO.seek(-4,1)
        #    self.raw = fileIO.read(8)
        self.val = int.from_bytes(self.raw, byteorder='big')
