# Created on: 09.08.2019
# Author: LK

import PyTrinamic

from PyTrinamic.modules.Landungsbruecke import Landungsbruecke
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.features.StallGuard2 import StallGuard2
from PyTrinamic.helpers import TMC_helpers
import time
import logging

### Parameters #################################################################
VELOCITY     = 100000
ACCELERATION = 1000
SG_VELOCITY  = 50000

SG_THRESHOLD = 6

# Delay between Demo steps
DELAY        = 2
# En/Disable switching direction after each stall
CHANGE_DIR   = True
################################################################################

TMC_helpers.showInfo()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

myInterface = ConnectionManager().connect()
module = Landungsbruecke(connection=myInterface)
eval = TMC5130_eval(parent=module)

if(module.hasFeature(StallGuard2, recursive=True)):
    logger.info("Landungsbruecke (Eval) or IC provide feature StallGuard2!")
else:
    raise ValueError("Neither Landungsbruecke (Eval) nor IC provide feature StallGuard2!")

eval.stallGuard2_setStallGuardThreshold(0, SG_THRESHOLD)
eval.stallGuard2_setStallVelocity(0, SG_VELOCITY)

direction = 1

try:
    while True:
        logger.info("Rotating")
        eval.rotate(direction * VELOCITY)
        logger.info("Waiting for stall ...")
        while eval.readRegisterField(0, eval.fields.EVENT_STOP_SG) == 0:
            pass
        logger.info("Stall detected!")
        time.sleep(DELAY)
        if CHANGE_DIR:
            # Flip the direction around
            direction = -direction
        # Clear event flag
        eval.readRegisterField(0, eval.fields.EVENT_STOP_SG)
except KeyboardInterrupt:
    logger.info("Demo aborted by KeyboardInterrupt")

logger.info("Stopping motor")
eval.stop()

while eval.readRegisterField(0, eval.fields.STST) == 0:
    pass

myInterface.close()
