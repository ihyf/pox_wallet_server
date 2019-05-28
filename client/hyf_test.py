import time
import json
import requests


class Hyf(object):
    def __init__(self):
        self.appid = "hyf_app"
        self.headers = {
            "content-type": "application/json",
            "Authorization": "flo test"
        }
        self.payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "",
            "params": {
                "data": {
                
                }
            }
        }
        self.url_local = "http://localhost:9001/api"
        self.url_wai = "http://149.28.56.184:9000/api"
    
    def send_request(self, url, method, data):
        self.payload["method"] = method
        self.payload["params"]["data"] = data
        print(url)
        print(self.payload)
        response = requests.post(url=url, data=json.dumps(self.payload), headers=self.headers)
        print(response.json())

    def test_my_method(self):
        method = "my_method"
        data = {
            "time": time.time()
        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_difficulty(self):
        method = "get_difficulty"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_coin_supply(self):
        method = "get_coin_supply"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_distribution(self):
        method = "get_distribution"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_block_count(self):
        method = "get_block_count"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_network_hashps(self):
        method = "get_network_hashps"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_node_count(self):
        method = "get_node_count"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)


if __name__ == "__main__":
    hyf = Hyf()

    # hyf.test_my_method()
    hyf.test_get_difficulty()
    hyf.test_get_coin_supply()
    hyf.test_get_distribution()
    hyf.test_get_block_count()
    hyf.test_get_network_hashps()
    hyf.test_get_node_count()
