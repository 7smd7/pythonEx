class BaseAdvertising():

    def __init__(self,id = 0):
        self.__id = id
        self.__clicks = 0
        self.__views = 0
    
    def getClicks(self):
        return self.__clicks
    
    def incClicks(self):
        self.__clicks += 1
    
    def getViews(self):
        return self.__views

    def incViews(self):
        self.__views += 1

    def describeMe(self):
        return "It's description of BaseAdvertising, the parent of Ad and Advertiser."