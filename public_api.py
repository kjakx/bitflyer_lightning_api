from http_api import HttpAPI

class PublicAPI(HttpAPI):

    def __init__(self):

        super().__init__()

    def getMarkets(self):

        return self._call("getmarkets")
    
    def getMarkets_usa(self):

        return self._call("getmarkets/usa")     

    def getMarkets_eu(self):

        return self._call("getmarkets/eu")

    def getBoard(self, product_code):

        return self._call("getboard", product_code=product_code)

    def getTicker(self, product_code):

        return self._call("getticker", product_code=product_code)

    def getExec(self, product_code, count=100, before=0, after=0):

        return self._call("getexecutions", count=count, before=before, after=after)

    def getChats(self, from_date=""):

        return self._call("getchats", from_date=from_date)

    def getChats_usa(self, from_date=""):

        return self._call("getchats/usa", from_date=from_date)

    def getChats_eu(self, from_date=""):

        return self._call("getchats/eu", from_date=from_date)

    def getHealth(self, product_code):

        return self._call("gethealth", product_code=product_code)

    def getBoardState(self, product_code):

        return self._call("getboardstate", product_code=product_code)

# test
if __name__ == "__main__":

    api = PublicAPI()
    print("markets:", api.getMarkets())
    code_fx = api.getMarkets()[1]['product_code']   # 'FX_BTC_JPY'
    board_fx = api.getBoard(code_fx)
    print("mid_price:", board_fx['mid_price'])
    print("best_bid:", board_fx['bids'][0])
    print("best_ask:", board_fx['asks'][0])
    ticker_fx = api.getTicker(code_fx)
    print("ticker:", ticker_fx)
    executions = api.getExec(code_fx, count=1)
    print("exec:", executions)
    chats = api.getChats("2018-10-22T00:00:00.000+09:00")
    print("last_chat:", chats[len(chats) - 1])
    health = api.getHealth(code_fx)
    print("health:", health)
    board_state = api.getBoardState(code_fx)
    print("board_state:", board_state)
    print(str("よくできました"))