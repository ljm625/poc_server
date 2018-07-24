import time
from flask_restful import Resource, reqparse
import yaml

from modules.PolicyControl import PolicyControl


class AppRouteAPI(Resource):
    def __init__(self):
        config = yaml.load(open('config.yaml', 'r'))
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', required=False, type=str, default=config['default_approute_rule'],
                                   location='json')
        self.reqparse.add_argument('desc', required=False, type=str, default=config['default_approute_desc'],
                                   location='json')
        self.reqparse.add_argument('policy', required=False, type=str, default=config['default_approute_policy'],
                                   location='json')
        self.reqparse.add_argument('mpls', required=False, type=bool, default=False, location='json')

        super(AppRouteAPI, self).__init__()

    def get(self):
        """
        Check the status of the policy
        :return: 200 with body indicating the policy status
        """
        try:
            args = self.reqparse.parse_args()
            pc = PolicyControl(mpls=args['mpls'])
            result = pc.get_policy_status(args['name'])
            return {'activated': result, "result": 'success'}, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400

    def post(self):
        # Used for creating the policy / Activating the policy
        args = self.reqparse.parse_args()
        try:

            pc = PolicyControl(mpls=args['mpls'])
            if args.get("name") in pc.policy:
                # The policy is already added, just activate it
                pc.activate_policy(args.get("name"))
                return {'result': 'success'}, 200
            else:
                pc.create_policy(args['name'], args['desc'], args['policy'])
                time.sleep(5)
                pc.activate_policy(args['name'])
                return {'result': 'success'}, 200
                # parse = parser.SyntaxnetParser(segmenter_model,parser_model,folder=args['syntax_folder'])
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400

    def delete(self):
        """
        Used for deactivate the policy
        :return: 204 if success, 400 if error
        """
        args = self.reqparse.parse_args()
        try:
            pc = PolicyControl(mpls=args['mpls'])
            if args.get("name") not in pc.policy:
                return {'result': 'failed', 'reason': 'policy doesnt exist'}
            else:
                pc.deactivate_policy(args['name'])
                return {}, 204
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400
