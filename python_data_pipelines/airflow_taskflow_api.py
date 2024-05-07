from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.models import Variable

@dag(
    schedule=timedelta(seconds=30),
    start_date=datetime(2021, 1, 1),
    catchup=False,
)
def etl_dag():

    sample_api_key = Variable.get(key="sample_api_key", default_var="")

    @task()
    def extract(sample_api_key):
        print("Data Extraction")
        print(f"API Key: {sample_api_key}")
        
        if len(sample_api_key) > 0:
            return [100, 200, 350]
        else:
            return []

    @task() #multiple_outputs=True
    def transform(data: list) -> dict[str, int]:
        print("Data Transformation")
        return {
            "result": sum(data)
        }

    @task()
    def load(data):
        print("Data Loading")
        print(f"Sum: {data.get('result')}")
    
    extracted_data = extract(sample_api_key)
    transformed_data = transform(extracted_data)
    load(transformed_data)

etl_dag()
