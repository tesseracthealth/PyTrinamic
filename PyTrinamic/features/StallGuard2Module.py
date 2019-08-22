# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.StallGuard2 import StallGuard2
from PyTrinamic.features.FeatureProvider import FeatureProvider

# StallGuard2 feature interface mixin for modules
# Module class needs to provide setAxisParameter, getAxisParameter and axisParameter functions
# (no full TMCL implementation neccessary)

class StallGuard2Module(StallGuard2, FeatureProvider):
    def stallGuard2_setFilterEnabled(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::SG2FilterEnable"), (axis if axis else self.getAxis()), value)
    def stallGuard2_getFilterEnabled(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::SG2FilterEnable"), (axis if axis else self.getAxis()))
    def stallGuard2_setStallGuardThreshold(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::SG2Threshold"), (axis if axis else self.getAxis()), value)
    def stallGuard2_getStallGuardThreshold(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::SG2Threshold"), (axis if axis else self.getAxis()))
    # Requires coolStep feature
    def stallGuard2_setStallVelocity(self, value, axis=None):
        return self.setAxisParameter(self.axisParameter("par::smartEnergyStallVelocity"), (axis if axis else self.getAxis()), value)
    # Requires coolStep feature
    def stallGuard2_getStallVelocity(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::smartEnergyStallVelocity"), (axis if axis else self.getAxis()))
