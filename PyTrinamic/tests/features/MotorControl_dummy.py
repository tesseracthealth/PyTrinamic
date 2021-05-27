# Author: LK
# Test MotorControl feature hierarchy in a dummy-manner.

def test_MotorControl_dummy(instance):
    instance.rotate(0, 1)
    instance.stop(0)
    instance.moveTo(0, 1, 1)
    instance.moveBy(0, 1, 1)
