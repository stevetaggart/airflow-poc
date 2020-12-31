from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from code_in_another_file import load_csv

default_args = {
    'owner': 'owner',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email': ['email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

dag = DAG('transform_csv', default_args=default_args, schedule_interval=timedelta(days=1))

transform_csv_task = PythonOperator(
        task_id='load_csv',
        python_callable=load_csv,
        provide_context=True,
        op_kwargs={'local_path': '/usr/local/airflow/files/TestCSV.csv'},
        dag=dag)

print_date_task = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

another_print_date_task = BashOperator(
    task_id='another_print_date',
    bash_command='date',
    dag=dag
)

transform_csv_task >> print_date_task  >> another_print_date_task