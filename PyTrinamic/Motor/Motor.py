# Author: LK
# Created on: 21.08.2019

class Motor(object):
    def __init__(self, channel=0, moduleId=1, connection=None, parent=None):
        # self.__features[StallGuard2] = [(StallGuard2IC, 1, 0), (StallGuard2Module, 0, 0)]
        self.__features = {}
        self.__channel  = channel
        self.__moduleId = moduleId
        self.__connection = connection
        self.__parent = parent
        if(parent):
            #parent.addMotor(self)
            self.__channel = parent.getChannel()
            self.__moduleId = parent.getModuleId()
            self.__connection = parent.getConnection()
    def setProviderIndex(self, provider, index):
        for feature in features:
            for prov in [p for p in self.__features[feature] if p[0] == provider]:
                prov[2] = index
    def getFeatureProvider(self, feature):
        provider = self.__features[feature][0]
        provider[0].setAxis(provider[2])
        return provider[0]
    def __getitem__(self, key):
        return self.getFeatureProvider(key)
    def addFeatureProvider(self, feature, provider, priority, index):
        if(not self.__features.get(feature)):
            self.__features[feature] = []
        self.__features[feature].append((provider, priority, index))
        self.__features[feature].sort(key=lambda prov: prov[1])
    def removeFeatureProvider(self, feature, provider):
        if(self.__features.get(feature)): # List exists
            self.__features[feature] = [p for p in self.__features[feature] if p[0] != provider]
        if(not self.__features.get(feature)): # List empty
            del self.__features[feature]
    def setFeatureProvider(self, feature, provider):
        to = self.__features[feature][self.__features[feature].index([p for p in self.__features[feature] if isinstance(p[0], provider)][0])]
        self.__features[feature][self.__features[feature].index([p for p in self.__features[feature] if isinstance(p[0], provider)][0])] = self.__features[feature][0]
        self.__features[feature][0] = to
    def hasFeature(self, feature):
        return (True if self.__features.get(feature) else False)
    def listFeatures(self):
        return self.__features.keys()
    def listFeatureProviders(self, feature):
        return [p[0] for p in self.__features[feature]]
    def listFeatureProviderMetas(self, feature):
        return self.__features[feature]
    def getFeatureProviderMeta(self, feature):
        return self.__features[feature][0]
