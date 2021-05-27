# Author: LK
# Test LinearRamp feature hierarchy in a dummy-manner.

def test_LinearRamp_dummy(instance):
    instance.setTargetPosition(0, 1)
    instance.setActualPosition(0, 1)
    instance.setTargetVelocity(0, 1)
    instance.setMaxVelocity(0, 1)
    instance.setMaxAcceleration(0, 1)
    print(instance.getTargetPosition(0))
    print(instance.getActualPosition(0))
    print(instance.getTargetVelocity(0))
    print(instance.getActualVelocity(0))
    print(instance.getMaxVelocity(0))
    print(instance.getMaxAcceleration(0))
