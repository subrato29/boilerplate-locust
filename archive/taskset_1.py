import random

from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/api/users/2")
        print("Get status code of 200")

    @task
    def get_random_status(self):
        status_code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        random_user = str(random.choice(status_code));
        res = self.client.get("/api/users/" + random_user);
        print ("Validating random HTTP status")


class MyLoadTest(HttpUser):
    host = "https://reqres.in"
    tasks = [MyHTTPCat]
    wait_time = constant(1)
