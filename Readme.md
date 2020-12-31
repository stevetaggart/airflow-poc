# Apache Airflow Proof of Concept
This POC shows how to run Apache Airflow on a local machine using Docker. It includes an Airflow DAG that uses the Pandas Python package to read a CSV file and write the data into a new CSV file.

## Local Machine Requirements
1. Docker must be installed. Install Docker Desktop for Windows or Mac depending on your OS. You might have to create a Docker Hub account to download Docker. 
2. Enable Shared Drives in the Docker settings.
3. Visual Studio Code with the [Docker Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) and the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.


## Instructions
First, clone this git repository to your local machine.

## Start the Docker container
In a terminal window run `docker-compose up -d` from the repository directory. This is the directory that contains the `docker-compose.yml` file. This spins up a Docker container that has Python and Apache Airflow installed and configured. It also makes the local `dags` and `files` directories available to the container.

## Attach VS Code to the container
1. Open the repository directory in VS Code.
2. Click on the Docker extension. You should see a running container.
3. Right-click on the running container and select Attach Visual Studio Code. This opens up a new instance of VS Code that attaches to the container.

## Load the `transform_csv` DAG into Airflow
1. Open a new Terminal in the attached instance of VS Code.
2. Run `python /usr/local/airflow/dags/transform_csv.py`. It should run quickly and only provides output if there are errors.

## Run the Airflow `transform_csv` DAG
1. Open http://localhost:8080 in a browser on your local machine to load the Airflow admin site. Be sure to use http because https doesn't work.
2. Click on the DAGs menu item. You should see several example DAGs listed. Look for the `transform_csv` DAG. This is a DAG created for the POC. 
3. Enable the `transform_csv` DAG by flipping the switch on the left to ON. 
4. Click on the little Trigger Dag icon (it looks like a play button).
5. You should get a prompt saying "Are you sure you want to run 'transform_csv' now?" Click on OK.

### View the DAG status in the Airflow UI
1. Click on the *Browse* menu item and then on *Dag Runs*.
2. It takes some time (a couple of minutes) for the DAG to finish running. You can refresh this page until the status shows *Success* instead of *Running*.
3. Once the status is *Success*, click on `transform_csv` in the *Dag Id* column. This should take you to a graph view of the DAG.
4. Click on the `load_csv` box in the graph. This should bring up a modal dialog.
5. Click on the *View Log* button. You should see the log for the `load_csv` task.

### View the transformed CSV
If the DAG ran successfully, you should see a new file `TestCSV.csv.loaded` in the `files` directory alongside the original `TestCSV.csv` file. The files should have the same contents. In the attached instance of VS Code, you might need to open the `/usr/local/airflow` folder (File->Open Folder...) to see the files in the `files` directory. You could also open a new Terminal in the attached instance of VS Code to look at the files.


