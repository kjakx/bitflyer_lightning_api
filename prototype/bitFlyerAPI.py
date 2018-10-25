import requests
import json

class BF_API():

    def __init__(self, endpoint_url):

        self.URL = endpoint_url

    def _req2dic(self, url):

        resp = requests.get(url)
        dic = json.loads(resp.content)
        return dic

    def _urlBuilder(self, path, **query):

        url = self.URL + path + '/'
        if len(query) != 0:
            url += '?'
            for i, (key, value) in enumerate(query.items(), 1):
                url += (key + '=' + str(value))
                if i != len(query):
                    url += '&'
        return url

    def _call(self, path, **query):

        url = self._urlBuilder(path, **query)
        dic = self._req2dic(url)
        return dic

# test
if __name__ == "__main__":
    api = BF_API("https://api.bitflyer.com/v1/")
    print(api._call("getexecutions", product_code="BTC_JPY", count=1, before=0, after=0))