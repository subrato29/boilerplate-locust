from locust import TaskSet, constant, task, HttpUser
import random


class ValidateTaskSet(TaskSet):

    @task
    def get_status(self):
        self.client.get("/api/users?page=2")
        print("Get status of 200")
        self.interrupt(reschedule=False)


class MyAnotherTaskSet(TaskSet):

    @task
    def get_another_status(self):
        self.client.get("/api/users/4")
        print("Get another status of 200")
        self.interrupt(reschedule=False)


class MyUser(HttpUser):
    host = "https://reqres.in"
    tasks = [ValidateTaskSet, MyAnotherTaskSet]
    wait_time = constant(1)
