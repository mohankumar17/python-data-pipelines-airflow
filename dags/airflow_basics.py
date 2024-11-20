from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def display_message(**kwargs):
    print("Hello, This is Python Method")

with DAG(
    "basic_dag",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(seconds=30)
    },
    description="A Sample ETL DAG that uses BashOperator",
    schedule=timedelta(minutes=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    t1 = BashOperator(
        task_id="bash_print_message",
        depends_on_past=True,
        bash_command="echo 'Welcome to Apache Airflow'",
        retries=3
    )

    t2 = BashOperator(
        task_id="bash_print_date",
        depends_on_past=True,
        bash_command="date",
        retries=3
    )

    t3 = PythonOperator(
        task_id="python_print_message",
        python_callable=display_message
    )

    t1 >> [t2 >> t3]