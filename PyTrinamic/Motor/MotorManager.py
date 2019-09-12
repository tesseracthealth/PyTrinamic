# Author: LK
# Created on: 22.08.2019

class MotorManager(object):
    def __init__(self, *modules):
        self.__motors = []
        for module in modules:
            self.__motors += module.getMotors()
    def getMotors(self):
        return self.__motors
    # Thread safe alternative for __getitem__ + feature instruction
    @staticmethod
    def execute(motor, feature, instruction, *args):
        return getattr(motor[feature], instruction)(*args, motor.getFeatureProviderMeta(feature)[2])
