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
        return self._put(self.API_URL + "datasets/",data)

    #Snapshots Commands
    def get_snapshots(self):
        return self._get(self.API_URL + "snapshots/")

    def create_snapshot(self,data):
        return self._post(self.API_URL + "snapshots/",data)

    def delete_snapshot(self,data):
        return self._delete(self.API_URL + "snapshots/",data)

    def rename_snapshot(self,data):
        return self._put(self.API_URL + "snapshots/",data)

    def clone_snapshot(self,data):
        return self._put(self.API_URL + "snapshots/clone",data)

    def rollback_snapshot(self,data):
        return self._put(self.API_URL + "snapshots/rollback",data)

    #Checks
    def check_response(self,response,method,name):
        if response.status_code == 200:
            pprint(f"{name.capitalize()} {method}d")
        elif response.status_code == 404:
            pprint(f"{name.capitalize()} not found")
        else:
            if method == "rollback":
                pprint("Error rolling back to this snapshot")
            elif method == "clone":
                pprint("Error creating clone or invalid snapshot / dataset name")
            else:
                pprint(f"Error {method[0:len(method)-1]}ing {name} or invalid format")
