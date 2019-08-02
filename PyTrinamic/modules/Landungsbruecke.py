'''
Created on 24.07.2019

@author: LK
'''

from Module import Module

class Landungsbruecke(Module):
    GP_VitalSignsErrorMask  = 1
    GP_DriversEnable        = 2
    GP_DebugMode            = 3
    GP_BoardAssignment      = 4
    GP_HWID                 = 5
    GP_PinState             = 6

    def __init__(self, evalboard):
        self.__evalboard = evalboard

    def hasFeature(self, feature):
        out = super().hasFeature(feature)
        if not out:
            out = self.__evalboard.hasFeature(feature)
        return out
