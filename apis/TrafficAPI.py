import time
from flask_restful import Resource, reqparse
import yaml

from modules.PolicyControl import PolicyControl
from modules.TrafficControl import TrafficControl


class TrafficAPI(Resource):
    def __init__(self):
        config = yaml.load(open('config.yaml', 'r'))
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('device', required=True, type=str, location='json')
        self.reqparse.add_argument('intf', required=True, type=str, location='json')
        self.reqparse.add_argument('mpls', required=False, type=bool, default=False, location='json')

        # self.reqparse.add_argument('policy', required=False, type=str, default=config['default_firewall_policy'], location='json')
        super(TrafficAPI, self).__init__()

    def post(self):
        """
        Check the status of the policy
        :return: 200 with body indicating the policy status
        """
        args=self.reqparse.parse_args()
        try:
            self.tf = TrafficControl(mpls=args['mpls'])
            result=self.tf.get_intf_traffic(args.get("device"),args.get("intf"))
            return result, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400