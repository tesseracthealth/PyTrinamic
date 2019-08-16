'''
Created on 09.01.2019

@author: LK, ED, LH
'''

from PyTrinamic.evalboards.Evalboard import Evalboard
from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.TrapezoidRampModule import TrapezoidRampModule

class TMC5130_eval(Evalboard, StallGuard2Module, TrapezoidRampModule):
    """
    This class represents a TMC5130 Evaluation board.

    Communication is done over the TMCL commands writeMC and readMC. An
    implementation without TMCL may still use this class if these two functions
    are provided properly. See __init__ for details on the function
    requirements.
    """

    __PIN_MAP = [
        # (pin_ic, pin_board)
        (2, 15),
        (3, 22),
        (4, 23),
        (5, 24),
        (7, 25),
        (8, 9),
        (9, 10),
        (23, 4),
        (24, 6),
        (25, 5),
        (26, 30),
        (27, 29),
        (28, 28)
    ]

    __AXIS_PARAMETERS = {
        "par::TargetPosition": 0,
        "par::ActualPosition": 1,
        "par::TargetVelocity": 2,
        "par::ActualVelocity": 3,
        "par::MaxVelocity": 4,
        "par::MaxAcceleration": 5,
        "par::MaxCurrent": 6,
        "par::StandbyCurrent": 7,
        "par::PositionReachedFlag": 8,
        "par::RightEndstop": 10,
        "par::LeftEndstop": 11,
        "par::AutomaticRightStop": 12,
        "par::AutomaticLeftStop": 13,
        "par::SW_MODE": 14,
        "par::A1": 15,
        "par::V1": 16,
        "par::MaxDeceleration": 17,
        "par::D1": 18,
        "par::StartVelocity": 19,
        "par::StopVelocity": 20,
        "par::RampWaitTime": 21,
        "par::THIGH": 23,
        "par::VDCMIN": 24,
        "par::HighSpeedChopperMode": 27,
        "par::HighSpeedFullstepMode": 28,
        "par::MeasuredSpeed": 29,
        "par::I_scale_analog": 33,
        "par::internal_Rsense": 34,
        "par::MicrostepResolution": 140,
        "par::ChopperBlankTime": 162,
        "par::ConstantTOffMode": 163,
        "par::DisableFastDecayComparator": 164,
        "par::ChopperHysteresisEnd": 165,
        "par::ChopperHysteresisStart": 166,
        "par::TOff": 167,
        "par::SEIMIN": 168,
        "par::SECDS": 169,
        "par::smartEnergyHysteresis": 170,
        "par::SECUS": 171,
        "par::smartEnergyHysteresisStart": 172,
        "par::SG2FilterEnable": 173,
        "par::SG2Threshold": 174,
        "par::VSense": 179,
        "par::smartEnergyActualCurrent": 180,
        "par::smartEnergyStallVelocity": 181,
        "par::smartEnergyThresholdSpeed": 182,
        "par::RandomTOffMode": 184,
        "par::ChopperSynchronization": 185,
        "par::PWMThresholdSpeed": 186,
        "par::PWMGrad": 187,
        "par::PWMAmplitude": 188,
        "par::PWMFrequency": 191,
        "par::PWMAutoscale": 192,
        "par::FreewheelingMode": 204,
        "par::LoadValue": 206,
        "par::EncoderPosition": 209,
        "par::EncoderResolution": 210
    }

    def __init__(self, moduleId=1, connection=None, parent=None):
        super().__init__(moduleId, connection, parent)
        self.setIC(TMC5130(channel=0, moduleId=self.getModuleId(), connection=self.getConnection()))

    # Use the motion controller functions for register access
    def writeRegister(self, channel, registerAddress, value):
        del channel
        self.getIC().writeRegister(registerAddress, value)

    def readRegister(self, channel, registerAddress, signed=False):
        del channel
        return self.getIC().readRegister(registerAddress, signed)

    def axisParameter(self, strParameter):
        return self.__AXIS_PARAMETERS.get(strParameter)

    # Motion Control functions
    def rotate(self, value):
        self.trapezoidRamp_setMaximumAcceleration(0, 1000)
        if value >= 0:
            self.trapezoidRamp_setTargetVelocity(0, value)
            self.getIC().writeRegisterField(self.getIC().fields.RAMPMODE, 1)
        else:
            self.trapezoidRamp_setTargetVelocity(0, -value)
            self.getIC().writeRegisterField(self.getIC().fields.RAMPMODE, 2)

    def stop(self):
        self.rotate(0)

    def moveTo(self, position, velocity):
        self.getIC().writeRegisterField(self.getIC().fields.RAMPMODE, 0)
        if velocity != 0:
            self.trapezoidRamp_setTargetVelocity(0, value)
        self.trapezoidRamp_setTargetPosition(0, value)

    def moveBy(self, motor, distance, velocity):
        position = self.trapezoidRamp_getTargetPosition(0)
        self.moveTo(motor, position + distance, velocity)
        return position + distance
