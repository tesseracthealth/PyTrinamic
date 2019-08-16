from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp

class TrapezoidRampModule(TrapezoidRamp):
    def trapezoidRamp_setTargetPosition(self, axis, value):
        self.setAxisParameter(self.axisParameter("par::TargetPosition"), axis, value)
    def trapezoidRamp_getTargetPosition(self, axis):
        return self.getAxisParameter(self.axisParameter("par::TargetPosition"), axis)
    def trapezoidRamp_setActualPosition(self, axis, value):
        self.setAxisParameter(self.axisParameter("par::ActualPosition"), axis, value)
    def trapezoidRamp_getActualPosition(self, axis):
        return self.getAxisParameter(self.axisParameter("par::ActualPosition"), axis)
    def trapezoidRamp_setTargetVelocity(self, axis, value):
        self.setAxisParameter(self.axisParameter("par::TargetVelocity"), axis, value)
    def trapezoidRamp_getTargetVelocity(self, axis):
        return self.getAxisParameter(self.axisParameter("par::TargetVelocity"), axis)
    def trapezoidRamp_setActualVelocity(self, axis, value):
        self.setAxisParameter(self.axisParameter("par::ActualVelocity"), axis, value)
    def trapezoidRamp_getActualVelocity(self, axis):
        return self.getAxisParameter(self.axisParameter("par::ActualVelocity"), axis)
    def trapezoidRamp_setMaximumVelocity(self, axis, value):
        self.setAxisParameter(self.axisParameter("par::MaxVelocity"), axis, value)
    def trapezoidRamp_getMaximumVelocity(self, axis):
        return self.getAxisParameter(self.axisParameter("par::MaxVelocity"), axis)
    def trapezoidRamp_setMaximumAcceleration(self, axis, value):
        self.setAxisParameter(self.axisParameter("par::MaxAcceleration"), axis, value)
    def trapezoidRamp_getMaximumAcceleration(self, axis):
        return self.getAxisParameter(self.axisParameter("par::MaxAcceleration"), axis)
