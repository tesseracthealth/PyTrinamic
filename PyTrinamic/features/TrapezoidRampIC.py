from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp

class TrapezoidRampIC(TrapezoidRamp):
    def trapezoidRamp_setTargetPosition(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.XTARGET, value)
    def trapezoidRamp_getTargetPosition(self, axis):
        del axis
        return self.readRegisterField(self.fields.XTARGET)
    def trapezoidRamp_setActualPosition(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.XACTUAL, value)
    def trapezoidRamp_getActualPosition(self, axis):
        del axis
        return self.readRegisterField(self.fields.XACTUAL)
    def trapezoidRamp_setTargetVelocity(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.VMAX, value)
    def trapezoidRamp_getTargetVelocity(self, axis):
        del axis
        return self.readRegisterField(self.fields.VMAX)
    def trapezoidRamp_setActualVelocity(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.VACTUAL, value)
    def trapezoidRamp_getActualVelocity(self, axis):
        del axis
        return self.readRegisterField(self.fields.VACTUAL)
    def trapezoidRamp_setMaximumVelocity(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.VMAX, value)
    def trapezoidRamp_getMaximumVelocity(self, axis):
        del axis
        return self.readRegisterField(self.fields.VMAX)
    def trapezoidRamp_setMaximumAcceleration(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.AMAX, value)
    def trapezoidRamp_getMaximumAcceleration(self, axis):
        del axis
        return self.readRegisterField(self.fields.AMAX)
