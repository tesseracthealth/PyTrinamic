# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp
from PyTrinamic.features.FeatureProvider import FeatureProvider

class TrapezoidRampModule(TrapezoidRamp, FeatureProvider):
    def setTargetPosition(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::TargetPosition"), (axis if axis else self.getAxis()), value)
    def getTargetPosition(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::TargetPosition"), (axis if axis else self.getAxis()), signed=True)
    def setActualPosition(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::ActualPosition"), (axis if axis else self.getAxis()), value)
    def getActualPosition(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::ActualPosition"), (axis if axis else self.getAxis()), signed=True)
    def setTargetVelocity(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::TargetVelocity"), (axis if axis else self.getAxis()), value)
    def getTargetVelocity(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::TargetVelocity"), (axis if axis else self.getAxis()))
    def setActualVelocity(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::ActualVelocity"), (axis if axis else self.getAxis()), value)
    def getActualVelocity(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::ActualVelocity"), (axis if axis else self.getAxis()))
    def setMaximumVelocity(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::MaxVelocity"), (axis if axis else self.getAxis()), value)
    def getMaximumVelocity(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::MaxVelocity"), (axis if axis else self.getAxis()))
    def setMaximumAcceleration(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::MaxAcceleration"), (axis if axis else self.getAxis()), value)
    def getMaximumAcceleration(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::MaxAcceleration"), (axis if axis else self.getAxis()))
