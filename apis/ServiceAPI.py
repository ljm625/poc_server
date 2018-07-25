import json
import time
from flask_restful import Resource, reqparse
import yaml

from modules.MongoStorage import MongoStorage


class ServiceAPI(Resource):
    def __init__(self):
        config = yaml.load(open('config.yaml', 'r'))
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('latency1', required=True, type=int, location='json')
        self.reqparse.add_argument('latency2', required=True, type=int, location='json')
        # self.reqparse.add_argument('mpls', required=False, type=bool, default=False, location='json')

        # self.reqparse.add_argument('policy', required=False, type=str, default=config['default_firewall_policy'], location='json')
        super(ServiceAPI, self).__init__()

    def get(self):
        """
        Get Service List
        :return: 200 with body that have all the service info.
        """
        try:
            mongo =MongoStorage()
            services = mongo.get_all_service()
            for service in services:
                # Here, we need to convert the objectId to id and add a self containing the link.
                service['id']=str(service['_id'])
                del service['_id']
                service['self']="/api/v1/services/{}".format(service['id'])
                service['sites']=json.loads(service['sites'])
            return services, 200

        except Exception as e:
            return {'result':'fail', 'reason':str(e)}, 400


    def post(self):
        """
        Create Service
        :return: 200 with body indicating the policy status
        """
        req = reqparse.RequestParser()
        req.add_argument('user', required=True, type=str, location='json')
        req.add_argument('service_name', required=True, type=str, location='json')
        req.add_argument('sites', required=True, location='json',type=list)
        req.add_argument('type', required=True, type=str, location='json')
        req.add_argument('cloud', required=True, type=str, location='json')
        req.add_argument('ip', required=True, type=str, location='json')
        args=req.parse_args()
        try:
            mongo = MongoStorage()
            result = mongo.deploy_service(args['user'],args['service_name'],json.dumps(args['sites']),args['type'],args['cloud'])
            return {"id":str(result)}, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400


class ServiceDetailAPI(Resource):
    def __init__(self):
        config = yaml.load(open('config.yaml', 'r'))

        # self.reqparse.add_argument('policy', required=False, type=str, default=config['default_firewall_policy'], location='json')
        super(ServiceDetailAPI, self).__init__()

    def get(self,service_id):
        # Get Service detail
        try:
            mongo = MongoStorage()
            result = mongo.get_service(service_id)
            result['id'] = str(result['_id'])
            del result['_id']
            result['sites'] = json.loads(result['sites'])

            return {'result':result}, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400

    def put(self,service_id):
        """
        Update Service
        :return: 200 with body indicating the policy status
        """

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('service_name', required=False, type=str, location='json')
        self.reqparse.add_argument('sites', required=False, type=list, location='json')
        self.reqparse.add_argument('type', required=False, type=str, location='json')
        self.reqparse.add_argument('cloud', required=False, type=str, location='json')
        self.reqparse.add_argument('ip', required=False, type=str, location='json')
        args=self.reqparse.parse_args()
        try:
            mongo = MongoStorage()
            # Fix sites to json
            if args.get("sites"):
                args['sites']=json.dumps(args['sites'])
            result = mongo.update_service(service_id,args)
            return {'result':result}, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400


    def delete(self,service_id):
        """
        Delete given service
        :return:
        """
        try:
            mongo = MongoStorage()
            result = mongo.delete_service(service_id)
            return {'result':result}, 200
        except Exception as e:
            return {'result': 'fail', "reason": str(e)}, 400
