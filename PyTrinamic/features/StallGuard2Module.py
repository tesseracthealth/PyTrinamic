from PyTrinamic.features.StallGuard2 import StallGuard2

# StallGuard2 feature interface mixin for modules
# Module class needs to provide setAxisParameter, getAxisParameter and axisParameter functions
# (no full TMCL implementation neccessary)

class StallGuard2Module(StallGuard2):
    def stallGuard2_setFilterEnabled(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::SG2FilterEnable"), axis, value)
    def stallGuard2_getFilterEnabled(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::SG2FilterEnable"), axis)
    def stallGuard2_setStallGuardThreshold(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::SG2Threshold"), axis, value)
    def stallGuard2_getStallGuardThreshold(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::SG2Threshold"), axis)
    # Requires coolStep feature
    def stallGuard2_setStallVelocity(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.setAxisParameter(self.axisParameter("par::smartEnergyStallVelocity"), axis, value)
    # Requires coolStep feature
    def stallGuard2_getStallVelocity(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::smartEnergyStallVelocity"), axis)
