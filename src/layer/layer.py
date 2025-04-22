from src.basic.gimp_string     import gimp_string
from src.basic.gimp_unit32     import gimp_uint32
from src.layer.gimp_layer_type import gimp_layer_type
from src.props.prop_list       import prop_list

class layer:
    def __init__(self, fileIO,byteLocation):
        fileIO.seek(byteLocation,0) #EXACT not relative!
        print("Jumped to position: %s" % (fileIO.tell()))
        self.width  = gimp_uint32(fileIO).val
        self.height = gimp_uint32(fileIO).val
        self.type   = gimp_layer_type(fileIO).val
        self.name   = gimp_string(fileIO).val
        print("---- Layer [%s] ----" % (self.name))
        print("-- type [%s] " % (self.type))
        print("-- Width x Height [%s x %s] " % (self.width,self.height))
        print("-- props -- ")
        self.props  = prop_list(fileIO).val
        print("---- END ----")