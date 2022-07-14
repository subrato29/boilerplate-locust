from locust import User, task, constant, between, constant_pacing


class MyUser(User):
    duration = 1
    wait_time = constant(duration)

    @task
    def launch(self):
        print("This will inject delay of " + str(MyUser.duration))
