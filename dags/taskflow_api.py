from datetime import datetime, timedelta
from airflow.decorators import dag, task
#from airflow.models import Variable

@dag(
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False
)
def taskflow_etl_dag():

    @task()
    def extract():
        print("Data Extraction")
        
        return [100, 200, 350]
        

    @task() #multiple_outputs=True
    def transform(data):
        print("Data Transformation")
        return {
            "result": sum(data)
        }

    @task()
    def load(data):
        print("Data Loading")
        print(f"Sum: {data.get('result')}")
    
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load(transformed_data)

taskflow_etl_dag()
