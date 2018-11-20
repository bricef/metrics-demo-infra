from locust import HttpLocust, TaskSet, task

class DemoLoadTest(TaskSet):
    @task(1)
    def test_endpoint(self):
        self.client.get("/test", headers={"Accept": "*/*"})


class MyLocust(HttpLocust):
    task_set = DemoLoadTest
    min_wait = 0
    max_wait = 15000
