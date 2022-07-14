from locust import HttpUser, task, constant, SequentialTaskSet


class ValidateResponse(SequentialTaskSet):

    @task
    def get_response_1(self):
        res = self.client.get("/api/users/2", name="JSON_RESPONSE_1")
        print(res)

    @task
    def get_response_2(self):
        verification_text = "janet.weaver@reqres.in"
        with self.client.get("/api/users/2", catch_response=True, name="JSON_RESPONSE_2") as response:
            if str(response.text).__contains__(verification_text):
                response.success()
            else:
                response.failure()

    @task
    def get_response_3(self):
        verification_text = "UNVERIFIED_DATA"
        with self.client.get("/api/register", catch_response=True, name="JSON_RESPONSE_3") as response:
            if str(response.text).__contains__(verification_text):
                response.success()
            else:
                response.failure("message not validated")


class MyLoadTest(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)
    tasks = [ValidateResponse]
