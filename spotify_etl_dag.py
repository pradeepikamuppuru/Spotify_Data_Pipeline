from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from spotify_etl import fetch_spotify_artist_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='DAG to fetch Spotify artist data',
    schedule_interval=timedelta(days=1),
)

def run_spotify_etl():
    client_id = 'b19960c6a802437b9f****bb1d***'
    client_secret = '3819c29b*****e689b72b36****f*'
    
    df = fetch_spotify_artist_data(client_id, client_secret)
    df.to_csv('s3://21121a2933/spotify_artist_data.csv', index=False)
    print("Spotify artist data fetched and saved successfully.")

run_etl = PythonOperator(
    task_id='complete_spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag,
)

run_etl
