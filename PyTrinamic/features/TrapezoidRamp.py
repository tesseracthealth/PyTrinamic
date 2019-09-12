# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.Feature import Feature
from PyTrinamic.Motor.Motor import Motor

class TrapezoidRamp(Feature):
    def setTargetPosition(self, value, motor):
        return motor[TrapezoidRamp].setTargetPosition(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def getTargetPosition(self, motor):
        return motor[TrapezoidRamp].getTargetPosition(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def setActualPosition(self, value, motor):
        return motor[TrapezoidRamp].setActualPosition(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def getActualPosition(self, motor):
        return motor[TrapezoidRamp].getActualPosition(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def setTargetVelocity(self, value, motor):
        return motor[TrapezoidRamp].setTargetVelocity(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def getTargetVelocity(self, motor):
        return motor[TrapezoidRamp].getTargetVelocity(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def setActualVelocity(self, value, motor):
        return motor[TrapezoidRamp].setActualVelocity(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def getActualVelocity(self, motor):
        return motor[TrapezoidRamp].getActualVelocity(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def setMaximumVelocity(self, value, motor):
        return motor[TrapezoidRamp].setMaximumVelocity(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def getMaximumVelocity(self, motor):
        return motor[TrapezoidRamp].getMaximumVelocity(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def setMaximumAcceleration(self, value, motor):
        return motor[TrapezoidRamp].setMaximumAcceleration(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    def getMaximumAcceleration(self, motor):
        return motor[TrapezoidRamp].getMaximumAcceleration(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
