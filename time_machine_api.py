from HTTPReq import *

class TimeMachineApi(HTTPRequest):
    def __init__(self):
        self.API_URL = "http://192.168.1.111:8080/v1/"

    #Pools Commands
    def get_pools(self):
        return self._get(self.API_URL + "pools/")

    #Datasets Commands
    def get_datasets(self):
        return self._get(self.API_URL + "datasets/")

    def create_dataset(self, data):
        return self._post(self.API_URL + "datasets/",data)

    def delete_dataset(self,data):
        return self._delete(self.API_URL + "datasets/",data)

    def rename_dataset(self,data):
        return self._put(self.API_URL + "datasets/", data)

    #Snapshots Commands
    def get_snapshots(self):
        return self._get(self.API_URL + "snapshots/")
