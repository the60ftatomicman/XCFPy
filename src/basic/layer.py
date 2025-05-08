# https://developer.gimp.org/core/standards/xcf/#the-layer-structure

from src.basic.gimp_string  import gimp_string
from src.basic.gimp_uint32  import gimp_uint32
from src.basic.gimp_pointer import gimp_pointer
from src.basic.hierarchy    import hierarchy

from src.props.prop_list import prop_list

from src.enums.layer_color_mode import LAYER_COLOR_MODE

class layer:
    def __init__(self, fileIO,byteLocation):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        print("Jumped to position: %s" % (fileIO.tell()))
        self.width  = gimp_uint32(fileIO).val
        self.height = gimp_uint32(fileIO).val
        self.type   = gimp_uint32(fileIO).val
        
        if self.type < 0 or self.type > 5:
            print("Expected layer color mode to be between: [%s] and [%s] but got [%s]" % (0,5,self.type))
        self.type = LAYER_COLOR_MODE(self.type)

        self.name   = gimp_string(fileIO).val
        print("---- Layer [%s] ----" % (self.name))
        print("-- type [%s] " % (self.type))
        print("-- Width x Height [%s x %s] " % (self.width,self.height))
        #print("-- props -- ")
        self.props  = prop_list(fileIO).val
        # Skip
        gimp_uint32(fileIO)
        # Hierachy structure
        hierarchyPointer = gimp_pointer(fileIO).val
        self.hierarchy = None
        if hierarchyPointer != 0:
            self.hierarchy = hierarchy(fileIO,hierarchyPointer)
        # Mask structure
        #maskPointer        = gimp_pointer(fileIO).val
        #self.mask = None #hierarchy(fileIO,hierarchyPointer)
        #Skip mask for no, don't care for picross!
        pointer = gimp_pointer(fileIO).val
        while pointer != 0:
            pointer = gimp_pointer(fileIO).val
        print("---- End of Layer ----")

    def get_pixels(self):
        return self.hierarchy.get_pixels()
       
