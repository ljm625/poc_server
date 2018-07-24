

import time
from flask_restful import Resource, reqparse
import yaml

from modules.LatencyControl import LatencyControl


class LatencyAPI(Resource):
    def __init__(self):
        config = yaml.load(open('config.yaml', 'r'))
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('latency1', required=True, type=int, location='json')
        self.reqparse.add_argument('latency2', required=True, type=int, location='json')
        # self.reqparse.add_argument('mpls', required=False, type=bool, default=False, location='json')

        # self.reqparse.add_argument('policy', required=False, type=str, default=config['default_firewall_policy'], location='json')
        super(LatencyAPI, self).__init__()

    def post(self):
        """
        Check the status of the policy
        :return: 200 with body indicating the policy status
        """
        args=self.reqparse.parse_args()
        try:
            self.lc=LatencyControl()
            result=self.lc.change_latency(args.get('latency1'),args.get('latency2'))
            return {'result':result}, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400