from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd

@dag(
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False
)
def database_file_etl_dag():
    @task()
    def extract(fileName):
        db_hook = PostgresHook(postgres_conn_id="postgres_db_conn")
        conn = db_hook.get_conn()
        curr = conn.cursor()
        
        curr.execute("SELECT order_id, customer_name, product_name, order_date, total_amount, status FROM ORDERS WHERE status='Shipped';")
        orders = curr.fetchall()
        
        df = pd.DataFrame(orders, columns=["order_id", "customer_name", "product_name", "order_date", "total_amount", "status"])
        df.to_csv(fileName, sep=",", mode="w", header=True, index=False, index_label=None)

        return df.shape[0]

    @task()
    def transform(fileName, tot_records):
        print(f"Total Records: {tot_records}")
        df = pd.read_csv(fileName)

        df["total_amount"] = df["total_amount"].astype(float)
        df["total_amount"] = df["total_amount"] * 80
        df.drop(axis=1, columns=["status"])

        df.to_csv(fileName, sep=",", mode="w", header=True, index=False, index_label=None)

    @task()
    def load(fileName):
        #df.to_csv(fileName)
        pass
    
    fileName = "dags/resources/shipped_orders.csv"
    tot_records = extract(fileName)
    transform(fileName, tot_records)
    #load()

database_file_etl_dag()