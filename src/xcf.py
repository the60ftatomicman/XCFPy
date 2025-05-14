## https://developer.gimp.org/core/standards/xcf/#xcf-file
## TODO ---- everytime a list results in us getting an offset thats odd,
## try putting a single int pull since 0s usually delimit stuff as well
##
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
            # this delimits every layer 
            gimp_uint32(fileIO)
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

    def get_pixels(self,layerName):
        pixels = []
        layer: layer
        for layer in self.layers:
            if layer.name == layerName:
                pixels = layer.get_pixels()
        return pixels

    def get_dimensions(self,layerName):
        dimensions = [-1,-1]
        layer: layer
        for layer in self.layers:
            if layer.name == layerName:
                dimensions = [layer.width,layer.height]
        return dimensions