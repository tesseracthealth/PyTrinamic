from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp

class TrapezoidRampIC(TrapezoidRamp):
    def trapezoidRamp_setTargetPosition(self, value, axis=None):
        del axis
        return self.writeRegisterField(self.fields.XTARGET, value)
    def trapezoidRamp_getTargetPosition(self, axis=None):
        del axis
        return self.readRegisterField(self.fields.XTARGET)
    def trapezoidRamp_setActualPosition(self, value, axis=None):
        del axis
        return self.writeRegisterField(self.fields.XACTUAL, value)
    def trapezoidRamp_getActualPosition(self, axis=None):
        del axis
        return self.readRegisterField(self.fields.XACTUAL)
    def trapezoidRamp_setTargetVelocity(self, value, axis=None):
        del axis
        return self.writeRegisterField(self.fields.VMAX, value)
    def trapezoidRamp_getTargetVelocity(self, axis=None):
        del axis
        return self.readRegisterField(self.fields.VMAX)
    def trapezoidRamp_setActualVelocity(self, value, axis=None):
        del axis
        return self.writeRegisterField(self.fields.VACTUAL, value)
    def trapezoidRamp_getActualVelocity(self, axis=None):
        del axis
        return self.readRegisterField(self.fields.VACTUAL)
    def trapezoidRamp_setMaximumVelocity(self, value, axis=None):
        del axis
        return self.writeRegisterField(self.fields.VMAX, value)
    def trapezoidRamp_getMaximumVelocity(self, axis=None):
        del axis
        return self.readRegisterField(self.fields.VMAX)
    def trapezoidRamp_setMaximumAcceleration(self, value, axis=None):
        del axis
        return self.writeRegisterField(self.fields.AMAX, value)
    def trapezoidRamp_getMaximumAcceleration(self, axis=None):
        del axis
        return self.readRegisterField(self.fields.AMAX)
