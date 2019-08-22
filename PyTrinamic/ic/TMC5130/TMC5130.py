'''
Created on 02.01.2019

@author: ed
'''

from PyTrinamic.ic.IC import IC
from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_register
from PyTrinamic.ic.TMC5130.TMC5130_register_variant import TMC5130_register_variant
from PyTrinamic.ic.TMC5130.TMC5130_fields import TMC5130_fields
from PyTrinamic.features.StallGuard2IC import StallGuard2IC
from PyTrinamic.features.TrapezoidRampIC import TrapezoidRampIC
from PyTrinamic.helpers import TMC_helpers

class TMC5130(IC, StallGuard2IC, TrapezoidRampIC):
    """
    Class for the TMC5130 IC
    """
    def __init__(self, channel=0, moduleId=1, connection=None, parent=None):
        super().__init__(channel, moduleId, connection, parent)

        self.registers  = TMC5130_register
        self.fields     = TMC5130_fields
        self.variants   = TMC5130_register_variant

        self._MOTOR_COUNT = 1

        self.addMotors(self._MOTOR_COUNT)

    def showChipInfo(self):
        print("TMC5130 chip info: ?")

    def writeRegisterField(self, field, value, axis=None):
        del axis
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0]), field[1], field[2], value))
    def readRegisterField(self, field, axis=None):
        del axis
        return TMC_helpers.field_get(self.readRegister(field[0]), field[1], field[2])

    # Motion Control functions
    def rotate(self, motor, value):
        if not(0 <= motor < self._MOTOR_COUNT):
            raise ValueError

        self.writeRegister(self.registers.AMAX, 1000)

        if value >= 0:
            self.writeRegister(self.registers.VMAX, value)
            self.writeRegister(self.registers.RAMPMODE, 1)
        else:
            self.writeRegister(self.registers.VMAX, -value)
            self.writeRegister(self.registers.RAMPMODE, 2)

    def stop(self, motor):
        self.rotate(motor, 0)

    def moveTo(self, motor, position, velocity):
        if not(0 <= motor < self._MOTOR_COUNT):
            raise ValueError

        self.writeRegister(self.registers.RAMPMODE, 0)

        if velocity != 0:
            self.writeRegister(self.registers.VMAX, velocity)

        self.writeRegister(self.registers.XTARGET, position)

    def moveBy(self, motor, distance, velocity):
        if not(0 <= motor < self._MOTOR_COUNT):
            raise ValueError

        position = self.readRegister(self.registers.XACTUAL, signed=True)

        self.moveTo(motor, position + distance, velocity)

        return position + distance

    def get_pin_state(self):
        pass
