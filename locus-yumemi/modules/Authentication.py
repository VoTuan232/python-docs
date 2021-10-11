from locust import task, between
import json
from locust.user.task import TaskSet


class Authentication(TaskSet):
    wait_time = between(1, 5)

    def __init__(self, parent):
        super().__init__(parent)
        self.token = ''
        self.headers = {}

    def on_start(self):
        self.token = self.login()
        self.headers = {'x-sendy-session': self.token}

    def on_stop(self):
        self.logout()

    def login(self):
        response = self.client.post("/authentication/login",
                                    json={
                                        "email": "yumemi@example.com",
                                        "password": "12345678a"
                                    })
        return json.loads(response._content)['token']['accessToken']

    def logout(self):
        self.client.headers = self.headers
        self.client.post("/authentication/logout")