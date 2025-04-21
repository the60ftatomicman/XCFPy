import struct
class gimp_float:
    def __init__(self, fileIO):
        self.raw = fileIO.read(4)
        self.val = struct.unpack('>f', self.raw)
