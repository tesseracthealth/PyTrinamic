# Author: LK
# Created on: 21.08.2019

from PyTrinamic.features.Feature import Feature
from PyTrinamic.Motor.Motor import Motor

class TrapezoidRamp(Feature):
    @staticmethod
    def setTargetPosition(value, motor):
        return motor[TrapezoidRamp].setTargetPosition(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def getTargetPosition(motor):
        return motor[TrapezoidRamp].getTargetPosition(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def setActualPosition(value, motor):
        return motor[TrapezoidRamp].setActualPosition(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def getActualPosition(motor):
        return motor[TrapezoidRamp].getActualPosition(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def setTargetVelocity(value, motor):
        return motor[TrapezoidRamp].setTargetVelocity(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def getTargetVelocity(motor):
        return motor[TrapezoidRamp].getTargetVelocity(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def setActualVelocity(value, motor):
        return motor[TrapezoidRamp].setActualVelocity(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def getActualVelocity(motor):
        return motor[TrapezoidRamp].getActualVelocity(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def setMaximumVelocity(value, motor):
        return motor[TrapezoidRamp].setMaximumVelocity(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def getMaximumVelocity(motor):
        return motor[TrapezoidRamp].getMaximumVelocity(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def setMaximumAcceleration(value, motor):
        return motor[TrapezoidRamp].setMaximumAcceleration(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def getMaximumAcceleration(motor):
        return motor[TrapezoidRamp].getMaximumAcceleration(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def setRampMode(value, motor):
        return motor[TrapezoidRamp].setRampMode(value, motor.getFeatureProviderMeta(TrapezoidRamp)[2])
    @staticmethod
    def getRampMode(motor):
        return motor[TrapezoidRamp].getRampMode(motor.getFeatureProviderMeta(TrapezoidRamp)[2])
