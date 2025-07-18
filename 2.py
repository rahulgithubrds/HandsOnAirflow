# Code will test Airflow connection with Snowflake save this python script as test_snowflake.py

from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

def test_connection():
    try:
        hook = SnowflakeHook(snowflake_conn_id="snowflake_default")
        conn = hook.get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION()")
        result = cursor.fetchone()
        print(f"Success! Snowflake version: {result[0]}")
    except Exception as e:
        print(f"Connection failed: {str(e)}")

if __name__ == "__main__":
    test_connection()
