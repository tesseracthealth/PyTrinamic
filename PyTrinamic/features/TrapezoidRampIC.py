# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp
from PyTrinamic.features.FeatureProvider import FeatureProvider

class TrapezoidRampIC(TrapezoidRamp, FeatureProvider):
    def trapezoidRamp_setTargetPosition(self, value, axis=None):
        return self.writeRegisterField(self.fields.XTARGET, value, (axis if axis else self.getAxis()))
    def trapezoidRamp_getTargetPosition(self, axis=None):
        return self.readRegisterField(self.fields.XTARGET, (axis if axis else self.getAxis()))
    def trapezoidRamp_setActualPosition(self, value, axis=None):
        return self.writeRegisterField(self.fields.XACTUAL, value, (axis if axis else self.getAxis()))
    def trapezoidRamp_getActualPosition(self, axis=None):
        return self.readRegisterField(self.fields.XACTUAL, (axis if axis else self.getAxis()))
    def trapezoidRamp_setTargetVelocity(self, value, axis=None):
        return self.writeRegisterField(self.fields.VMAX, value, (axis if axis else self.getAxis()))
    def trapezoidRamp_getTargetVelocity(self, axis=None):
        return self.readRegisterField(self.fields.VMAX, (axis if axis else self.getAxis()))
    def trapezoidRamp_setActualVelocity(self, value, axis=None):
        return self.writeRegisterField(self.fields.VACTUAL, value, (axis if axis else self.getAxis()))
    def trapezoidRamp_getActualVelocity(self, axis=None):
        return self.readRegisterField(self.fields.VACTUAL, (axis if axis else self.getAxis()))
    def trapezoidRamp_setMaximumVelocity(self, value, axis=None):
        return self.writeRegisterField(self.fields.VMAX, value, (axis if axis else self.getAxis()))
    def trapezoidRamp_getMaximumVelocity(self, axis=None):
        return self.readRegisterField(self.fields.VMAX, (axis if axis else self.getAxis()))
    def trapezoidRamp_setMaximumAcceleration(self, value, axis=None):
        return self.writeRegisterField(self.fields.AMAX, value, (axis if axis else self.getAxis()))
    def trapezoidRamp_getMaximumAcceleration(self, axis=None):
        return self.readRegisterField(self.fields.AMAX, (axis if axis else self.getAxis()))
