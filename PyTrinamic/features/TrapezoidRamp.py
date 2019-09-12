# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.Feature import Feature

class TrapezoidRamp(Feature):
    def setTargetPosition(self, value, axis):
        raise NotImplementedError()
    def getTargetPosition(self, axis):
        raise NotImplementedError()
    def setActualPosition(self, value, axis):
        raise NotImplementedError()
    def getActualPosition(self, axis):
        raise NotImplementedError()
    def setTargetVelocity(self, value, axis):
        raise NotImplementedError()
    def getTargetVelocity(self, axis):
        raise NotImplementedError()
    def setActualVelocity(self, value, axis):
        raise NotImplementedError()
    def getActualVelocity(self, axis):
        raise NotImplementedError()
    def setMaximumVelocity(self, value, axis):
        raise NotImplementedError()
    def getMaximumVelocity(self, axis):
        raise NotImplementedError()
    def setMaximumAcceleration(self, value, axis):
        raise NotImplementedError()
    def getMaximumAcceleration(self, axis):
        raise NotImplementedError()
