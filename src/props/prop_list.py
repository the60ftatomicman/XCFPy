from src.props.prop_factory import prop_factory

class prop_list:
    def __init__(self, fileIO):
        self.val  = []

        currPropType = "initial"
        while currPropType != "PROP_END" and currPropType != "undetermined":
            currProp = prop_factory(fileIO)
            if currProp.type != "undetermined":
                self.val.append(currProp)
            currPropType = currProp.type
        
        print("Prop count [%s]" % (
            len(self.val)
        ))
        
        for currProp in self.val:
            print("Prop Type: [%s] " % currProp.type)