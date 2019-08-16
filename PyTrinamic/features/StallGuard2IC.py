from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2IC(StallGuard2):
    def stallGuard2_setFilterEnabled(self):
        raise NotImplementedError()
    def stallGuard2_getFilterEnabled(self):
        raise NotImplementedError()
    def stallGuard2_setStallGuardThreshold(self):
        raise NotImplementedError()
    def stallGuard2_getStallGuardThreshold(self):
        raise NotImplementedError()
    def stallGuard2_setStallVelocity(self):
        raise NotImplementedError()
    def stallGuard2_getStallVelocity(self):
        raise NotImplementedError()
