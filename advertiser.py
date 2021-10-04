from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
    
    totalClicks = 0
    otherId = {};

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name
        if id in Advertiser.otherId.keys():
            raise NameError('this id is used')
        else:
            Advertiser.otherId[id] = 1
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    @staticmethod
    def help():
        return "for define Advertiser you shoud input uniq id and name."

    def describeMe(self):
        return "It's description of Advertiser, the child of BaseAdvertiser."

    def incClicks(self):
        super().incClicks()
        Advertiser.totalClicks += 1
    
    @staticmethod
    def getTotalClicks():
        return Advertiser.totalClicks