import requests
import yaml
from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient

config=yaml.load(open('config.yaml', 'r'))

class MongoStorage(object):

    def __init__(self,username=config['username'],password=config['password'],hostname=config['mongo_hostname'],dbname=config['mongo_dbname']):
        # Initialize the Mongo Database
        self.mongo = MongoClient("mongodb://{}:{}@{}/{}".format(username,password,hostname,dbname))
        self.database=self.mongo.get_database(dbname)


    def read(self):
        pass

    def write(self):
        pass

    def deploy_service(self,user,service_name,sites,type="cloudbone",cloud="aliyun",ip="0.0.0.0"):

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result =self.database.services.insert_one({"user":user,"service_name":service_name,"sites":sites,"type":type,"cloud":cloud,"ip":ip,"status":"submitted"
                                                   ,"logs":[], "time":time_now})
        # print(result)
        print(result.inserted_id)
        self.add_logs(result.inserted_id,"提交服务创建请求")
        return result.inserted_id

    def update_service(self,id,update_json):
        self.database.get_collection("services").find_one_and_update({"_id":ObjectId(id)},{"$set" : update_json})
        return True

    def delete_service(self,id):
        self.database.get_collection("services").delete_one({"_id": ObjectId(id)})
        return True

    def get_all_service(self):
        service_list = list(self.database.get_collection("services").find({}))
        return service_list

    def get_service(self,id):
        return self.database.get_collection("services").find_one({"_id":ObjectId(id)})

    def add_logs(self,id,logs):
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        old_data = self.database.get_collection("services").find_one({"_id": ObjectId(id)})
        log = {"time":time_now,"log":logs}
        new_log = old_data['logs']
        new_log.append(log)
        self.database.get_collection("services").find_one_and_update({"_id":ObjectId(id)},{"$set" : {"logs":new_log}})
        return True

    def update_status(self,id,status):
        self.update_service(id,{"status":status})
        return True