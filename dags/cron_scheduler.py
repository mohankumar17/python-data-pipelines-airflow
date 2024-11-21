from datetime import datetime, timedelta
from airflow.decorators import dag, task

@dag(
    #schedule_interval="@daily",
    schedule_interval="45 6 * * *", # 06:45 AM Daily [UTC Timezone]
    start_date=datetime(2024, 11, 18),
    catchup=True
)
def cron_scheduler_sample_dag():
    
    @task()
    def sample_task():
        print("Cron Expression Schedule based Sample DAG")

    sample_task()

cron_scheduler_sample_dag()