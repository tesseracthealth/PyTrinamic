class IC(object):
    def hasFeature(self, feature):
        return isinstance(self, feature)
    def showChipInfo(self):
        raise NotImplementedError()
    def writeRegister(self, registerAddress, value, channel):
        raise NotImplementedError()
    def readRegister(self, registerAddress, channel):
        raise NotImplementedError()
    def writeRegisterField(self, field, value):
        raise NotImplementedError()
    def readRegisterField(self, field):
        raise NotImplementedError()
