#!/usr/bin/env python3
'''
Dump all register values of the TMC4330 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 06.02.2020

@author: JM
'''
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC4330_eval import TMC4330_eval

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC4330 = TMC4330_eval(myInterface)

print("GENERAL_CONF:                           0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.GENERAL_CONF)))
print("REFERENCE_CONF:                         0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.REFERENCE_CONF)))
print("START_CONF:                             0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.START_CONF)))
print("INPUT_FILT_CONF:                        0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.INPUT_FILT_CONF)))
print("SCALE_CONF:                             0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SCALE_CONF)))
print("ENC_IN_CONF:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_IN_CONF)))
print("ENC_IN_DATA:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_IN_DATA)))
print("STEP_CONF:                              0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.STEP_CONF)))
print("SPI_STATUS_SELECTION:                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SPI_STATUS_SELECTION)))
print("EVENT_CLEAR_CONF:                       0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.EVENT_CLEAR_CONF)))
print("INTR_CONF:                              0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.INTR_CONF)))
print("EVENTS:                                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.EVENTS)))
print("STATUS:                                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.STATUS)))
print("STP_LENGTH_ADD___DIR_SETUP_TIME:        0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.STP_LENGTH_ADD___DIR_SETUP_TIME)))
print("START_OUT_ADD:                          0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.START_OUT_ADD)))
print("GEAR_RATIO:                             0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.GEAR_RATIO)))
print("START_DELAY:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.START_DELAY)))
print("CLK_GATING_DELAY:                       0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CLK_GATING_DELAY)))
print("STDBY_DELAY:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.STDBY_DELAY)))
print("PWM_VMAX:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PWM_VMAX)))
print("CL_ANGLES:                              0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CL_ANGLES)))
print("HOME_SAFETY_MARGIN:                     0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.HOME_SAFETY_MARGIN)))
print("PWM_FREQ:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PWM_FREQ)))
print("RAMPMODE:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.RAMPMODE)))
print("XACTUAL:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.XACTUAL)))
print("VACTUAL:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VACTUAL)))
print("AACTUAL:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.AACTUAL)))
print("VMAX:                                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VMAX)))
print("VSTART:                                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VSTART)))
print("VSTOP:                                  0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VSTOP)))
print("VBREAK:                                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VBREAK)))
print("AMAX:                                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.AMAX)))
print("DMAX:                                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.DMAX)))
print("ASTART:                                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ASTART)))
print("DFINAL:                                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.DFINAL)))
print("DSTOP:                                  0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.DSTOP)))
print("BOW1:                                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.BOW1)))
print("BOW2:                                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.BOW2)))
print("BOW3:                                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.BOW3)))
print("BOW4:                                   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.BOW4)))
print("CLK_FREQ:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CLK_FREQ)))
print("POS_COMP:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.POS_COMP)))
print("VIRT_STOP_LEFT:                         0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VIRT_STOP_LEFT)))
print("VIRT_STOP_RIGHT:                        0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VIRT_STOP_RIGHT)))
print("X_HOME:                                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_HOME)))
print("X_LATCH___REV_CNT___X_RANGE:            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_LATCH___REV_CNT___X_RANGE)))
print("XTARGET:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.XTARGET)))
print("X_PIPE0:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE0)))
print("X_PIPE1:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE1)))
print("X_PIPE2:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE2)))
print("X_PIPE3:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE3)))
print("X_PIPE4:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE4)))
print("X_PIPE5:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE5)))
print("X_PIPE6:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE6)))
print("X_PIPE7:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.X_PIPE7)))
print("SH_REG0:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG0)))
print("SH_REG1:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG1)))
print("SH_REG2:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG2)))
print("SH_REG3:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG3)))
print("SH_REG4:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG4)))
print("SH_REG5:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG5)))
print("SH_REG6:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG6)))
print("SH_REG7:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG7)))
print("SH_REG8:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG8)))
print("SH_REG9:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG9)))
print("SH_REG10:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG10)))
print("SH_REG11:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG11)))
print("SH_REG12:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG12)))
print("SH_REG13:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SH_REG13)))
print("CLK_Gating___SW_Reset:                  0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CLK_Gating___SW_Reset)))
print("ENC_POS:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_POS)))
print("ENC_LATCH___ENC_RESET_VAL:              0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_LATCH___ENC_RESET_VAL)))
print("ENC_POS_DEV___CL_TR_TOLERANCE:          0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_POS_DEV___CL_TR_TOLERANCE)))
print("ENC_POS_DEV_TOL:                        0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_POS_DEV_TOL)))
print("ENC_IN_RES___ENC_CONST:                 0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_IN_RES___ENC_CONST)))
print("ENC_OUT_RES:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_OUT_RES)))
print("SER_CLK_IN_HIGH_LOW:                    0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SER_CLK_IN_HIGH_LOW)))
print("SSI_IN_CLK_DELAY___SSI_IN_WTIME:        0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SSI_IN_CLK_DELAY___SSI_IN_WTIME)))
print("SER_PTIME:                              0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.SER_PTIME)))
print("CL_OFFSET:                              0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CL_OFFSET)))
print("PID_VEL___PID_P___CL_VMAX_CALC_P:       0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PID_VEL___PID_P___CL_VMAX_CALC_P)))
print("PID_ISUM_RD___PID_I___CL_VMAX_CALC_I:   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PID_ISUM_RD___PID_I___CL_VMAX_CALC_I)))
print("PID_D___CL_DELTA_P:                     0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PID_D___CL_DELTA_P)))
print("PID_E___PID_I_CLIP___PID_D_CLKDIV:      0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PID_E___PID_I_CLIP___PID_D_CLKDIV)))
print("PID_DV_CLIP:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PID_DV_CLIP)))
print("PID_TOLERANCE___CL_TOLERANCE:           0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.PID_TOLERANCE___CL_TOLERANCE)))
print("CL_VMIN_EMF:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CL_VMIN_EMF)))
print("CL_VADD_EMF:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CL_VADD_EMF)))
print("ENC_VEL_ZERO:                           0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_VEL_ZERO)))
print("ENC_VMEAN_SER_ENC_VARIATION_CL_CYCLE:   0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_VMEAN_SER_ENC_VARIATION_CL_CYCLE)))
print("V_ENC:                                  0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.V_ENC)))
print("V_ENC_MEAN:                             0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.V_ENC_MEAN)))
print("ADDR_TO_ENC:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ADDR_TO_ENC)))
print("DATA_TO_ENC:                            0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.DATA_TO_ENC)))
print("MSLUT__:                                0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.MSLUT__)))
print("MSLUTSEL:                               0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.MSLUTSEL)))
print("MSCNT:                                  0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.MSCNT)))
print("USTEPTA_B:                              0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.USTEPTA_B)))
print("USTEPA_B_SCALE:                         0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.USTEPA_B_SCALE)))
print("CIRCULAR_DEC:                           0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.CIRCULAR_DEC)))
print("ENC_COMP____:                           0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.ENC_COMP____)))
print("START_SIN___:                           0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.START_SIN___)))
print("VERSION_NO:                             0x{0:08X}".format(TMC4330.readRegister(TMC4330.registers.VERSION_NO)))

myInterface.close()