# API Tests - Using Python 

## This repository purpose is to showcase the automatically generated test assertions for the happy path scenario.

## What is Python and Pytest Framework 

`Python` is a high-level, general-purpose programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is designed to be easy to learn and has a clean and concise syntax, which makes it a popular choice for both beginners and experienced programmers.

The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

### Setup of dependencies for the tests 

To activate our environment, we use the command:
```bash
python -m venv venv
venv\Scripts\Activate
```
If everything is correct, your environment will be activated and on the cmd you will see like this:
```bash
(name_of_environment) C:\User\tests 
```
To disable your environment just run:
```bash
deactivate
```
### Setup:

```bash
pip install -r requirements.txt
```
If you update the libraries version you can freeze update requirements
```bash
pip freeze > requirements.txt
```

### Run with Docker

```bash
 docker run -it --rm --name <testname> -v ${pwd}:/app -w /app <imagename>
```

### For the report generation use 

```bash
pytest test.py --html-report=./report/report.html 
```
OR
```bash
pytest ./tests/test_dummy.py -s -v --html=./report/report.html
```
### To run specific test function

focused test
```bash
pytest ./tests/test_dummy.py -s -v -k test_get_products --html=./report/report.html
```
### Definition of the API that will be tested

API Testing with Requests and Pytest
This repository contains Python scripts for testing an API using the requests library and the pytest framework. The API being tested is the DummyJSON API.

Configuration: Create a .env file with the necessary evironment parameters. Example:

### config.ini file

TOKEN=aaaaaaa
BASE_URL=https://dummyjson.com
PRODUCT=phone
LIMIT=10
USER=xxxxxxx
PASSWORD=yyyyyyyy
PHONES=smartphones

Running all the tests
Run the tests using the following command:

```bash
pytest ./tests/test_dummy.py
```
### Test Descriptions



About the API:
- Base URL: `https://dummyjson.com`


For this tutorial, we will focus on three types of tests:
- Contract: If the API is able to validate the query parameters that are sent 
- Status: If the status codes are correct 
- Authentication: Even this API doesn't requires the token, we can do tests with this 

Our Scenarios:

- Positive testing of a user flow 

### CI

- CircleCI
- GitHUb Actions

### Performance tests with Locust

- Performance test scenario for different endpioints

To run tests use:

- locust -f ./perf_tests/locust.py --headless --users 10 --spawn-rate 10 --run-time 30 --stop-timeout 10s --host https://dummyjson.com

OR

- locust --config locust.conf

To see the real time metrics:

- run docker compose up -d
- start the grafana and set up the data source to prometheus
- choose the dashboard: docs https://medium.com/devopsturkiye/locust-real-time-monitoring-with-grafana-66654bb4b32

To use JTL reporter:

- git clone https://github.com/ludeknovy/jtl-reporter.git
- docker-compose up -d
- Now open the application in your browser: http://IP_ADDRESS:2020
- Download jtl_listener.py into your locust project folder.

- Register the listener in your locust test by placing event listener at the very end of the file:

- from jtl_listener import JtlListener
- 
```bash
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    JtlListener(env=environment,  project_name="project name",
                scenario_name="scenario name",
                environment="tested envitonment",
                backend_url="http://IP_ADDRESS")
```
- Generate api token in the application and set it as JTL_API_TOKEN env variable.

- After the test finishes you will find a jtl file in logs folder.
- Docs: https://jtlreporter.site/docs/integrations/locust