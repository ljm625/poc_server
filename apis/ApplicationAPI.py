import time
from flask_restful import Resource, reqparse
import yaml

from modules.PolicyControl import PolicyControl
from modules.TrafficControl import TrafficControl


class ApplicationAPI(Resource):
    def __init__(self):
        config = yaml.load(open('config.yaml', 'r'))
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('device', required=True, type=str,
                                   location='json')
        # self.reqparse.add_argument('desc', required=False, type=str, default=config['default_approute_desc'],
        #                            location='json')
        # self.reqparse.add_argument('policy', required=False, type=str, default=config['default_approute_policy'],
        #                            location='json')
        self.reqparse.add_argument('mpls', required=False, type=bool, default=False, location='json')

        super(ApplicationAPI, self).__init__()

    # def get(self):
    #     """
    #     Check the status of the policy
    #     :return: 200 with body indicating the policy status
    #     """
    #     try:
    #         args = self.reqparse.parse_args()
    #         pc = PolicyControl()
    #         result = pc.get_policy_status(args['name'])
    #         return {'activated': result, "result": 'success'}, 200
    #     except Exception as e:
    #         return {'result': 'fail', "reason": str(e)}, 400

    def post(self):
        # Used for get the application lis
        args = self.reqparse.parse_args()
        self.tf = TrafficControl(mpls=args['mpls'])

        try:
            result = self.tf.get_device_app_flow(args.get("device"))
            return result, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400
    # def delete(self):
    #     """
    #     Used for deactivate the policy
    #     :return: 204 if success, 400 if error
    #     """
    #     args = self.reqparse.parse_args()
    #     try:
    #         pc = PolicyControl()
    #         if args.get("name") not in pc.policy:
    #             return {'result': 'failed', 'reason': 'policy doesnt exist'}
    #         else:
    #             pc.deactivate_policy(args['name'])
    #             return {}, 204
    #     except Exception as e:
    #         return {'result': 'fail', "reason": str(e)}, 400
