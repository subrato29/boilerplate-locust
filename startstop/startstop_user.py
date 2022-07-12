from locust import User, task, constant


class MyTest(User):
    wait_time = constant(1)

    def on_start(self):
        print("Starting")

    @task
    def validate(self):
        print("Validating")

    def on_stop(self):
        print("Stopped")
