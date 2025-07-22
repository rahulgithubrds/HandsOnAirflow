# ~/test_snowflake.py
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_connection():
    try:
        logger.info("Testing Snowflake connection")
        hook = SnowflakeHook(snowflake_conn_id="snowflake_default")
        conn = hook.get_conn()
        cursor = conn.cursor()

        # Test basic queries
        cursor.execute("SELECT CURRENT_ACCOUNT()")
        account = cursor.fetchone()[0]
        logger.info(f"Connected to account: {account}")

        cursor.execute("SHOW DATABASES LIKE 'QUICK_PRACTICE_DB'")
        db_exists = cursor.fetchone()
        logger.info(f"Database exists: {bool(db_exists)}")

        return True
    except Exception as e:
        logger.error(f"Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_connection()
