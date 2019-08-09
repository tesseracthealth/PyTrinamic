from StallGuard2 import StallGuard2

# StallGuard2 feature interface mixin for modules
# Module class needs to provide setAxisParameter, getAxisParameter and axisParameter functions
# (no full TMCL implementation neccessary)

class StallGuard2Module(StallGuard2):
    def stallGuard2_setFilterEnabled(self, axis, value):
        self.setAxisParameter(self, self.axisParameter("par::SG2FilterEnable"), axis, value)
    def stallGuard2_getFilterEnabled(self, axis):
        return self.getAxisParameter(self, self.axisParameter("par::SG2FilterEnable"), axis)
    def stallGuard2_setStallGuardThreshold(self, axis, value):
        self.setAxisParameter(self, self.axisParameter("par::SG2Threshold"), axis, value)
    def stallGuard2_getStallGuardThreshold(self, axis):
        return self.getAxisParameter(self, self.axisParameter("par::SG2Threshold"), axis, value)
