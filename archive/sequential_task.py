from locust import SequentialTaskSet, HttpUser, constant, task


class MySeqTask(SequentialTaskSet):

    @task
    def get_status_1(self):
        self.client.get("/users?page=2");
        print("get_status_1 of 200");

    @task
    def get_status_2(self):
        self.client.get("/api/users/2");
        print("get_status_2 of 200");


class MyLoadTest(HttpUser):
    host = "https://reqres.in"
    tasks = [MySeqTask]
    wait_time = constant(1)
