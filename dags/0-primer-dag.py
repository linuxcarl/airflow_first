from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator
#with cotext manager
with DAG(
    dag_id="primer-dag",
    description ="primer dag",
    start_date=datetime(2025,2,10),
    schedule_interval="@once",
) as dag:
    task_1= EmptyOperator(task_id="dummy")