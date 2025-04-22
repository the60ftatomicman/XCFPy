
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
from src.props.layer.prop_show_mask     import prop_show_mask
from src.props.layer.prop_offsets       import prop_offsets
from src.props.layer.prop_mode          import prop_mode
from src.props.layer.prop_blend_space   import prop_blend_space

from src.props.shared.prop_lock_position   import prop_lock_position
from src.props.shared.prop_tattoo          import prop_tattoo
from src.props.shared.prop_end             import prop_end
from src.props.shared.prop_parasites       import prop_parasites
from src.props.shared.prop_color_tag       import prop_color_tag
from src.props.shared.prop_lock_content    import prop_lock_content
from src.props.shared.prop_lock_visibility import prop_lock_visibility

class prop:
    def __init__(self, fileIO):
        self.val = None
        self.type = "undetermined"
        b = fileIO.read(4)
        typecode = int.from_bytes(b, byteorder='big')
        fileIO.seek(-4,1)
        
        if typecode == prop_end.typecode:
            self.val  = prop_end(fileIO)
            self.type = prop_end.name
            print("----- END OF PROPERTIES LIST ------")
        elif typecode == prop_active_layer.typecode:
            self.val  = prop_active_layer(fileIO)
            self.type = prop_active_layer.name
        elif typecode == prop_opacity.typecode:
            self.val  = prop_opacity(fileIO)
            self.type = prop_opacity.name
        elif typecode == prop_mode.typecode:
            self.val  = prop_mode(fileIO)
            self.type = prop_mode.name
        elif typecode == prop_visible.typecode:
            self.val  = prop_visible(fileIO)
            self.type = prop_visible.name
        elif typecode == prop_lock_alpha.typecode:
            self.val  = prop_lock_alpha(fileIO)
            self.type = prop_lock_alpha.name
        elif typecode == prop_apply_mask.typecode:
            self.val  = prop_apply_mask(fileIO)
            self.type = prop_apply_mask.name
        elif typecode == prop_edit_mask.typecode:
            self.val  = prop_edit_mask(fileIO)
            self.type = prop_edit_mask.name
        elif typecode == prop_show_mask.typecode:
            self.val  = prop_show_mask(fileIO)
            self.type = prop_show_mask.name
        elif typecode == prop_offsets.typecode:
            self.val  = prop_offsets(fileIO)
            self.type = prop_offsets.name
        elif typecode == prop_compression.typecode:
            self.val  = prop_compression(fileIO)
            self.type = prop_compression.name
        elif typecode == prop_resolution.typecode:
            self.val  = prop_resolution(fileIO)
            self.type = prop_resolution.name
        elif typecode == prop_tattoo.typecode:
            self.val  = prop_tattoo(fileIO)
            self.type = prop_tattoo.name
        elif typecode == prop_parasites.typecode:
            self.val  = prop_parasites(fileIO)
            self.type = prop_parasites.name
        elif typecode == prop_unit.typecode:
            self.val  = prop_unit(fileIO)
            self.type = prop_unit.name
        elif typecode == prop_lock_content.typecode:
            self.val  = prop_lock_content(fileIO)
            self.type = prop_lock_content.name
        elif typecode == prop_lock_position.typecode:
            self.val  = prop_lock_position(fileIO)
            self.type = prop_lock_position.name
        elif typecode == prop_float_opacity.typecode:
            self.val  = prop_float_opacity(fileIO)
            self.type = prop_float_opacity.name
        elif typecode == prop_color_tag.typecode:
            self.val  = prop_color_tag(fileIO)
            self.type = prop_color_tag.name
        elif typecode == prop_blend_space.typecode:
            self.val  = prop_blend_space(fileIO)
            self.type = prop_blend_space.name
        elif typecode == prop_lock_visibility.typecode:
            self.val  = prop_lock_visibility(fileIO)
            self.type = prop_lock_visibility.name
        else:
            print("[ERROR] unknown property code [%s][%s]"%(self.val,typecode))