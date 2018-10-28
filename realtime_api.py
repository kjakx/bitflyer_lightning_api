import websocket
import json

class RealtimeAPI():
    def __init__(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("wss://ws.lightstream.bitflyer.com/json-rpc",
                                        on_message = lambda ws, message: print(message),
                                        on_error = lambda ws, error: print(error),
                                        on_close = lambda ws: print("### closed ###"),
                                        on_open = lambda ws: ws.send(self.data))
        self.data = None

    def board_snapshot(self, product_code):
        self.subscribe("lightning_board_snapshot_" + product_code)
    
    def board(self, product_code):
        self.subscribe("lightning_board_" + product_code)

    def ticker(self, product_code):
        self.subscribe("lightning_ticker_" + product_code)

    def executions(self, product_code):
        self.subscribe("lightning_executions_" + product_code)

    def subscribe(self, channelName):
        self.data = json.dumps({
            'method': "subscribe",
            'params': {'channel': channelName},
        })
        self.ws.run_forever()
# test
if __name__ == "__main__":
    api = RealtimeAPI()
    product_code = "FX_BTC_JPY"
    api.ticker(product_code)