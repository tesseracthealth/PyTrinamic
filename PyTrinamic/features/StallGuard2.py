from PyTrinamic.features.Feature import Feature

class StallGuard2(Feature):
    def stallGuard2_setFilterEnabled(self, axis, value):
        raise NotImplementedError()
    def stallGuard2_getFilterEnabled(self, axis):
        raise NotImplementedError()
    def stallGuard2_setStallGuardThreshold(self, axis, value):
        raise NotImplementedError()
    def stallGuard2_getStallGuardThreshold(self, axis):
        raise NotImplementedError()
    def stallGuard2_setStallVelocity(self, axis, value):
        raise NotImplementedError()
    def stallGuard2_getStallVelocity(self, axis):
        raise NotImplementedError()
