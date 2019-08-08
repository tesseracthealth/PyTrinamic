from StallGuard2 import StallGuard2

# StallGuard2 feature interface mixin for modules
# Module class needs to provide setAxisParameter and getAxisParameter functions
# (no full TMCL implementation neccessary)
class StallGuard2Module(StallGuard2):
    def stallGuard2_setFilterEnabled(self):
        self.setAxisParameter(self, commandType, axis, value, moduleID=None)
    def stallGuard2_getFilterEnabled(self):
        self.setAxisParameter(self, commandType, axis, value, moduleID=None)
        raise NotImplementedError()
    def stallGuard2_setStallGuardThreshold(self):
        self.setAxisParameter(self, commandType, axis, value, moduleID=None)
        raise NotImplementedError()
    def stallGuard2_getStallGuardThreshold(self):
        self.setAxisParameter(self, commandType, axis, value, moduleID=None)
        raise NotImplementedError()
