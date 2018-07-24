"""
Class with REST Api GET and POST libraries

Example: python rest_api_lib.py vmanage_hostname username password

PARAMETERS:
    vmanage_hostname : Ip address of the vmanage or the dns name of the vmanage
    username : Username to login the vmanage
    password : Password to login the vmanage

Note: All the three arguments are manadatory
"""

import time

from modules.PolicyControl import PolicyControl


def main():
    # vmanage_ip, username, password = '10.63.54.240', 'admin', 'admin'
    # policy_name="Firewall_Test"
    # obj = rest_api_lib(vmanage_ip, username, password)
    # response = obj.get_request('device')
    # payload=    {"policyName":policy_name,"policyDescription":"test policy","policyDefinition":"policy\n  lists \n    site-list firewall-sites\n      site-id 1\n  control-policy firewall-service\n    sequence 10\n      match route\n        site-id 2\n      action accept\n        set service FW vpn 10\n    default-action accept\napply-policy\n  site-list firewall-sites control-policy firewall-service out\n"}
    # result=obj.post_request("template/policy/vsmart",payload=payload)
    # response = obj.get_request("template/policy/vsmart")
    # print(response)
    # # Example request to make a Post call to the vmanage "url=https://vmanage.viptela.com/dataservice/device/action/rediscover"
    # payload = {"action": "rediscover", "devices": [{"deviceIP": "172.16.248.105"}, {"deviceIP": "172.16.248.106"}]}
    # response = obj.post_request('device/action/rediscover', payload)
    policyName="Add-Firewall2"
    policyDesc="TEST"
    policyCLI="policy\n  lists \n    site-list firewall-sites\n      site-id 4\n  control-policy firewall-service\n    sequence 10\n      match route\n        site-id 5\n      action accept\n        set service FW vpn 10\n    default-action accept\napply-policy\n  site-list firewall-sites control-policy firewall-service out\n"

    pc=PolicyControl()
    # pc.deactivate_policy(policyName)
    pc.create_policy(policyName,policyDesc,policyCLI)
    time.sleep(5)
    pc.activate_policy(policyName)



if __name__ == '__main__':
    main()