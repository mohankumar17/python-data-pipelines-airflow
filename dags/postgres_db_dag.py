# Expose port 5432 for postgres in docker-compose.yaml file
# Use host as: host.docker.internal for windows

from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id="postgres_db_dag",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(seconds=30)
    },
    description="A Sample DAG that interact with Postgres SQL Database",
    schedule="@once",
    start_date=datetime(2024, 11, 21),
    catchup=False,
) as dag:
    create_user_table_task = PostgresOperator(
        task_id="create_user_table",
        postgres_conn_id="postgres_db_conn",
        sql="""
            CREATE TABLE IF NOT EXISTS USERS(
                user_id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT CHECK (age >= 0)
            );
            """
    )

    insert_user_task = PostgresOperator(
        task_id="insert_user",
        postgres_conn_id="postgres_db_conn",
        sql="""
            INSERT INTO USERS(name, age) 
            VALUES ('Paul', 35);
            """
    )

    create_user_table_task >> insert_user_task

