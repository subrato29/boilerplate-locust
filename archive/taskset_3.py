import random

from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/api/users/2")
        print("Get status code of 200")
        self.interrupt(reschedule=False)


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_status_1(self):
        self.client.get("/api/users/10")
        print("Get nested status code 200")
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://reqres.in"
    tasks = [MyHTTPCat, MyAnotherHTTPCat]
    wait_time = constant(1)
