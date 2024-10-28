from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from src.get_wiki_data import get_wiki_data

dag = DAG(
    dag_id='dag_football',
    default_args={
        "owner":"Karan",
        "start_date":datetime(2024,10,22),
    },
    schedule_interval=None,
    catchup=False
)

# Extraction
extract_data_wiki = PythonOperator(
    task_id = "extract_data_wiki",
    python_callable=get_wiki_data,
    provide_context=True,
    op_kwargs={
        "url": "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"},
    dag=dag    
)
# preprocessing

# loading