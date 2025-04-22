from src.basic.gimp_unit32     import gimp_uint32
from src.basic.gimp_pointer    import gimp_pointer

from src.layer.layer           import layer

from src.props.prop_list       import prop_list


class xcf:
    def __init__(self, fileIO):
        self.fileTag      = fileIO.read(9)
        self.fileVersion  = fileIO.read(5)
        self.base_width   = gimp_uint32(fileIO)
        self.base_height  = gimp_uint32(fileIO)
        self.base_type    = gimp_uint32(fileIO)
        self.precision    = gimp_uint32(fileIO)
        self.props        = prop_list(fileIO).val

        #Now do layers
        layerPointers = []
        self.layers   = []
        layerPointers.append(gimp_pointer(fileIO).val)

        for layerPointer in layerPointers:
            l = layer(fileIO,layerPointer)