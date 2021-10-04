from ad import Ad
from advertiser import Advertiser
from base_model import BaseAdvertising

def main():
    baseAdvertising = BaseAdvertising()
    
    advertise1 = Advertiser(1,"name1")
    advertise2 = Advertiser(2,"name2")

    ad1 = Ad(1,"title1", "img-url1", "link1", advertise1)
    ad2 = Ad(2,"title2", "img-url2", "link2", advertise2)

    print(baseAdvertising.describeMe())
    print(ad2.describeMe())
    print(advertise1.describeMe())

    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad2.incViews()
    ad1.incClicks()
    ad1.incClicks()
    ad2.incClicks()

    print(advertise2.getName())
    advertise2.setName("new name")
    print(advertise2.getName())

    print(ad1.getClicks())
    print(advertise2.getClicks())
    print(Advertiser.getTotalClicks())
    print(Advertiser.help())


if __name__ == "__main__":
    main()