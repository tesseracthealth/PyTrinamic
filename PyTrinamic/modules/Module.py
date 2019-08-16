# Created on: 09.08.2019
# Author: LK

class Module(object):
    def __init__(self, moduleId=1, connection=None, parent=None):
        self.__moduleId = moduleId
        self.__submodules = []
        self.__connection = connection
        if(parent):
            self.__connection = parent.getConnection()
        if(connection):
            self.__connection = connection
    def setConnection(self, connection):
        self.__connection = connection
    def setModuleId(self, moduleId):
        self.__moduleId = moduleId
    def getConnection(self):
        return self.__connection
    def getModuleId(self):
        return self.__moduleId
    def addSubmodule(self, submodule):
        self.__submodules.append(submodule)
    def removeSubmodule(self, submodule):
        self.__submodules.remove(submodule)
    def getSubmodules(self):
        return self.__submodules
    def hasFeature(self, feature, recursive=False):
        if(isinstance(self, feature)):
            return True
        elif(recursive):
            for submodule in self.getSubmodules():
                if submodule.hasFeature(feature, recursive):
                    return True
        return False
    def hasSubmodule(self, submodule, recursive=False):
        del recursive
        return (submodule in self.getSubmodules())
    def axisParameter(self, strParameter):
        raise NotImplementedError()
    def getAxisParameter(self, commandType, axis, signed=False):
        return self.getConnection().getAxisParameter(commandType, axis, self.getModuleId(), signed)
    def setAxisParameter(self, commandType, axis, value):
        return self.getConnection().setAxisParameter(commandType, axis, value, self.getModuleId())
