import time
from hashlib import sha256
import hmac
import requests
import json

class ApiHitter():
    def __init__(self, key=None, secret=None):
        self.URL = "https://api.bitflyer.com"
        self.KEY = key
        if type(secret) == str:
            secret = secret.encode("utf-8")
        self.SECRET = secret

    def _getResponce(self, method, url, data=None, headers=None):
        responce = requests.request(method, url, data=data, headers=headers)
        return json.loads(responce.content)

    def _buildQuery(self, **params):
        query = ""
        if params is not None:
            params = {key: params[key] for key in params if params[key] is not None}
            if len(params) != 0:
                query += '?'
                for i, (key, value) in enumerate(params.items(), 1):
                    query += (key + '=' + str(value))
                    if i != len(params):
                        query += '&'
        return query

    def _generateSign(self, timestamp, method, path, **params):
        if method == "GET":
            query = self._buildQuery(**params)
            text = timestamp + method + path + query
        else: # method == "POST":
            body = json.dumps(params)
            text = timestamp + method + path + body
        sign = hmac.new(self.SECRET, text.encode('utf-8'), sha256).hexdigest()
        return sign

    def _makeHeaders(self, timestamp, method, path, **params):
        sign = self._generateSign(timestamp, method, path, **params)
        headers = {
            'ACCESS-KEY': self.KEY,
            'ACCESS-TIMESTAMP': timestamp,
            'ACCESS-SIGN': sign,
            'Content-Type': 'application/json'
        }
        return headers

    def _timestamp(self):
        return str(time.time())
    
    def request(self, method, path, **params):
        if self.KEY and self.SECRET:
            timestamp = self._timestamp()
            headers = self._makeHeaders(timestamp, method, path, **params)
        else:
            headers = None
        if method == "GET":
            query = self._buildQuery(**params)
            url = self.URL + path + query
            responce = self._getResponce(method, url, headers=headers)
        else: # method == "POST":
            url = self.URL + path
            data = json.dumps(params)
            responce = self._getResponce(method, url, data=data, headers=headers)
        return responce
# test
if __name__ == "__main__":
    api = ApiHitter( \
        key="YOUR_API_KEY", \
        secret="YOUR_API_SECRET" \
    )
    method = "GET"
    path = "/v1/me/getexecutions"
    params = {'count':10, 'before':0, 'after':0}
    query = api._buildQuery(**params)
    url = api.URL + path + query
    print(url)
    timestamp = api._timestamp()
    print(timestamp)
    sign = api._generateSign(timestamp, method, path, **params)
    print(sign)
    headers = api._makeHeaders(timestamp, method, path, **params)
    print(headers)
    responce = api._getResponce(method, url, headers=headers)
    print(responce)