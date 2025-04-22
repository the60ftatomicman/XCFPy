
from src.props.base import base

class prop_active_layer(base):
    typecode    = 2
    payLoadSize = 0
    name        = "PROP_ACTIVE_LAYER"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_active_layer.name,prop_active_layer.typecode,prop_active_layer.payLoadSize)

