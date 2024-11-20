from datetime import datetime, timedelta
from airflow.decorators import dag, task
#from airflow.models import Variable

@dag(
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False
)
def taskflow_etl_dag():

    #sample_api_key = Variable.get(key="sample_api_key", default_var="")
    sample_api_key = "AXT12ohsdgoojf32423kbklk"

    @task()
    def extract(sample_api_key):
        print("Data Extraction")
        print(f"API Key: {sample_api_key}")
        
        if len(sample_api_key) > 0:
            return [100, 200, 350]
        else:
            return []

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
    
    extracted_data = extract(sample_api_key)
    transformed_data = transform(extracted_data)
    load(transformed_data)

taskflow_etl_dag()
