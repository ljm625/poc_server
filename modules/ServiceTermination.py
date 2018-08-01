from multiprocessing import Process

import time

from modules.CloudCenterRest import CloudCenterControl
from modules.MongoStorage import MongoStorage


class ServiceTermination(Process):
    """
    This Process is used to terminate service.
    """
    def __init__(self,service_id,service_name):
        Process.__init__(self)
        self.service_id = service_id
        self.service_name =  service_name
        self.cc = CloudCenterControl()

    def terminiate_cloud_center_vm(self):
        if self.jobId:
            result = self.cc.delete_jobs(self.jobId)
            return True
        print("WARNING : No CloudCenter Service associated with this instance.")
        return None


    def run(self):
        """
        Here we define the jobs we need to do
        :return:
        """

        self.mongo = MongoStorage()
        # Prepare to start the service
        print("INFO : Trying to terminate Service: {}".format(self.service_id))
        service_detail = self.mongo.get_service(self.service_id)
        self.jobId=service_detail.get("jobId")
        print("INFO : Trying to terminate CloudCenter Component: {}".format(self.service_id))
        result =self.terminiate_cloud_center_vm()
        # Need to loop check until the service fully terminated.
        if result:
            status = self.cc.get_jobs_status(self.jobId)
            timer = 0
            while status!="Terminated":
                if timer>300:
                    # Re-terminate the service if stucked.
                    self.terminiate_cloud_center_vm()
                    timer = 0
                status = self.cc.get_jobs_status(service_detail.get("jobId"))
                time.sleep(10)
                timer+=10

        print("INFO : CloudCenter Terminated - JobId : {} for {}".format(self.jobId,self.service_id))

        self.mongo.delete_service(self.service_id)

        print("INFO : Service Terminated - {}".format(self.service_id))



