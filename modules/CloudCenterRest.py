import requests


class CloudCenterControl(object):
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        pass

    def build_url(self,url):
        return "https://{}/api/v1/{}".format(self.hostname,url)


    def get(self,url, header = {}):
        requests.get()

    def post(self,url,body,header = {"Content-Type":"application/json"}):
        requests.post()

    def delete(self,url,header = {}):
        requests.delete()

