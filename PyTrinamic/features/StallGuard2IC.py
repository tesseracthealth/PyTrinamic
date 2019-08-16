from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2IC(StallGuard2):
    def stallGuard2_setFilterEnabled(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.SFILT, value)
    def stallGuard2_getFilterEnabled(self, axis):
        del axis
        return self.readRegisterField(self.fields.SFILT)
    def stallGuard2_setStallGuardThreshold(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.SGT, value)
    def stallGuard2_getStallGuardThreshold(self, axis):
        del axis
        return self.readRegisterField(self.fields.SGT)
    def stallGuard2_setStallVelocity(self, axis, value):
        del axis
        return self.writeRegisterField(self.fields.TCOOLTHRS, value)
    def stallGuard2_getStallVelocity(self, axis):
        del axis
        return self.readRegisterField(self.fields.TCOOLTHRS)
