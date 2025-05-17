from math import floor
from src.basic.gimp_uint32 import gimp_uint32
from src.props.base import base
from src.enums.guide_orientation import GUIDE_ORIENTATION


## For now I parse this so I don't crash, but it'd be nice to possible to DO something with this
## Like determine our dividers from the guides in the XCF
class prop_guides(base):
    typecode    = 18
    payLoadSize = None
    name        = "PROP_GUIDES"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_guides.name,prop_guides.typecode,prop_guides.payLoadSize)
        ##
        ##
        ##
        self.bytesPerGuide = 5
        self.payLoadSize = gimp_uint32(fileIO).val
        if self.payLoadSize % self.bytesPerGuide != 0:
                print("Expected [%s] payloadSize: [%s] to be divisible by [%s]." % (self.name,self.payLoadSize,self.bytesPerGuide))

        self.val = []
        for i in range(floor(self.payLoadSize/self.bytesPerGuide)):
             self.val.append(prop_guide(fileIO))
        self.print_val()

class prop_guide():
     def __init__(self, fileIO):
          self.coord = gimp_uint32(fileIO).val
          self.orientation = fileIO.read(1)#TODO -- get this to work with BYTES GUIDE_ORIENTATION()