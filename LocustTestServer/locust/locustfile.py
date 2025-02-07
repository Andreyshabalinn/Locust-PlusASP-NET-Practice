from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 2)  # Ждём 1-2 секунды между запросами

    @task
    def test_endpoint(self):
        self.client.get("/test")