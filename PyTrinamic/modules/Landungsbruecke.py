'''
Created on 24.07.2019

@author: LK
'''

from Module import Module

class Landungsbruecke(Module, StallGuard2Module):
    __GLOBAL_PARAMETERS = {
        "par::VitalSignsErrorMask": 1,
        "par::DriversEnable": 2,
        "par::DebugMode": 3,
        "par::BoardAssignment": 4,
        "par::HWID": 5,
        "par::PinState": 6
    }

    # Constructor
    def __init__(self, connection, evalboard, moduleId=None):
        self.__connection = connection
        self.__evalboard = evalboard
        self.__moduleId = moduleId

    # Setters

    def setConnection(self, connection):
        self.__connection = connection

    def setEvalboard(self, evalboard):
        self.__evalboard = evalboard

    def setModuleId(self, moduleId):
        self.__moduleId = moduleId

    # Getters

    def getConnection(self):
        return self.__connection

    def getEvalboard(self):
        return self.__evalboard

    def getModuleId(self):
        return self.__moduleId

    # General functions

    def axisParameter(self, strParameter):
        return self.getEvalboard().axisParameter(strParameter)

    def getAxisParameter(self, commandType, axis, signed=False):
        return self.getConnection().getAxisParameter(commandType, axis, self.getModuleId(), signed)

    def setAxisParameter(self, commandType, axis, value):
        return self.getConnection().setAxisParameter(commandType, axis, value, self.getModuleId())

    # Use the motion controller functions for register access
    def writeRegister(self, registerAddress, value):
        return self.getConnection().writeMC(registerAddress, value, self.getModuleId())

    def readRegister(self, registerAddress, signed=False):
        return self.getConnection().readMC(registerAddress, self.getModuleId(), signed)

    def hasFeature(self, feature):
        # Check if I have the feature as mixin
        out = super().hasFeature(feature)
        if not out:
            # Check if my evalboard has the feature
            out = self.__evalboard.hasFeature(feature)
        return out
