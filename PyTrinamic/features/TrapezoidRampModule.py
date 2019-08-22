# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp

class TrapezoidRampModule(TrapezoidRamp):
    def trapezoidRamp_setTargetPosition(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::TargetPosition"), (axis if axis else self.getAxis()), value)
    def trapezoidRamp_getTargetPosition(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::TargetPosition"), (axis if axis else self.getAxis()), signed=True)
    def trapezoidRamp_setActualPosition(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::ActualPosition"), (axis if axis else self.getAxis()), value)
    def trapezoidRamp_getActualPosition(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::ActualPosition"), (axis if axis else self.getAxis()), signed=True)
    def trapezoidRamp_setTargetVelocity(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::TargetVelocity"), (axis if axis else self.getAxis()), value)
    def trapezoidRamp_getTargetVelocity(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::TargetVelocity"), (axis if axis else self.getAxis()))
    def trapezoidRamp_setActualVelocity(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::ActualVelocity"), (axis if axis else self.getAxis()), value)
    def trapezoidRamp_getActualVelocity(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::ActualVelocity"), (axis if axis else self.getAxis()))
    def trapezoidRamp_setMaximumVelocity(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::MaxVelocity"), (axis if axis else self.getAxis()), value)
    def trapezoidRamp_getMaximumVelocity(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::MaxVelocity"), (axis if axis else self.getAxis()))
    def trapezoidRamp_setMaximumAcceleration(self, value, axis=None):
        self.setAxisParameter(self.axisParameter("par::MaxAcceleration"), (axis if axis else self.getAxis()), value)
    def trapezoidRamp_getMaximumAcceleration(self, axis=None):
        return self.getAxisParameter(self.axisParameter("par::MaxAcceleration"), (axis if axis else self.getAxis()))
