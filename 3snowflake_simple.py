# ~/airflow/dags/snowflake_simple.py
# DAG File

from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 24),
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=2),
    'email_on_failure': True,
}

with DAG(
    "snowflake_simple_fixed",
    start_date=datetime(2025, 7, 24),
    schedule=None,
    catchup=False,
    default_args=default_args,
    max_active_runs=1
) as dag:

    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    # 1. Activate warehouse first
    activate_warehouse = SQLExecuteQueryOperator(
        task_id="activate_warehouse",
        conn_id="snowflake_default",
        sql="ALTER WAREHOUSE COMPUTE_WH RESUME;"
    )

    # 2. Connection test (after warehouse resume)
    test_connection = SQLExecuteQueryOperator(
        task_id="test_connection",
        conn_id="snowflake_default",
        sql="SELECT CURRENT_VERSION() AS snowflake_version",
        show_return_value_in_logs=True
    )

    # 3. Robust table creation
    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="snowflake_default",
        sql="""
        BEGIN;
        CREATE TABLE IF NOT EXISTS QUICK_PRACTICE_DB.PUBLIC.airflow_practice_table (
            id INT,
            name STRING,
            value NUMBER,
            created_at TIMESTAMP_LTZ DEFAULT CURRENT_TIMESTAMP()
        );
        COMMIT;
        """,
        retries=2,
        retry_delay=timedelta(minutes=0.5)
    )

    # 4. Insert data
    insert_data = SQLExecuteQueryOperator(
        task_id="insert_data",
        conn_id="snowflake_default",
        sql="""
        INSERT INTO QUICK_PRACTICE_DB.PUBLIC.airflow_practice_table (id, name, value)
        VALUES
            (1, 'test', 42),
            (2, 'demo', 3.14),
            (3, 'airflow', 100)
        """
    )

    # 5. Query data
    query_data = SQLExecuteQueryOperator(
        task_id="query_data",
        conn_id="snowflake_default",
        sql="SELECT * FROM QUICK_PRACTICE_DB.PUBLIC.airflow_practice_table",
        show_return_value_in_logs=True
    )

    # Dependencies with warehouse activation first
    # start >> activate_warehouse >> test_connection >> create_table >> insert_data >> query_data >> end

    #  warehouse activation step is skipped below
    start >> test_connection >> create_table >> insert_data >> query_data >> end
