from datetime import datetime, timedelta
from airflow.decorators import dag, task

@dag(
    schedule=timedelta(days=1),
    start_date=datetime(2024, 11, 18),
    catchup=True #Default True -> Will run from scheduled start_date to until present date/moment
)
def catchup_sample_dag():
    
    @task()
    def sample_task():
        print("Task in Catchup Sample DAG")

    sample_task()

catchup_sample_dag()