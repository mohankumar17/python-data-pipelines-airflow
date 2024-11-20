from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def extract(**kwargs):
    print("Data Extraction")

    ti = kwargs["ti"]
    extracted_data = [100, 200, 350]
    ti.xcom_push("extracted_data", extracted_data)  # XComm Limitation - Max data size is 48KB

def transform(**kwargs):
    print("Data Transformation")

    ti = kwargs["ti"]
    extracted_data = ti.xcom_pull(task_ids="python_extract", key="extracted_data")
    transformed_data = sum(extracted_data)
    ti.xcom_push("transformed_data", transformed_data)

def load(**kwargs):
    print("Data Loading")

    ti = kwargs["ti"]
    transformed_data = ti.xcom_pull(task_ids="python_transform", key="transformed_data")
    print(f"Loaded Data: {transformed_data}")

with DAG(
    "sample_etl_dag",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    },
    description="A Sample ETL DAG that uses BashOperator and PythonOperator",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    t1 = BashOperator(
        task_id="bash_print_message",
        depends_on_past=True,
        bash_command="echo 'Welcome to Apache Airflow ETL Pipeline'",
        retries=3
    )

    t2 = PythonOperator(
        task_id="python_extract",
        python_callable=extract
    )

    t3 = PythonOperator(
        task_id="python_transform",
        python_callable=transform
    )

    t4 = PythonOperator(
        task_id="python_load",
        python_callable=load
    )

    t1 >> t2 >> t3 >> t4