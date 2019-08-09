# Created on: 09.08.2019
# Author: LK

class Module(object):
    def hasFeature(self, feature):
        return isinstance(self, feature)
    def axisParameter(self, strParameter):
        raise NotImplementedError()
    def getAxisParameter(self, commandType, axis, signed=False):
        raise NotImplementedError()
    def setAxisParameter(self, commandType, axis, value):
        raise NotImplementedError()
