from locust import User, task


class MyFirstTest(User):

    @task
    def launch(self):
        print("Launching the url")

    @task
    def search(self):
        print("Searching")


class MySecondTest(User):

    @task
    def launch2(self):
        print("Second test")

    @task
    def search2(self):
        print("Second search test")