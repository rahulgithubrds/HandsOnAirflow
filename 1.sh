# This code will create an airflow connection with Snowflake

airflow connections add snowflake_default \
  --conn-type snowflake \
  --conn-host AN22787.us-west-2.aws.snowflakecomputing.com \
  --conn-login snowflake_login_username \
  --conn-password snowflake_login_password \
  --conn-schema PUBLIC \
  --conn-extra '{
      "account": "PQVEFAQ-AN22787",
      "warehouse": "COMPUTE_WH",
      "database": "QUICK_PRACTICE_DB",
      "region": "us-west-2",
      "role": "ACCOUNTADMIN"
  }'
