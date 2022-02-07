"""
Move a motor back and forth using velocity and position mode of the TMC5072
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5072_eval

pytrinamic.show_info()
myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:
    # Create TMC5062-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5072_eval(myInterface)
    mc = eval_board.ics[0]
    motor0 = eval_board.motors[0]
    print(motor0)
    motor1 = eval_board.motors[1]
    print(motor1)

    print("Preparing parameter for motor 0...")
#    eval_board.write_register(mc.REG.A1_M1, 1000)
#    eval_board.write_register(mc.REG.V1_M1, 50000)
#    eval_board.write_register(mc.REG.D1_M1, 500)
#    eval_board.write_register(mc.REG.DMAX_M1, 500)
#    eval_board.write_register(mc.REG.VSTART_M1, 0)
#    eval_board.write_register(mc.REG.VSTOP_M1, 10)
#    eval_board.write_register(mc.REG.AMAX_M1, 1000)

    motor0.set_axis_parameter(motor0.AP.MaxVelocity, 100000)
    motor0.set_axis_parameter(motor0.AP.MaxAcceleration, 1000)
    motor0.set_axis_parameter(motor0.AP.A1, 1000)
    motor0.set_axis_parameter(motor0.AP.V1, 0)
    motor0.set_axis_parameter(motor0.AP.MaxDeceleration, 500)
    motor0.set_axis_parameter(motor0.AP.D1, 500)
    motor0.set_axis_parameter(motor0.AP.StartVelocity, 0)
    motor0.set_axis_parameter(motor0.AP.StopVelocity, 20)
    motor0.set_axis_parameter(motor0.AP.RampWaitTime, 0)

    print("Preparing parameter for motor 1...")
#    eval_board.write_register(mc.REG.A1_M2, 1000)
#    eval_board.write_register(mc.REG.V1_M2, 50000)
#    eval_board.write_register(mc.REG.D1_M2, 500)
#    eval_board.write_register(mc.REG.DMAX_M2, 500)
#    eval_board.write_register(mc.REG.VSTART_M2, 0)
#    eval_board.write_register(mc.REG.VSTOP_M2, 10)
#    eval_board.write_register(mc.REG.AMAX_M2, 1000)

    motor1.set_axis_parameter(motor1.AP.MaxVelocity, 100000)
    motor1.set_axis_parameter(motor1.AP.MaxAcceleration, 1000)
    motor1.set_axis_parameter(motor1.AP.A1, 1000)
    motor1.set_axis_parameter(motor1.AP.V1, 0)
    motor1.set_axis_parameter(motor1.AP.MaxDeceleration, 500)
    motor1.set_axis_parameter(motor1.AP.D1, 500)
    motor1.set_axis_parameter(motor1.AP.StartVelocity, 0)
    motor1.set_axis_parameter(motor1.AP.StopVelocity, 20)
    motor1.set_axis_parameter(motor1.AP.RampWaitTime, 0)

    # Clear actual positions
    motor0.actual_position = 0
    motor1.actual_position = 0

    print("Rotating motor 1...")
    motor0.rotate(10*25600)
    time.sleep(3)

    print("Stopping motor 1...")
    motor0.stop()
    time.sleep(1)

    print("Rotating motor 2...")
    motor1.rotate(10*25600)
    time.sleep(3)

    print("Stopping motor 2...")
    motor1.stop()
    time.sleep(1)

    print("Moving back to 0...")
    # eval_board.move_to(0, 0, 100000)
    # eval_board.move_to(1, 0, 100000)
    motor0.move_to(0, 100000)
    motor1.move_to(0, 100000)

    time.sleep(1)

    # Wait until position 0 is reached by both motors
    while (motor0.actual_position != 0) or (motor1.actual_position != 0):
        print("Actual position motor0: " + str(motor0.actual_position) + "   "
              + "actual position motor1: " + str(motor1.actual_position))
        time.sleep(0.2)

    print("Reached position 0")

print("\nReady.")