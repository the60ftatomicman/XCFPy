## https://developer.gimp.org/core/standards/xcf/#xcf-file
## THE ISSUE YOU ARE HAVING... you need to modify your props list based soley on the things that it shows
# ---------- Imports
# ----- Internal Libs
from os import path
from src.basic.gimp_string     import gimp_string
from src.basic.gimp_unit32     import gimp_uint32
from src.basic.gimp_pointer    import gimp_pointer
from src.layer.gimp_layer_type import gimp_layer_type
from src.props.prop            import prop

# ---------- Main
if __name__ == '__main__':
    dirRoot     = path.dirname(path.realpath(__file__))
    xcfFilePath = dirRoot+"/demo.xcf"
    layerPointers=[]
    with open(xcfFilePath, "rb", buffering=0) as f:
        sections = [
            ["fileTag",9,bytes],
            ["fileVersion",5,bytes],
            ["width",4,gimp_uint32],
            ["height",4,gimp_uint32],
            ["base_type",4,gimp_uint32],
            ["precision",4,gimp_uint32],
            ["PROP_COMPRESSION",4,prop],
            ["PROP_RESOLUTION",4,prop],
            ["PROP_TATTOO",4,prop],
            ["PROP_UNIT",4,prop],
            ["PROP_PARASITES",4,prop],
            ["PROP_END",4,prop],
            ["Layer1Pointer",4,gimp_pointer]
            #["Layer2Pointer",4,int]
        ]
        for section in sections:
            if section[2] is gimp_uint32:
                gint = gimp_uint32(f)
                print("[%s]=[%s]" % (section[0], gint.val))
            #TODO we need an unknown prop class that gets the type and builds from there
            elif section[2] is prop:
                p = prop(f)
                print("[%s]=[%s,%s]" % (section[0], p.type,p.val))
            elif section[2] is gimp_pointer:
                p = gimp_pointer(f,'v011') ## TODO -- add something that stores the file version
                print("[%s]=[%s]" % (section[0],p.val))
                layerPointers.append([section[0],p.val])
            else:
                b = f.read(section[1])
                print("[%s]=[%s]" % (section[0], b))

        # lets get the height of layer 1
        # https://developer.gimp.org/core/standards/xcf/#layer-properties
        for layer in layerPointers:
            f.seek(layer[1],0)
            print("Jumped to position: %s" % (f.tell()))
            layerName = layer[0]
            properties = [
                ["width"                ,4,gimp_uint32],
                ["height"               ,4,gimp_uint32],
                ["type"                 ,4,gimp_layer_type],
                ["name"                 ,4,gimp_string],
                ["prop_active_layer"    ,4,prop],
                ["prop_opacity"         ,4,prop],
                ["prop_float_opacity"   ,4,prop],
                ["prop_visibility"      ,4,prop],
                ["prop_color_tag"       ,4,prop],
                ["prop_locked_content"  ,4,prop],
                ["prop_lock_alpha"      ,4,prop],
                ["prop_lock_position"   ,4,prop],
                ["prop_lock_visibility" ,4,prop],
                ["prop_apply_mask"      ,4,prop],
                ["prop_edit_mask"       ,4,prop],
                #PROP_COLOR_TAG 
                ["next",4,gimp_uint32]
            ]
            for property in properties:
                if property[2] is gimp_uint32:
                    gint = gimp_uint32(f)
                    print("[%s]=[%s]" % (property[0], gint.val))
                elif property[2] is gimp_layer_type:
                    glyrtype = gimp_layer_type(f)
                    print("[%s]=[%s]" % (property[0], glyrtype.val))
                elif property[2] is prop:
                    p = prop(f)
                    print("[%s]=[%s,%s]" % (property[0], p.type,p.val))
                elif property[2] is gimp_string:
                    gstr = gimp_string(f)
                    print("[%s]=[%s]" % (property[0], gstr.val))
                else:
                    b = f.read(property[1])
                    print("[%s %s]=[%s]" % (layerName,property[0], b))