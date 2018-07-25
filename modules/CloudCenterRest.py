import requests


class CloudCenterControl(object):
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        pass

    def get(self,url, header = {}):
        requests.get()

    def post(self,url,body,header = {}):
        requests.post()

    def delete(self,url,header = {}):
        requests.delete()

