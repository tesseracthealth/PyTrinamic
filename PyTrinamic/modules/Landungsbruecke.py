'''
Created on 24.07.2019

@author: LK
'''

from PyTrinamic.modules.Module import Module

class Landungsbruecke(Module):
    __GLOBAL_PARAMETERS = {
        "par::VitalSignsErrorMask": 1,
        "par::DriversEnable": 2,
        "par::DebugMode": 3,
        "par::BoardAssignment": 4,
        "par::HWID": 5,
        "par::PinState": 6
    }
