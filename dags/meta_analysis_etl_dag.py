from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

RAW_PATH = "/opt/airflow/dags/comorbidity_risks.csv"
TMP_PATH = "/opt/airflow/dags/tmp_extracted.csv"
OUTPUT_PATH = "/opt/airflow/dags/transformed_comorbidity_risks.csv"

def extract():
    df = pd.read_csv(RAW_PATH)
    df.to_csv(TMP_PATH, index=False)

def transform():
    df = pd.read_csv(TMP_PATH)
    df["Comorbidity_Count"] = df["Condition"].apply(lambda x: x.count("+") + 1 if "+" in x else 1)
    df["CI_Width"] = df["CI_Upper"] - df["CI_Lower"]
    df["Wide_CI_Flag"] = df["CI_Width"] > 3
    df.to_csv(OUTPUT_PATH, index=False)

def load():
    df = pd.read_csv(OUTPUT_PATH)
    print("Loaded data with shape:", df.shape)

with DAG(
    dag_id="meta_analysis_etl_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    description="ETL DAG for comorbidity risk factors meta-analysis"
) as dag:
    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3
