from src.basic.gimp_uint32 import gimp_uint32

class gimp_string:
    def __init__(self, fileIO):

        length = gimp_uint32(fileIO).val

        self.raw = fileIO.read(length)
        self.val = self.raw.decode("utf-8")
        print("Length of string is: [%s]"%(length))

