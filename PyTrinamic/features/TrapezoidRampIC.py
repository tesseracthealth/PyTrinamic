# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp
from PyTrinamic.features.FeatureProvider import FeatureProvider

class TrapezoidRampIC(TrapezoidRamp, FeatureProvider):
    def setTargetPosition(self, value, axis=None):
        return self.writeRegisterField(self.fields.XTARGET, value, (axis if axis else self.getAxis()))
    def getTargetPosition(self, axis=None):
        return self.readRegisterField(self.fields.XTARGET, (axis if axis else self.getAxis()))
    def setActualPosition(self, value, axis=None):
        return self.writeRegisterField(self.fields.XACTUAL, value, (axis if axis else self.getAxis()))
    def getActualPosition(self, axis=None):
        return self.readRegisterField(self.fields.XACTUAL, (axis if axis else self.getAxis()))
    def setTargetVelocity(self, value, axis=None):
        return self.writeRegisterField(self.fields.VMAX, value, (axis if axis else self.getAxis()))
    def getTargetVelocity(self, axis=None):
        return self.readRegisterField(self.fields.VMAX, (axis if axis else self.getAxis()))
    def setActualVelocity(self, value, axis=None):
        return self.writeRegisterField(self.fields.VACTUAL, value, (axis if axis else self.getAxis()))
    def getActualVelocity(self, axis=None):
        return self.readRegisterField(self.fields.VACTUAL, (axis if axis else self.getAxis()))
    def setMaximumVelocity(self, value, axis=None):
        return self.writeRegisterField(self.fields.VMAX, value, (axis if axis else self.getAxis()))
    def getMaximumVelocity(self, axis=None):
        return self.readRegisterField(self.fields.VMAX, (axis if axis else self.getAxis()))
    def setMaximumAcceleration(self, value, axis=None):
        return self.writeRegisterField(self.fields.AMAX, value, (axis if axis else self.getAxis()))
    def getMaximumAcceleration(self, axis=None):
        return self.readRegisterField(self.fields.AMAX, (axis if axis else self.getAxis()))
    def setRampMode(self, value, axis=None):
        if(hasattr(self.fields, "RAMPMODE")):
            return self.writeRegisterField(self.fields.RAMPMODE, value, (axis if axis else self.getAxis()))
    def getRampMode(self, axis=None):
        if(hasattr(self.fields, "RAMPMODE")):
            return self.readRegisterField(self.fields.RAMPMODE, (axis if axis else self.getAxis()))
