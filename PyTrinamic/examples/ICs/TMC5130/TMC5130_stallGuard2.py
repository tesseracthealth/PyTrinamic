# Created on: 09.08.2019
# Author: LK

import PyTrinamic

from PyTrinamic.modules.Landungsbruecke import Landungsbruecke
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130
from PyTrinamic.features.StallGuard2 import StallGuard2
from PyTrinamic.helpers import TMC_helpers
import time
import logging

### Parameters #################################################################
VELOCITY     = 100000
ACCELERATION = 1000
SG_VELOCITY  = 50000

SG_THRESHOLD = 8

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
ic = TMC5130(connection=myInterface)

if(ic.hasFeature(StallGuard2)):
    logger.info("IC provides feature StallGuard2!")

ic.stallGuard2_setStallGuardThreshold(0, SG_THRESHOLD)
ic.stallGuard2_setStallVelocity(0, SG_VELOCITY)

direction = 1

try:
    while True:
        logger.info("Rotating")
        ic.rotate(0, direction * VELOCITY)
        logger.info("Waiting for stall ...")
        while ic.readRegisterField(ic.fields.EVENT_STOP_SG) == 0:
            pass
        logger.info("Stall detected!")
        time.sleep(DELAY)
        if CHANGE_DIR:
            # Flip the direction around
            direction = -direction
        # Clear event flag
        ic.readRegisterField(ic.fields.EVENT_STOP_SG)
except KeyboardInterrupt:
    logger.info("Demo aborted by KeyboardInterrupt")

logger.info("Stopping motor")
ic.stop(0)

while ic.readRegisterField(ic.fields.STST) == 0:
    pass

myInterface.close()
