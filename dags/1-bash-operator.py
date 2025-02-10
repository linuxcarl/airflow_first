from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
with DAG(dag_id="bash_operator",
    description="Bash Operator",
    start_date=datetime(2025,2,10),
) as dag:
    opr= BashOperator(task_id="bash_operator", bash_command="echo 'Hello platzi people with bash operator!'")