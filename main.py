#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/14/2016 2:00 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    :
# @File    : dragnn_parser.py
# @Software: PyCharm
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS


from apis.AppRouteAPI import AppRouteAPI
from apis.ApplicationAPI import ApplicationAPI
from apis.DeviceAPI import DeviceAPI
from apis.DeviceIntfAPI import DeviceIntfAPI
from apis.DeviceMplsAPI import DeviceMplsAPI
from apis.DeviceMplsIntfAPI import DeviceMplsIntfAPI
from apis.FirewallAPI import FirewallAPI
from apis.LatencyAPI import LatencyAPI
from apis.ServiceAPI import ServiceAPI, ServiceDetailAPI
from apis.TrafficAPI import TrafficAPI

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(FirewallAPI, '/api/v1/firewall')

api.add_resource(AppRouteAPI, '/api/v1/app_route')

api.add_resource(TrafficAPI, '/api/v1/traffic')

api.add_resource(ApplicationAPI, '/api/v1/app_vis')

api.add_resource(DeviceAPI, '/api/v1/devices')

api.add_resource(DeviceIntfAPI, '/api/v1/devices/<device>')

api.add_resource(DeviceMplsAPI, '/api/v1/devices_mpls')

api.add_resource(DeviceMplsIntfAPI, '/api/v1/devices_mpls/<device>')

api.add_resource(LatencyAPI, '/api/v1/latency')

api.add_resource(ServiceAPI, '/api/v1/services')

api.add_resource(ServiceDetailAPI, '/api/v1/services/<service_id>')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',
            port=9010)