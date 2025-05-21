# Airflow ETL: Meta-Analysis of Comorbidity Risk Factors

This project demonstrates an end-to-end ETL pipeline using Apache Airflow inside Docker.

## Use Case

We extract and transform data from a simulated meta-analysis of COVID-19 mortality relative risks (RRs) associated with various comorbid conditions. The pipeline performs:

- Data ingestion from CSV
- CI width calculation
- Comorbidity count extraction
- Flagging wide confidence intervals

## Project Structure

```
dags/
├── meta_analysis_etl_dag.py          # Main ETL DAG
└── comorbidity_risks.csv             # Input data
```

## How to Run

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/airflow-etl-project.git
   cd airflow-etl-project
   ```
3. Download Airflow’s Docker Compose config:
   ```bash
   curl -LfO https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml
   ```
4. Set up environment:
   ```bash
   mkdir logs plugins
   echo AIRFLOW_UID=50000 > .env
   docker-compose up airflow-init
   docker-compose up
   ```

5. Visit `http://localhost:8080` and log in (default user: airflow / airflow)

## Output

Creates a cleaned output file:

```
dags/transformed_comorbidity_risks.csv
```

With added columns:
- `Comorbidity_Count`
- `CI_Width`
- `Wide_CI_Flag`

## Sample DAG Run

All tasks are orchestrated via Airflow:
- Extract → Transform → Load
