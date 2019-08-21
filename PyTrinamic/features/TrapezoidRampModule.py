from PyTrinamic.features.TrapezoidRamp import TrapezoidRamp

class TrapezoidRampModule(TrapezoidRamp):
    def trapezoidRamp_setTargetPosition(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::TargetPosition"), axis, value)
    def trapezoidRamp_getTargetPosition(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::TargetPosition"), axis, signed=True)
    def trapezoidRamp_setActualPosition(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::ActualPosition"), axis, value)
    def trapezoidRamp_getActualPosition(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::ActualPosition"), axis, signed=True)
    def trapezoidRamp_setTargetVelocity(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::TargetVelocity"), axis, value)
    def trapezoidRamp_getTargetVelocity(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::TargetVelocity"), axis)
    def trapezoidRamp_setActualVelocity(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::ActualVelocity"), axis, value)
    def trapezoidRamp_getActualVelocity(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::ActualVelocity"), axis)
    def trapezoidRamp_setMaximumVelocity(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::MaxVelocity"), axis, value)
    def trapezoidRamp_getMaximumVelocity(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::MaxVelocity"), axis)
    def trapezoidRamp_setMaximumAcceleration(self, value, axis=None):
        if not axis:
            axis = self.getAxis()
        self.setAxisParameter(self.axisParameter("par::MaxAcceleration"), axis, value)
    def trapezoidRamp_getMaximumAcceleration(self, axis=None):
        if not axis:
            axis = self.getAxis()
        return self.getAxisParameter(self.axisParameter("par::MaxAcceleration"), axis)
