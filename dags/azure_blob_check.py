from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.sensors.wasb_sensor import WasbBlobSensor
from datetime import datetime, timedelta

from code_in_another_file import load_csv

# This DAG requires an external Python package for interacting with Azure
# See AzureBlobStorageInfo.md for information about running this DAG

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

dag = DAG('azure_blob_check', default_args=default_args, schedule_interval=timedelta(days=1))

azure_blob_check = WasbBlobSensor(
    task_id='blob_check',
    container_name='blob-test',
    blob_name='test/TestCSV.csv',
    wasb_conn_id='wasb_default',
    dag=dag
)

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

azure_blob_check >> transform_csv_task >> print_date_task  >> another_print_date_task