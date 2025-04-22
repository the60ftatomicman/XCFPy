from src.props.base import base

class prop_end(base):
    typecode    = 0
    payLoadSize = 0
    name        = "PROP_END"
    def __init__(self, fileIO):
        super().__init__(fileIO,prop_end.name,prop_end.typecode,prop_end.payLoadSize)
