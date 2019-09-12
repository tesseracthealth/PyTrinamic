from PyTrinamic.modules.Module import Module

class Evalboard(Module):
    def __init__(self, moduleId=1, connection=None, parent=None):
        super().__init__(moduleId, connection, parent)
        self.__ics = []
    def appendIC(self, ic):
        self.__ics.append(ic)
    def getICs(self):
        return self.__ics
    def setIC(self, ic):
        self.__ics = []
        self.__ics.append(ic)
        self.registers = ic.registers
        self.fields = ic.fields
        self.variants = ic.variants
    def getIC(self, index=None):
        if(self.__ics):
            return self.__ics[index if index else 0]
        return None
    def hasFeature(self, feature, recursive=False):
        if(super().hasFeature(feature, recursive)):
            return True
        elif(recursive):
            for ic in self.getICs():
                if(ic.hasFeature(feature)):
                    return True
        return False
    def writeRegister(self, channel, registerAddress, value):
        raise NotImplementedError()
    def readRegister(self, channel, registerAddress, signed=False):
        raise NotImplementedError()
