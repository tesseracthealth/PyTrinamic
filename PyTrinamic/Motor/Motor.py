class Motor(object):
    def __init__(self, index=0, channel=0, moduleId=1, connection=None, parent=None):
        # self.__features[StallGuard2] = [(StallGuard2IC, 1), (StallGuard2Module, 0)]
        self.__features = {}
        self.__index = index # Global index
        self.__channel  = channel
        self.__moduleId = moduleId
        self.__connection = connection
        self.__parent = parent
        if(parent):
            parent.addMotor(self)
            self.__channel = parent.getChannel()
            self.__moduleId = parent.getModuleId()
            self.__connection = parent.getConnection()
    def setIndex(self, index):
        self.__index = index
    def getIndex(self):
        return self.__index
    def getFeatureProvider(self, feature):
        provider = self.__features[feature][0][0]
        provider.setAxis(self.getIndex())
        return provider
    def __getitem__(self, key):
        return self.getFeatureProvider(key)
    def addFeatureProvider(self, feature, provider, priority):
        if(not self.__features.get(feature)):
            self.__features[feature] = []
        self.__features[feature].append((provider(axis=self.__index), priority))
        self.__features[feature].sort(key=provider[1])
    def removeFeatureProvider(self, feature, provider):
        if(self.__features.get(feature)): # List exists
            self.__features[feature] = [p for p in self.__features[feature] if p[0].__class__ != provider]
        if(not self.__features.get(feature)): # List empty
            del self.__features[feature]
    def setFeatureProvider(self, feature, provider):
        self.__features[feature][0], self.__features[feature][self.__features[feature].index([p for p in self.__features[feature] if p[0].__class__ == provider][0])] = self.__features[feature][self.__features[feature].index([p for p in self.__features[feature] if p[0].__class__ == provider][0])], self.__features[feature][0]
