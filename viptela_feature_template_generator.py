import json
from pprint import pprint

from modules.ViptelaRest import ViptelaRest

template ='''
{

    "templateName": "VPN_%s",
    "templateDescription": "service_vpn_%s",
    "templateType": "vpn-vedge",
    "templateMinVersion": "15.0.0",
    "templateDefinition":     {
        "vpn-id": {
            "vipObjectType": "object",
            "vipType": "constant",
            "vipValue": %s
        },
        "name": {
            "vipObjectType": "object",
            "vipType": "ignore",
            "vipVariableName": "vpn_name"
        },
        "ecmp-hash-key": {
            "layer4": {
                "vipObjectType": "object",
                "vipType": "ignore",
                "vipValue": "false",
                "vipVariableName": "vpn_layer4"
            }
        },
        "tcp-optimization": {
            "vipObjectType": "node-only",
            "vipType": "ignore",
            "vipValue": "false",
            "vipVariableName": "vpn_tcp_optimization"
        },
        "host": {
            "vipType": "ignore",
            "vipValue": [],
            "vipObjectType": "tree",
            "vipPrimaryKey": [
                "hostname"
            ]
        },
        "service": {
            "vipType": "ignore",
            "vipValue": [],
            "vipObjectType": "tree",
            "vipPrimaryKey": [
                "svc-type"
            ]
        },
        "ip": {
            "route": {
                "vipType": "constant",
                "vipValue": [
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_1"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_2"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_3"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_4"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_5"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_6"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_7"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_8"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_9"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    },
                    {
                        "prefix": {
                            "vipObjectType": "object",
                            "vipType": "variableName",
                            "vipValue": "",
                            "vipVariableName": "prefix_10"
                        },
                        "vipOptional": true,
                        "next-hop": {
                            "vipType": "constant",
                            "vipValue": [
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_1"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_0"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                },
                                {
                                    "address": {
                                        "vipObjectType": "object",
                                        "vipType": "variableName",
                                        "vipValue": "",
                                        "vipVariableName": "nexthop_2"
                                    },
                                    "distance": {
                                        "vipObjectType": "object",
                                        "vipType": "ignore",
                                        "vipValue": 1,
                                        "vipVariableName": "vpn_next_hop_ip_distance_1"
                                    },
                                    "priority-order": [
                                        "address",
                                        "distance"
                                    ]
                                }
                            ],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "address"
                            ]
                        },
                        "priority-order": [
                            "prefix",
                            "next-hop"
                        ]
                    }
                ],
                "vipObjectType": "tree",
                "vipPrimaryKey": [
                    "prefix"
                ]
            },
            "gre-route": {},
            "ipsec-route": {}
        },
        "ipv6": {},
        "omp": {
            "advertise": {
                "vipType": "ignore",
                "vipValue": [],
                "vipObjectType": "tree",
                "vipPrimaryKey": [
                    "protocol"
                ]
            }
        }
    },
    "deviceType": [
        "vedge-cloud",
        "vedge-1000",
        "vedge-2000",
        "vedge-100",
        "vedge-100-B",
        "vedge-100-WM",
        "vedge-100-M",
        "vedge-5000"
    ],
    "deviceModels": [
        {
            "name": "vedge-100",
            "displayName": "vEdge 100",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        },
        {
            "name": "vedge-100-B",
            "displayName": "vEdge 100 B",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        },
        {
            "name": "vedge-100-M",
            "displayName": "vEdge 100 M",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        },
        {
            "name": "vedge-100-WM",
            "displayName": "vEdge 100 WM",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        },
        {
            "name": "vedge-1000",
            "displayName": "vEdge 1000",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        },
        {
            "name": "vedge-2000",
            "displayName": "vEdge 2000",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        },
        {
            "name": "vedge-5000",
            "displayName": "vEdge 5000",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        },
        {
            "name": "vedge-cloud",
            "displayName": "vEdge Cloud",
            "deviceType": "vedge",
            "isCliSupported": true,
            "isCiscoDeviceModel": false
        }
    ],
    "transitionInProgress": true,
    "secAddrIndex": 0,
    "viewMode": "add",
    "templateUrl": "/app/configuration/template/feature/templates/vpn-vedge-15.0.0.html",
    "factoryDefault": false
}
'''


def create_feature_template(start,end):
    rest = ViptelaRest("192.168.100.32","admin","admin","MTUyODczNzA3NDYwNQ==")
    # pprint(json.loads(template % (103,103,103)))
    for i in range(start,end+1):
        resp= rest.post_request("template/feature/",json.loads(template % (i,i,i)))
        if resp.status_code == 200:
            print("Succeessfully created VPN Template VPN_{}".format(i))


if __name__ == '__main__':
  create_feature_template(104,162)