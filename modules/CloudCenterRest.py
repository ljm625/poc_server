import requests
import yaml

config=yaml.load(open('config.yaml', 'r'))

class CloudCenterControl(object):
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        pass

    def build_url(self,url):
        return "https://{}:9443/v1/{}".format(self.hostname,url)


    def get(self,url, header = {}):
        resp = requests.get(self.build_url(url),auth=(self.username, self.password),headers=header)
        if resp.status_code>300:
            resp.raise_for_status()
        else:
            return resp.json()

    def post(self,url,body,header = {"Content-Type":"application/json"}):
        resp=requests.post(self.build_url(url),json=body,headers = header,auth=(self.username, self.password))
        if resp.status_code>300:
            resp.raise_for_status()
        else:
            return resp.json()



    def delete(self,url,header = {}):
        resp=requests.delete(self.build_url(url),headers=header,auth = (self.username,self.password))
        if resp.status_code>300:
            resp.raise_for_status()
        else:
            return resp.json()


    def create_instance(self):
        result = self.post("jobs",config["cloudcenter_profile"])
        return result

    def get_instance_by_id(self,id):
        result = self.get("jobs/{}".format(id))
        return result
