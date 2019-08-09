# Created on: 09.08.2019
# Author: LK

import PyTrinamic

from PyTrinamic.modules.Landungsbruecke import Landungsbruecke
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.features.StallGuard2 import StallGuard2
import time
import logging

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

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
eval = TMC5130_eval(channel=0)
module = Landungsbruecke(connection=myInterface, evalboard=eval, moduleId=1)

if(module.hasFeature(StallGuard2())):
    logger.info("Landungsbruecke or Evalboard provides feature StallGuard2!")
else:
    raise ValueError("Neither Landungsbruecke nor Evalboard provide feature StallGuard2!")
