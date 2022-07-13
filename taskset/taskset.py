from locust import TaskSet, constant, task, HttpUser
import random


class ValidateTestSet(TaskSet):

    @task
    def get_status(self):
        self.client.get("/api/users?page=2")
        print("Get status of 200")

    @task
    def get_status_of_random_user(self):
        user = [2, 3, 4, 5, 6]
        endpoint = "/api/users?page=" + str(random.choice(user))
        res = self.client.get(endpoint)
        print("HTTP status code of random user: " + str(res.status_code))


class MyUser(HttpUser):
    host = "https://reqres.in"
    tasks = [ValidateTestSet]
    wait_time = constant(1)
