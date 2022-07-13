from locust import HttpUser, constant, task

from util import *


class MyReqRes(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_user(self):
        res = self.client.get("/api/users?page=2")
        print("=====================================")
        print(res.json())
        print("=====================================")
        print(res.status_code)

    @task
    def create_user(self):
        res = self.client.post("/api/users", data={"name": "locust_" + Util.get_random_string(6),
                                                   "job": "job_" + str(Util.get_random_int(100, 200))})
        print("=====================================")
        print(res.json())
        print("=====================================")
        print(res.status_code)
        # print(res.headers)
