import json

import requests
import sys


class ViptelaRest(object):
    def __init__(self, vmanage_ip, username, password,tenant=None):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.tenant=tenant
        self.login(self.vmanage_ip, username, password)

    def login(self, vmanage_ip, username, password):
        """Login to vmanage"""
        base_url_str = 'https://%s/' % vmanage_ip

        login_action = '/j_security_check'

        # Format data for loginForm
        login_data = {'j_username': username, 'j_password': password}

        # Url for posting login data
        login_url = base_url_str + login_action

        url = base_url_str + login_url

        sess = requests.session()
        # If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False,headers={"Content-Type":"application/x-www-form-urlencoded"})
        # if self.tenant:
        #     sess.headers.update({'vsession_id':self.tenant})

        if login_response.status_code>=300:
            print(
            "Login Failed")
            raise BaseException("ERROR : The username/password is not correct.")

        self.session[vmanage_ip] = sess

    def get_request(self, mount_point):
        """GET request"""
        url = "https://%s:8443/dataservice/%s" % (self.vmanage_ip, mount_point)
        if self.tenant:
            header={"VSessionId":self.tenant}
        else:
            header={}
        response = self.session[self.vmanage_ip].get(url, verify=False,headers=header)
        if response.status_code>=300:
            response.raise_for_status()
        elif response.status_code==200:
                return response
        else:
            return None

    def post_request(self, mount_point, payload, headers={'Content-Type': 'application/json'}):
        """POST request"""
        url = "https://%s:8443/dataservice/%s" % (self.vmanage_ip, mount_point)
        if self.tenant:
            headers["VSessionId"]=self.tenant
        payload = json.dumps(payload)
        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        return response

    def put_request(self, mount_point, payload=None, headers={'Content-Type': 'application/json'}):
        """
        PUT Method
        :param mount_point: The url for API
        :param payload: The payload for API
        :param headers: The header
        :return: response
        """
        url= "https://{}:8443/dataservice/{}".format(self.vmanage_ip,mount_point)
        if self.tenant:
            headers["VSessionId"]=self.tenant
        if payload:
            payload=json.dumps(payload)
            response = self.session[self.vmanage_ip].put(url=url,data=payload,headers=headers,verify=False)
        else:
            response=self.session[self.vmanage_ip].put(url=url,headers=headers,verify=False)
        return response