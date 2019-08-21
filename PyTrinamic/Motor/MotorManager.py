class MotorManager(object):
    def __init__(self, *modules):
        self.__motors = []
        for module in modules:
            
