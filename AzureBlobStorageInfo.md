In order to connect to Azure Blob storage from Airflow you need:
The Docker image needs to be built with the `azure-storage-blob` Python dependency. To do that:

(Following instructions at: https://github.com/puckel/docker-airflow)
1. If you're on Windows, make sure git is set to check out files with Unix-style line endings:
`git config --global core.autocrlf false`
If you don't do this you can get the error discussed here: https://stackoverflow.com/questions/29045140/env-bash-r-no-such-file-or-directory
2. Clone the repo: 
`git clone https://github.com/puckel/docker-airflow.git`
3. Pull the image: 
`docker pull puckel/docker-airflow`
4. Build the image with the Azure Storage Blob dependency:
 `docker build --rm --build-arg PYTHON_DEPS="azure-storage-blob==2.1.0" -t puckel/docker-airflow .`
* Make sure you include the period at the end of the `docker build` command. :)
* The `2.1.0` version of the `azure-storage-blob` Python package was required at the time these instructions were written.
5. You can then start your Docker container and use the Azure Storage Blob sensor in a DAG.

## Python code needed to use the Azure Storage Blob sensor:
```
from airflow.contrib.sensors.wasb_sensor import WasbBlobSensor

azure_blob_check = WasbBlobSensor(
    task_id='blob_check',
    container_name='blob-test',
    blob_name='test/TestCSV.csv',
    wasb_conn_id='wasb_default',
    dag=dag
)
```
`blob_name` is a file path. This took me a long time to figure out. I don't know if wildcards are allowed.

## Configure the Azure Storage Blob connection in Airflow
On the Airflow admin site under `Admin->Connections` edit the `wasb_default` connection:
1. Enter the Azure storage account name in the `Login` field. Example: `ssisuploadazureblobtest`
2. Enter an access key in the `Password` field. 
Storage account name and access keys are available in Azure on the `Storage Account -> Access Keys` page.


### In Azure you need:
1. A storage account
2. A container within the storage account
