## https://developer.gimp.org/core/standards/xcf/#xcf-file
from src.basic.gimp_uint32     import gimp_uint32
from src.basic.gimp_pointer    import gimp_pointer

from src.basic.layer           import layer

from src.props.prop_list       import prop_list


class xcf:
    def __init__(self, fileIO):
        print("-----------------------------")
        print("----- Beginning  Image ------")
        print("-----------------------------")
        self.fileTag      = fileIO.read(9)
        self.fileVersion  = fileIO.read(5)
        self.base_width   = gimp_uint32(fileIO)
        self.base_height  = gimp_uint32(fileIO)
        self.base_type    = gimp_uint32(fileIO)
        self.precision    = gimp_uint32(fileIO)
        self.props        = prop_list(fileIO).val

        # Now do layers
        layerPointers = []
        self.layers   = []
        pointer = gimp_pointer(fileIO).val
        while pointer != 0:
            layerPointers.append(pointer)
            pointer = gimp_pointer(fileIO).val

        # Now do Channels
        channelPointers = []
        self.channels   = []
        pointer = gimp_pointer(fileIO).val
        while pointer != 0:
            channelPointers.append(pointer)
            pointer = gimp_pointer(fileIO).val

        # Now do Vectors
        vectorPointers = []
        self.vectors   = []
        pointer = gimp_pointer(fileIO).val
        while pointer != 0:
            vectorPointers.append(pointer)
            pointer = gimp_pointer(fileIO).val
        print("-----------------------------")
        print("----- Beginning Layers ------")
        print("-----------------------------")
        # visit objects
        for layerPointer in layerPointers:
            l = layer(fileIO,layerPointer)
            self.layers.append(l)
        print("-----------------------------")
        print("-----       DONE       ------")
        print("-----------------------------")