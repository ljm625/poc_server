from modules.ViptelaRest import ViptelaRest
import yaml
config=yaml.load(open('config.yaml', 'r'))

class PolicyControl(object):
    """
    Control the policy, including creating & activating / disactivate policy
    """
    def __init__(self,vmanage_ip=config['viptela_url'],username=config["viptela_username"],password=config["viptela_password"],mpls=False):
        """
        The Initial command for policy
        """
        if mpls:
            vmanage_ip=config['viptela_mpls_url']
            self.rest=ViptelaRest(vmanage_ip=vmanage_ip,username=username,password=password,tenant=config['tenant_id'])
        else:
            self.rest=ViptelaRest(vmanage_ip=vmanage_ip,username=username,password=password)
        # GET the policy list
        self.policy=self.get_policy_list()


    def get_policy_list(self):
        """
        Get the policy list
        :return: A dict with name:id combination
        """
        result=self.rest.get_request("template/policy/vsmart")
        json_list=result.json()
        policy_list={}
        for policy in json_list["data"]:
            policy_list[policy['policyName']]=(policy['policyId'],policy['isPolicyActivated'])
        return policy_list

    def activate_policy(self,policy_name):
        """
        Activate the policy
        :param policy_name:
        :return:
        """
        if policy_name not in self.policy:
            raise Exception("ERROR : Policy not exist!")
        result=self.rest.post_request("template/policy/vsmart/activate/{}".format(self.policy[policy_name][0]),payload={})
        if result.status_code>=300:
            raise Exception("ERROR: {}".format(result.content))
        return result

    def deactivate_policy(self,policy_name):
        """
        Deactivate the policy
        :param policy_name:
        :return:
        """
        if policy_name not in self.policy:
            raise Exception("ERROR : Policy not exist!")
        result=self.rest.post_request("template/policy/vsmart/deactivate/{}".format(self.policy[policy_name][0]),payload={})
        if result.status_code>=300:
            raise Exception("ERROR: {}".format(result.content))
        return result

    def create_policy(self,policy_name,policy_description,policy_cli_body):
        def builder():
            return {"policyName": policy_name,
                    "policyDescription": policy_description,
                    "policyDefinition": policy_cli_body
                    }
        if policy_name in self.policy:
            raise Exception("ERROR : Same name policy already exist")
        result=self.rest.post_request("template/policy/vsmart",payload=builder())
        if result.status_code>=300:
            raise Exception("ERROR: {}".format(result.content))
        # time.sleep(1)
        self.policy=self.get_policy_list()
        return result

    def get_policy_status(self,policy_name):
        """
        Get the status of the policy
        :param policy_name: the policy_name
        :return: boolean, true for activated, false for not activated.
        """
        if policy_name in self.policy:
            return self.policy[policy_name][1]
        else:
            return False

