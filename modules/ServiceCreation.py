from multiprocessing import Process

import time

from modules.CloudCenterRest import CloudCenterControl
from modules.MongoStorage import MongoStorage


class ServiceCreation(Process):
    def __init__(self,service_id,service_name):
        Process.__init__(self)
        self.service_id = service_id
        self.service_name =  service_name
        self.cc = CloudCenterControl()

        pass

    def create_cloud_center_vm(self):
        result = self.cc.create_jobs(self.service_name,"WQxsca!@#sadwdaSSSX213")
        id = result['id']
        self.mongo.add_logs(self.service_id,"提交云端创建请求")
        return id

    def get_ip_address(self,jobId):
        timer = 0
        while timer<90 :
            try:
                ip = self.cc.get_jobs_ip_address(jobId)
                if ip:
                    return ip
                else:
                    raise Exception("Wait")
            except:
                time.sleep(5)
                timer+=5
        return None

    def run(self):
        """
        Here we define the jobs we need to do
        :return:
        """

        self.mongo = MongoStorage()
        # Prepare to start the service
        print("INFO : Trying to start Service: {}".format(self.service_id))
        self.mongo.update_status(self.service_id,"processing")
        print("INFO : Trying to start CloudCenter Component: {}".format(self.service_id))
        jobsId = self.create_cloud_center_vm()
        if jobsId:
            print("INFO : CloudCenter Task submitted - JobId : {} for {}".format(jobsId,self.service_id))
            self.mongo.update_service(self.service_id,{"jobId":jobsId})
            print("INFO : Waiting for IP Address - JobId : {} for {}".format(jobsId,self.service_id))
            ip_address=self.get_ip_address(jobsId)
            if not ip_address:
                raise Exception("Failed to get IP")
            print("INFO : Got IP Address {} - JobId : {} for {}".format(ip_address,jobsId,self.service_id))
            self.mongo.update_service(self.service_id, {"ip": ip_address})
            status = self.cc.get_jobs_status(jobsId)
            while status!="Deployed":
                status = self.cc.get_jobs_status(jobsId)
                time.sleep(10)
            print("INFO : CloudCenter Deployed - JobId : {} for {}".format(jobsId,self.service_id))
            self.mongo.add_logs(self.service_id,"云端创建完成")



