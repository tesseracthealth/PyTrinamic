class Module(object):
    def hasFeature(self, feature):
        return isinstance(self, feature)
