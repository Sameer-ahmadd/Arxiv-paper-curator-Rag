from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta


@task
def hello_world():
    """
    This function prints "Hello World"
    """
    print("Airflow DAG is running")
    return "Success"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# DAG defination
dag = DAG(
    "hello_world_week1",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["week1", "testing"],
)

# Execute the task
hello_world()
