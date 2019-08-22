# Created on: 09.08.2019
# Author: LK

from PyTrinamic.helpers import TMC_helpers
from PyTrinamic.Motor.Motor import Motor

class IC(object):
    def __init__(self, channel=0, moduleId=1, connection=None, parent=None):
        self.__motors = []
        self.__channel  = channel
        self.__moduleId = moduleId
        self.__connection = connection
        self.__parent = parent
        if(parent):
            parent.addSubmodule(self)
            self.__connection = parent.getConnection()
            self.__moduleId = parent.getModuleId()
        for i in range(0, self._MOTOR_COUNT, 1):
            self.addMotor(Motor(parent=self))
    def getConnection(self):
        return self.__connection
    def setConnection(self, connection):
        self.__connection = connection
    def getChannel(self):
        return self.__channel
    def setChannel(self, channel):
        self.__channel = channel
    def getModuleId(self):
        return self.__moduleId
    def setModuleId(self, moduleId):
        self.__moduleId = moduleId
    def addMotor(self, motor):
        for feature in [f for f in self.__bases__ if instanceof(f, Feature)]:
            motor.addFeatureProvider(feature, self, 1, len(self.__motors))
        self.__motors.append(motor)
        if(self.__parent):
            self.__parent.addMotor(motor)
    def removeMotor(self, motor):
        self.__motors.remove(motor)
        if(self.__parent):
            self.__parent.removeMotor(motor)
        for i, motor in enumerate(self.__motors):
            motor.setProviderIndex(self, i)
    def getMotors(self):
        return self.__motors
    def hasFeature(self, feature, recursive=False):
        if(isinstance(self, feature)):
            return True
        elif(recursive):
            for motor in self.getMotors():
                if motor.hasFeature(feature, recursive):
                    return True
        return False
    def showChipInfo(self):
        raise NotImplementedError()
    def writeRegister(self, registerAddress, value):
        return self.getConnection().writeMC(self.getChannel(), registerAddress, value, self.getModuleId())
    def readRegister(self, registerAddress, signed=False):
        return self.getConnection().readMC(self.getChannel(), registerAddress, self.getModuleId(), signed)
    def writeRegisterField(self, field, value):
        raise NotImplementedError()
    def readRegisterField(self, field):
        raise NotImplementedError()
