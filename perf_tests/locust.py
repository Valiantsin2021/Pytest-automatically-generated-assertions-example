from locust import FastHttpUser, task, between, events
import os
import logging
from jtl_listener import JtlListener


class WebsiteUser(FastHttpUser):
    wait_time = between(1, 2)
    base_url = os.getenv("BASE_URL", "https://dummyjson.com")

    @task
    def test_home(self):
        response = self.client.get(self.base_url)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"
        # Add more assertions as needed

    @task
    def test_products(self):
        response = self.client.get(f"{self.base_url}/products")
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

    @task
    def test_single_product(self):
        response = self.client.get(f"{self.base_url}/products/1")
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

    @task
    def test_search_product(self):
        product = os.getenv("PRODUCT")
        response = self.client.get(f"{self.base_url}/products/search?q={product}")
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

    @task
    def test_limit_products(self):
        limit = os.getenv("LIMIT")
        response = self.client.get(
            f"{self.base_url}/products?limit={limit}&skip={limit}&select=title,price"
        )
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"


@events.quitting.add_listener
def _(environment, **kw):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 200:
        logging.error("Test failed due to average response time ratio > 100 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 800:
        logging.error("Test failed due to 95th percentile response time > 100 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    JtlListener(env=environment,  project_name="project name",
                scenario_name="scenario name",
                environment="tested environment",
                backend_url="http://localhost:2020")

# locust -f ./perf_tests/locust.py --headless --users 10 --spawn-rate 10 --run-time 30 --stop-timeout 10s --host https://dummyjson.com --csv ./report/locust/example
# locust -f locust_file.py --headless --users 10 --spawn-rate 10 --run-time 30 --stop-timeout 10s --processes 4
# to auto calculate the procesess to start pass --processes -1
# to run with config file use locust --config locust.conf
# set test dir with cli args  -f/--locustfile (like locust -f locustfiles/locustfile1.py,locustfiles/locustfile2.py,locustfiles/more_files/locustfile3.py)
# for reports  --csv example The files will be named example_stats.csv, example_failures.csv, example_exceptions.csv and example_stats_history.csv (when using --csv example).
