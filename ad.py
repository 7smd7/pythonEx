from base_model import BaseAdvertising

class Ad(BaseAdvertising):

    otherId = {};

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__link = link
        self.__imgUrl = imgUrl
        self.__advertiser = advertiser
        if id in Ad.otherId.keys():
            raise NameError('this id is used')
        else:
            Ad.otherId[id] = 1
    
    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getImgUrl(self,imgUrl):
        return self.__imgUrl

    def setImgUrl(self,imgUrl):
        self.__imgUrl = imgUrl

    def getLink(self):
        return self.__link

    def setLink(self,link):
        self.__link = link

    def setAdvertiser(self, advertiser):
        self.__advertiser = advertiser

    def describeMe(self):
        return "It's description of Ad, the child of BaseAdvertiser."

    def incClicks(self):
        super().incClicks()
        self.__advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.__advertiser.incViews()