# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.Feature import Feature
from PyTrinamic.features.FeatureProvider import FeatureProvider

class StallGuard2(Feature, FeatureProvider):
    def stallGuard2_setFilterEnabled(self, value, axis):
        raise NotImplementedError()
    def stallGuard2_getFilterEnabled(self, axis):
        raise NotImplementedError()
    def stallGuard2_setStallGuardThreshold(self, value, axis):
        raise NotImplementedError()
    def stallGuard2_getStallGuardThreshold(self, axis):
        raise NotImplementedError()
    def stallGuard2_setStallVelocity(self, value, axis):
        raise NotImplementedError()
    def stallGuard2_getStallVelocity(self, axis):
        raise NotImplementedError()
