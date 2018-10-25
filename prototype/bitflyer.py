import requests
import json

def _req2dic(url): # 呼び出す必要なし

    resp = requests.get(url)
    # print(resp)
    dic = json.loads(resp.content)
    return dic

def _urlBuilder(api_name, **kwargs): # 呼び出す必要なし

    url = 'https://api.bitflyer.com/v1/' + api_name + '/?'
    # print(len(kwargs))
    for i, (key, value) in enumerate(kwargs.items(), 1):
        url += (key + '=' + str(value))
        if i != len(kwargs):
            url += '&'
    # print(url)
    return url

def getMarkets(current="jpy"):

    """
    current: jpy, usa, eu
    板の名前(product_code)の辞書を返す．例えば：
    [
        {
            "product_code": "BTC_JPY"
        },
        {
            "product_code": "FX_BTC_JPY"
        },
        {
            "product_code": "ETH_BTC"
        },
        {
            "product_code": "BCH_BTC"
        },
        {
            "product_code": "BTCJPY28DEC2018",
            "alias": "BTCJPY_MAT3M"
        },
        {
            "product_code": "BTCJPY26OCT2018",
            "alias": "BTCJPY_MAT1WK"
        },
        {
            "product_code": "BTCJPY02NOV2018",
            "alias": "BTCJPY_MAT2WK"
        }
    ]
    """
    if (current != 'jpy'):
        url = _urlBuilder("getmarkets/" + current)
    else:
        url = _urlBuilder("getmarkets")
    return _req2dic(url)

def getBoard(product_code):

    """ 
    板情報を返す
    product_code: getMarkets()で取得できる
    board = {
        mid_price: float
        bids = {
            price: int
            size: float
        }
        asks = {
            price: int
            size: float
        }
    }
    """
    url = _urlBuilder("getboard", **{'product_code': product_code})
    return _req2dic(url)

def getTicker(product_code):

    """ for example...
    {
        "product_code": "BTC_JPY",
        "timestamp": "2018-10-22T12:20:21.18",
        "tick_id": 3934932,
        "best_bid": 720668,
        "best_ask": 720993,
        "best_bid_size": 0.05,
        "best_ask_size": 0.5664,
        "total_bid_depth": 1746.00447262,
        "total_ask_depth": 2071.13689656,
        "ltp": 720988,
        "volume": 160101.62515103,
        "volume_by_product": 2181.66815001
    }
    """
    url = _urlBuilder("getticker", **{'product_code': product_code})
    return _req2dic(url)

def getExec(product_code, count=100, before=0, after=0):

    """ for example...
    [
        {
            "id": 515598342,
            "side": "SELL",
            "price": 720700,
            "size": 0.01,
            "exec_date": "2018-10-22T12:23:02.23",
            "buy_child_order_acceptance_id": "JRF20181022-122207-005508",
            "sell_child_order_acceptance_id": "JRF20181022-122302-837275"
        },
        ...
    ]
    """
    url = _urlBuilder("getexecutions", **{'count': count, 'before': before, 'after': after})
    return _req2dic(url)

def getChats(from_date="", country="jp"):

    """
    from_dateはISO 8601フォーマットの日付．
    例えば"2018-10-22T12:00:00.000"とか.
    何も指定しないと5日前くらいからのチャットが全部返ってくるっぽい．
    件数にするとだいたい54800件だった．
    country: jp, usa, eu
    応答はやや遅い．
    出力例：
    [
        {
            "nickname": "チョリヤシの木@BWV147",
            "message": "～ 9:00 ～",
            "date": "2018-10-22T00:00:06.623"
        },
        {
            "nickname": "月詠のイザナ",
            "message": "９時",
            "date": "2018-10-22T00:00:08.467"
        },
        ...
    ]
    """
    if country == "jp":
        url = _urlBuilder("getchats", **{'from_date': from_date})
    else:
        url = _urlBuilder("getchats/" + country, **{'from_date': from_date})
    return _req2dic(url)

def getHealth(product_code):
    
    """
    通常時は:
    {
        "status": "NORMAL"
    }
    """
    url = _urlBuilder("gethealth", **{'product_code': product_code})
    return _req2dic(url)

def getBoardState(product_code):

    """
    板の状態？通常時は：
    {
        "health": "NORMAL",
        "state": "RUNNING"
    }
    """
    url = _urlBuilder("getboardstate", **{'product_code': product_code})
    return _req2dic(url)

# てすと
if __name__ == "__main__":

    print("markets:", getMarkets())
    code_fx = getMarkets()[1]['product_code']   # 'FX_BTC_JPY'
    board_fx = getBoard(code_fx)
    print("mid_price:", board_fx['mid_price'])
    print("best_bid:", board_fx['bids'][0])
    print("best_ask:", board_fx['asks'][0])
    ticker_fx = getTicker(code_fx)
    print("ticker:", ticker_fx)
    executions = getExec(code_fx, count=1)
    print("exec:", executions)
    chats = getChats("2018-10-22T00:00:00.000+09:00")
    print("last_chat:", chats[len(chats) - 1])
    health = getHealth(code_fx)
    print("health:", health)
    board_state = getBoardState(code_fx)
    print("board_state:", board_state)
    print(str("よくできました"))