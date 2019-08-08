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
    def __init__(self, evalboard):
        self.__evalboard = evalboard

    # Setters

    def setEvalboard(self, evalboard):
        self.__evalboard = evalboard

    # Getters

    def getEvalboard(self):
        return self.__evalboard

    # General functions

    def hasFeature(self, feature):
        # Check if I have the feature as mixin
        out = super().hasFeature(feature)
        if not out:
            # Check if my evalboard has the feature
            out = self.__evalboard.hasFeature(feature)
        return out
