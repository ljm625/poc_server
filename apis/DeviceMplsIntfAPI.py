import time
from flask_restful import Resource, reqparse
import yaml

from modules.PolicyControl import PolicyControl
from modules.TrafficControl import TrafficControl


class DeviceMplsIntfAPI(Resource):
    def __init__(self):
        config = yaml.load(open('config.yaml', 'r'))
        # self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('name', required=False, type=str, default=config['default_firewall_rule'], location='json')
        # self.reqparse.add_argument('desc', required=False, type=str, default=config['default_firewall_desc'], location='json')
        # self.reqparse.add_argument('policy', required=False, type=str, default=config['default_firewall_policy'], location='json')
        super(DeviceMplsIntfAPI, self).__init__()

    def get(self,device):
        """
        Check the status of the policy
        :return: 200 with body indicating the policy status
        """
        # self.tf=TrafficControl(mpls=True)
        try:
            self.tf = TrafficControl(mpls=True)

            result=self.tf.get_device_intf(device)
            return result, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400