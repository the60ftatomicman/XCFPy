
## TODO this can probably be lessened....
from src.props.image.prop_compression import prop_compression
from src.props.image.prop_resolution  import prop_resolution
from src.props.image.prop_unit        import prop_unit

from src.props.layer.prop_active_layer  import prop_active_layer
from src.props.layer.prop_opacity       import prop_opacity
from src.props.layer.prop_float_opacity import prop_float_opacity
from src.props.layer.prop_visible       import prop_visible
from src.props.layer.prop_lock_alpha    import prop_lock_alpha
from src.props.layer.prop_apply_mask    import prop_apply_mask
from src.props.layer.prop_edit_mask     import prop_edit_mask

from src.props.shared.prop_lock_position   import prop_lock_position
from src.props.shared.prop_tattoo          import prop_tattoo
from src.props.shared.prop_end             import prop_end
from src.props.shared.prop_parasites       import prop_parasites
from src.props.shared.prop_color_tag       import prop_color_tag
from src.props.shared.prop_locked_content  import prop_locked_content
from src.props.shared.prop_lock_visibility import prop_lock_visibility

class prop:
    def __init__(self, fileIO):
        self.val = None
        self.type = "undetermined"
        b = fileIO.read(4)
        typecode = int.from_bytes(b, byteorder='big')
        fileIO.seek(-4,1)
        if typecode == 0:
            self.val  = prop_end(fileIO)
            self.type = "PROP_END"
            print("--------- END OF PROPERTIES LIST ----------")
        elif typecode == 2:
            self.val  = prop_active_layer(fileIO)
            self.type = "PROP_ACTIVE_LAYER"
        elif typecode == 6:
            self.val  = prop_opacity(fileIO)
            self.type = "PROP_OPACITY"
        elif typecode == 8:
            self.val  = prop_visible(fileIO)
            self.type = "PROP_VISIBLE"
        elif typecode == 10:
            self.val  = prop_lock_alpha(fileIO)
            self.type = "PROP_LOCK_ALPHA"
        elif typecode == 11:
            self.val  = prop_apply_mask(fileIO)
            self.type = "PROP_APPLY_MASK"
        elif typecode == 12:
            self.val  = prop_edit_mask(fileIO)
            self.type = "PROP_EDIT_MASK"
        elif typecode == 17:
            self.val  = prop_compression(fileIO)
            self.type = "PROP_COMPRESSION"
        elif typecode == 19:
            self.val  = prop_resolution(fileIO)
            self.type = "PROP_RESOLUTION"
        elif typecode == 20:
            self.val  = prop_tattoo(fileIO)
            self.type = "PROP_TATTOO"
        elif typecode == 21:
            self.val  = prop_parasites(fileIO)
            self.type = "PROP_PARASITES"
        elif typecode == 22:
            self.val  = prop_unit(fileIO)
            self.type = "PROP_UNIT"
        elif typecode == 28:
            self.val  = prop_locked_content(fileIO)
            self.type = "PROP_LOCK_CONTENT"
        elif typecode == 32:
            self.val  = prop_lock_position(fileIO)
            self.type = "PROP_LOCK_POSITION"
        elif typecode == 33:
            self.val  = prop_float_opacity(fileIO)
            self.type = "PROP_FLOAT_OPACITY"
        elif typecode == 34:
            self.val  = prop_color_tag(fileIO)
            self.type = "PROP_COLOR_TAG"
        elif typecode == 42:
            self.val  = prop_lock_visibility(fileIO)
            self.type = "PROP_LOCK_VISIBILITY"
        else:
            print("[ERROR] unknown property code [%s][%s]"%(self.val,b))