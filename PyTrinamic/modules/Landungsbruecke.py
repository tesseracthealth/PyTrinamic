'''
Created on 24.07.2019

@author: LK
'''

from Module import Module

class Landungsbruecke(Module, StallGuard2Module):
    GP_VitalSignsErrorMask  = 1
    GP_DriversEnable        = 2
    GP_DebugMode            = 3
    GP_BoardAssignment      = 4
    GP_HWID                 = 5
    GP_PinState             = 6

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

    def hasFeature(self, feature):
        # Check if I have the feature as mixin
        out = super().hasFeature(feature)
        if not out:
            # Check if my evalboard has the feature
            out = self.__evalboard.hasFeature(feature)
        return out
