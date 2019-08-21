from PyTrinamic.features.Feature import Feature
from PyTrinamic.features.FeatureProvider import FeatureProvider

class TrapezoidRamp(Feature, FeatureProvider):
    def trapezoidRamp_setTargetPosition(self, value, axis):
        raise NotImplementedError()
    def trapezoidRamp_getTargetPosition(self, axis):
        raise NotImplementedError()
    def trapezoidRamp_setActualPosition(self, value, axis):
        raise NotImplementedError()
    def trapezoidRamp_getActualPosition(self, axis):
        raise NotImplementedError()
    def trapezoidRamp_setTargetVelocity(self, value, axis):
        raise NotImplementedError()
    def trapezoidRamp_getTargetVelocity(self, axis):
        raise NotImplementedError()
    def trapezoidRamp_setActualVelocity(self, value, axis):
        raise NotImplementedError()
    def trapezoidRamp_getActualVelocity(self, axis):
        raise NotImplementedError()
    def trapezoidRamp_setMaximumVelocity(self, value, axis):
        raise NotImplementedError()
    def trapezoidRamp_getMaximumVelocity(self, axis):
        raise NotImplementedError()
    def trapezoidRamp_setMaximumAcceleration(self, value, axis):
        raise NotImplementedError()
    def trapezoidRamp_getMaximumAcceleration(self, axis):
        raise NotImplementedError()
