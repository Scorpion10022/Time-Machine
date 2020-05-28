import json
import os
import requests

from pprint import pprint

class HTTPRequest:
    def _get(self,url):
        response = requests.get(url)
        result = []
        for item in response.json():
            result.append({"name": item.get("name")})
        return result

    def _post(self,url,data):
        try:
            return requests.post(url, json=data)
        except requests.exceptions.RequestException as e:
            return False

    def _put(self,url,data):
        try:
            return requests.put(url, json=data)
        except requests.exceptions.RequestException as e:
            return False

    def _delete(self,url,data):
        return requests.delete(url, json=data)
