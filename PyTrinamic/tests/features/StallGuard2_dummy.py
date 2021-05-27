# Author: LK
# Test StallGuard2 feature hierarchy in a dummy-manner.

def test_StallGuard2_dummy(instance):
    instance.setStallguard2Filter(0, 1)
    instance.setStallguard2Threshold(0, 1)
    instance.setStopOnStallVelocity(0, 1)
    print(instance.getStallguard2Filter(0))
    print(instance.getStallguard2Threshold(0))
    print(instance.getStopOnStallVelocity(0))
