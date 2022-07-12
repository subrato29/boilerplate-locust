from locust import User, task, constant


class MyFirstTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launch the URL..")

    @task
    def search(self):
        print("First search test")


class MySecondTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def lunch(self):
        print("Second test")

    @task
    def search2(self):
        print("Second search test")
