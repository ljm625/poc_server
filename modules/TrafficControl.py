from modules.ViptelaRest import ViptelaRest
import yaml
config=yaml.load(open('config.yaml', 'r'))

class TrafficControl(object):
    """
    Control the traffic related APIs, including get device list (System-ip), get interface etc.
    """
    def __init__(self,vmanage_ip=config['viptela_url'],username=config["viptela_username"],password=config["viptela_password"],mpls=False):
        """
        The Initial command
        """
        self.device_list={}
        if mpls:
            vmanage_ip=config['viptela_mpls_url']
            self.rest=ViptelaRest(vmanage_ip=vmanage_ip,username=username,password=password,tenant=config['tenant_id'])
        else:
            self.rest=ViptelaRest(vmanage_ip=vmanage_ip,username=username,password=password)

        self.get_vedge_list()


    def get_vedge_list(self):
        """
        Get the vedge list
        :return: A dict with name:id combination
        """
        result=self.rest.get_request("system/device/vedges")
        json_list=result.json()
        devices={}
        for device in json_list["data"]:
            if "host-name" in device:
                devices[device["host-name"]]=device["deviceIP"]
        self.device_list=devices

    def get_traffic(self,device_name):
        """
        GET traffic of a device
        :param policy_name:
        :return:
        """
        if device_name not in self.device_list:
            raise Exception("ERROR : Device not exist!")
        result=self.rest.get_request("device/interface?deviceId={}".format(self.device_list[device_name]))
        if result.status_code>=300:
            raise Exception("ERROR: {}".format(result.content))
        return result

    def get_device_intf(self,device_name):
        if device_name not in self.device_list:
            raise Exception("ERROR : Device not exist!")
        traffic = self.get_traffic(device_name).json()
        if_list=[]
        for intf in traffic['data']:
            if intf['af-type']=='ipv4':
                if_list.append(intf['ifname'])
        return if_list

    def get_intf_traffic(self,device_name,device_intf):
        """
        GET traffic of a device intf
        :param device_name:
        :param device_intf:
        :return:
        """
        if device_name not in self.device_list:
            raise Exception("ERROR : Device not exist!")
        traffic=self.get_traffic(device_name).json()
        for intf in traffic['data']:
            if intf['af-type']=='ipv4' and intf['ifname']==device_intf:
                return {"rx-kbps":intf["rx-kbps"],"tx-kbps":intf["tx-kbps"]}
        raise Exception("ERROR : Intf not exist")

    def get_device_app_flow(self,device_name):
        """

        :param device_name:
        :return: a list of app running on this device
        """

        if device_name not in self.device_list:
            raise Exception("ERROR : Device not exist!")
        result = self.rest.get_request("device/dpi/flows?deviceId={}".format(self.device_list[device_name]))
        if result.status_code>=300:
            raise Exception("ERROR: {}".format(result.content))
        return result.json()['data']
