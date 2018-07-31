import json

import requests
import yaml

config=yaml.load(open('config.yaml', 'r'))

class CloudCenterControl(object):
    def __init__(self,hostname=config['cloudcenter_address'],username=config['cloudcenter_username'],password=config['cloudcenter_password']):
        self.hostname = hostname
        self.username = username
        self.password = password
        pass

    def build_url(self,url):
        return "https://{}:9443/{}".format(self.hostname,url)


    def get(self,url, header = {}):
        resp = requests.get(self.build_url(url),auth=(self.username, self.password),headers=header,verify=False)
        if resp.status_code>300:
            resp.raise_for_status()
        else:
            return resp.json()

    def post(self,url,body,header = {"Content-Type":"application/json"}):
        resp=requests.post(self.build_url(url),json=body,headers = header,auth=(self.username, self.password),verify=False)
        if resp.status_code>300:
            resp.raise_for_status()
        else:
            return resp.json()



    def delete(self,url,header = {}):
        resp=requests.delete(self.build_url(url),headers=header,auth = (self.username,self.password),verify=False)
        if resp.status_code>300:
            resp.raise_for_status()
        else:
            return resp.json()


    def create_jobs(self,name,password):
        # print(config["cloudcenter_profile"]%(name,password))
        result = self.post("v2/jobs",json.loads(config["cloudcenter_profile"]%(name,password)))
        return result

    def get_jobs_by_id(self,id):
        result = self.get("v1/jobs/{}".format(id))
        return result

    def get_jobs_ip_address(self,jobId):
        """
        The process of getting job IP address:
        1. check if there's vm params
        2. If not get its sub Job
        3. Check if there's vm params
        4. return ip_address.
        :param jobId:
        :return:
        """
        result = self.get_jobs_by_id(jobId)
        if len(result['virtualMachines'])>0:
            return result['virtualMachines'][0]['publicIp']
        else:
            if len(result['jobs'])==1:
                return result['jobs'][0]['virtualMachines'][0]['publicIp']
        return None

    def delete_jobs(self,jobId):
        result = self.delete("v1/jobs/{}".format(jobId))
        return result

    def get_jobs_status(self,jobId):
        result = self.get_jobs_by_id(jobId)
        return result['deploymentInfo']['deploymentStatus']