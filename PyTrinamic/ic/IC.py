# Created on: 09.08.2019
# Author: LK

from PyTrinamic.helpers import TMC_helpers

class IC(object):
    def __init__(self, channel=0, moduleId=1, connection=None):
        self.__channel  = channel
        self.__moduleId = moduleId
        self.__connection = connection
    def getConnection(self):
        return self.__connection
    def setConnection(self, connection):
        self.__connection = connection
    def getChannel(self):
        return self.__channel
    def setChannel(self, channel):
        self.__channel = channel
    def getModuleId(self):
        return self.__moduleId
    def setModuleId(self, moduleId):
        self.__moduleId = moduleId
    def hasFeature(self, feature):
        return isinstance(self, feature)
    def showChipInfo(self):
        raise NotImplementedError()
    def writeRegister(self, registerAddress, value):
        return self.getConnection().writeMC(self.getChannel(), registerAddress, value, self.getModuleId())
    def readRegister(self, registerAddress, signed=False):
        return self.getConnection().readMC(self.getChannel(), registerAddress, self.getModuleId(), signed)
    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0]), field[1], field[2], value))
    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0]), field[1], field[2])
