from bitFlyerAPI import BF_API

class HttpAPI(BF_API):

    def __init__(self):
        super().__init__("https://api.bitflyer.com/v1/")

# test
if __name__ == "__main__":
    api = HttpAPI()
    print(api._call("getexecutions", product_code="BTC_JPY", count=1, before=0, after=0))