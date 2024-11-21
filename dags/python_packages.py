# Install the additinal packages to airflow docker container

# 1. Specify additional packages in requirements.txt in local.
# 2. Use Dockerfile to run pip command for installing custom packages specified in requirements.txt
# 3. Use the following command to build new image from existing airflow image
#    >  docker build . --tag custom_airflow:1.0.0
# 4. Update the image name in env and docker-compose.yaml file with new image name "custom_airflow:1.0.0"
# 5. Run docker-componse up -d to start containers from new image

from datetime import datetime, timedelta
from airflow.decorators import dag, task

@dag(
    schedule=timedelta(days=1),
    start_date=datetime(2024, 11, 18),
    catchup=False
)
def pydantic_dag():
    from pydantic import BaseModel

    @task()
    def validate_schema():
        class User(BaseModel):
            id: int
            name: str
        
        user = User(id=1, name="Paul") 
        print(user)

    validate_schema()

pydantic_dag()