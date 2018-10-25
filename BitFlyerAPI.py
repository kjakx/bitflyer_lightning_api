from public_api import PublicAPI
from private_api import PrivateAPI

class BitFlyerAPI(PublicAPI, PrivateAPI):
    def __init__(self, key=None, secret=None):
        super().__init__(key, secret)

if __name__ == "__main__":
    api = BitFlyerAPI( \
        key = "YOUR_API_KEY", \
        secret = "YOUR_API_SECRET")
    print(api.getBalance())
    print(api.getChats("2018-10-25T00:00:00.000"))
    """
    print(api.sendChildOrder(\
                            product_code="FX_BTC_JPY", \
                            child_order_type="LIMIT", \
                            price=114514, \
                            side="BUY", \
                            size=0.01))
    """
    api_nonkey = BitFlyerAPI()
    print(api.getMarkets())