# Use Dockerfile to run pip command for installing custom packages specified in requirements.txt
# Use below command to build new image from existing airflow image
# docker buildx build . --tag extending_airflow:latest

from datetime import datetime, timedelta
from airflow.decorators import dag, task

@dag(
    schedule=timedelta(days=1),
    start_date=datetime(2024, 11, 18),
    catchup=False
)
def api_requests_dag():
    import requests

    @task()
    def get_call():
        res = requests.get("https://jsonplaceholder.typicode.com/users/1")
        user = res.json()
        print("User: ", user)

    get_call()

api_requests_dag()