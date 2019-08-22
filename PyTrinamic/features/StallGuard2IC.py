# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2IC(StallGuard2):
    def stallGuard2_setFilterEnabled(self, value, axis=None):
        return self.writeRegisterField(self.fields.SFILT, value, (axis if axis else self.getAxis()))
    def stallGuard2_getFilterEnabled(self, axis=None):
        return self.readRegisterField(self.fields.SFILT, (axis if axis else self.getAxis()))
    def stallGuard2_setStallGuardThreshold(self, value, axis=None):
        return self.writeRegisterField(self.fields.SGT, value, (axis if axis else self.getAxis()))
    def stallGuard2_getStallGuardThreshold(self, axis=None):
        return self.readRegisterField(self.fields.SGT, (axis if axis else self.getAxis()))
    def stallGuard2_setStallVelocity(self, value, axis=None):
        return self.writeRegisterField(self.fields.TCOOLTHRS, value, (axis if axis else self.getAxis()))
    def stallGuard2_getStallVelocity(self, axis=None):
        return self.readRegisterField(self.fields.TCOOLTHRS, (axis if axis else self.getAxis()))
