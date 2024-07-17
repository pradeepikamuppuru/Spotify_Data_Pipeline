sudo apt-get update
sudo apt-get install -y python3-pip python3-dev
sudo apt-get install -y python3-venv

#Create a virtual environment
python3 -m venv airflow-env

#Activate the virtual environment
source airflow-env/bin/activate

#Installing necessary packages
pip install apache-airflow
pip install spotipy
pip install s3fs
pip install spotipy

#If you want to create a new user, use the following command
airflow users create \
--username admin \
--firstname FIRST_NAME \
--lastname LAST_NAME \
--role Admin \
--email admin@example.com

#Use following commands to upload the codes to airflow
nano airflow.cfg
mkdir spotify_dag.py
cd spotify_dag.py
ls
nano spotify_etl.py
#enter spotify_etl code
nano spotify_dag_code.py
#enter dag code

#Use the following command to assign to correct port
airflow webserver -p 8080
or
airflow standalone

