class gimp_int32:
    def __init__(self, fileIO):
        self.raw = fileIO.read(4)
        self.val = int.from_bytes(self.raw, byteorder='big',signed=True)
