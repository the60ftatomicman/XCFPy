
from src.props.image.prop_compression import prop_compression
from src.props.image.prop_resolution  import prop_resolution
from src.props.image.prop_unit        import prop_unit
from src.props.image.prop_guides      import prop_guides

from src.props.layer.prop_active_layer    import prop_active_layer
from src.props.layer.prop_opacity         import prop_opacity
from src.props.layer.prop_float_opacity   import prop_float_opacity
from src.props.layer.prop_visible         import prop_visible
from src.props.layer.prop_apply_mask      import prop_apply_mask
from src.props.layer.prop_edit_mask       import prop_edit_mask
from src.props.layer.prop_show_mask       import prop_show_mask
from src.props.layer.prop_offsets         import prop_offsets
from src.props.layer.prop_mode            import prop_mode
from src.props.layer.prop_blend_space     import prop_blend_space
from src.props.layer.prop_composite_space import prop_composite_space
from src.props.layer.prop_composite_mode  import prop_composite_mode
from src.props.layer.prop_linked          import prop_linked

from src.props.shared.prop_lock      import prop_lock_alpha,prop_lock_content,prop_lock_position,prop_lock_visibility
from src.props.shared.prop_tattoo    import prop_tattoo
from src.props.shared.prop_end       import prop_end
from src.props.shared.prop_parasites import prop_parasites
from src.props.shared.prop_color_tag import prop_color_tag



class prop_factory:

    assignable_properties = [
        # Shared
        prop_end,
        prop_lock_position,
        prop_tattoo,
        prop_parasites,
        prop_color_tag,
        prop_lock_content,
        prop_lock_visibility,
        # Images properties
        prop_compression,
        prop_resolution,
        prop_unit,
        prop_guides,
        # Layer properties
        prop_active_layer,
        prop_opacity,
        prop_float_opacity,
        prop_visible,
        prop_lock_alpha,
        prop_apply_mask,
        prop_edit_mask,
        prop_show_mask,
        prop_offsets,
        prop_mode,
        prop_blend_space,
        prop_composite_space,
        prop_composite_mode,
        prop_linked
    ]

    def __init__(self, fileIO):
        self.val = None
        self.type = "undetermined"
        b = fileIO.read(4)
        typecode = int.from_bytes(b, byteorder='big')
        fileIO.seek(-4,1)
        for prop_type in prop_factory.assignable_properties:
            if hasattr(prop_type, "typecode") and typecode == prop_type.typecode:
                self.val = prop_type(fileIO)
                self.type = prop_type.name
                #if typecode == prop_end.typecode:
                #    print("----- END OF PROPERTIES LIST ------")
            if self.val != None:
                break
        if self.val == None:
            print("[ERROR] unknown property type code [%s]"%(typecode))