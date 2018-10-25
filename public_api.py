from apihitter import ApiHitter

class PublicAPI(ApiHitter):
    def __init__(self, key=None, secret=None):
        super().__init__(key, secret)

    def getMarkets(self):
        return self.request("GET", "/v1/getmarkets")
    
    def getMarkets_usa(self):
        return self.request("GET", "/v1/getmarkets/usa")     

    def getMarkets_eu(self):
        return self.request("GET", "/v1/getmarkets/eu")

    def getBoard(self, product_code):
        return self.request("GET", "/v1/getboard", product_code=product_code)

    def getTicker(self, product_code):
        return self.request("GET", "/v1/getticker", product_code=product_code)

    def getExecutions(self, product_code, count=100, before=0, after=0):
        return self.request("GET", "/v1/getexecutions", \
                            count=count, before=before, after=after)

    def getChats(self, from_date=""):
        return self.request("GET", "/v1/getchats", from_date=from_date)

    def getChats_usa(self, from_date=""):
        return self.request("GET", "/v1/getchats/usa", from_date=from_date)

    def getChats_eu(self, from_date=""):
        return self.request("GET", "/v1/getchats/eu", from_date=from_date)

    def getHealth(self, product_code):
        return self.request("GET", "/v1/gethealth", product_code=product_code)

    def getBoardState(self, product_code):
        return self.request("GET", "/v1/getboardstate", product_code=product_code)

# test
if __name__ == "__main__":
    api = PublicAPI(key="YOUR_API_KEY", \
                    secret="YOUR_API_SECRET" )
    print("markets:", api.getMarkets())
    code_fx = api.getMarkets()[1]['product_code']   # 'FX_BTC_JPY'
    board_fx = api.getBoard(code_fx)
    print("mid_price:", board_fx['mid_price'])
    print("best_bid:", board_fx['bids'][0])
    print("best_ask:", board_fx['asks'][0])
    ticker_fx = api.getTicker(code_fx)
    print("ticker:", ticker_fx)
    executions = api.getExecutions(code_fx, count=1)
    print("exec:", executions)
    chats = api.getChats(b"2018-10-22T00:00:00.000")
    print("last_chat:", chats[0])
    health = api.getHealth(code_fx)
    print("health:", health)
    board_state = api.getBoardState(code_fx)
    print("board_state:", board_state)
    print(str("よくできました"))