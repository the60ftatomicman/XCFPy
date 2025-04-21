from src.basic.gimp_unit32 import gimp_uint32
from src.basic.gimp_string import gimp_string

class prop_parasites:
    def __init__(self, fileIO):
        self.type = gimp_uint32(fileIO).val
        if self.type != 21:
            print("Expected type: [%s] but got [%s]" % (21,self.type))
        self.payLoadSize = gimp_uint32(fileIO).val
        print("parasite payload size: [%s]"%self.payLoadSize)

        self.parasites = []
        i=0
        while i < self.payLoadSize:
            parasite = prop_parasite(fileIO)
            print("Parasite [%s] name [%s]"%(len(self.parasites),parasite.name))
            print("Parasite [%s] flags [%s]"%(len(self.parasites),parasite.flags))
            print("Parasite [%s] payLoad [%s]"%(len(self.parasites),parasite.payLoad))
            self.parasites.append(parasite)
            nextParasite = gimp_uint32(fileIO).val
            if nextParasite == 0:
                i = self.payLoadSize
            else:
                fileIO.seek(-4,1)
                i = i + parasite.length
        print("parasite count: [%s]"%len(self.parasites))

class prop_parasite:
    def __init__(self, fileIO):
        self.name = gimp_string(fileIO).val
        self.flags = gimp_uint32(fileIO).val
        self.length = gimp_uint32(fileIO).val
        self.payLoad = fileIO.read(self.length)


