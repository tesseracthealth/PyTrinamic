# Created on: 09.08.2019
# Author: LK

import PyTrinamic
from PyTrinamic.modules.Landungsbruecke import Landungsbruecke
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
import time

### Parameters #################################################################
VELOCITY     = 100000
ACCELERATION = 1000
SG_VELOCITY  = 50000

SG_THRESHOLD = 6

# Delay between Demo steps
DELAY        = 1
# En/Disable switching direction after each stall
CHANGE_DIR   = True
################################################################################

PyTrinamic.showInfo()

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
eval = TMC5130_eval(myInterface)
module = Landungsbruecke(myInterface)

connection, evalboard, moduleId=None

module = Landungsbruecke()
