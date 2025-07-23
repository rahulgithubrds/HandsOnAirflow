# Bash
# This code will create an airflow connection with Snowflake
# Paramters values used here are just for demonstrations

airflow connections add snowflake_default    \ 
  --conn-type snowflake \
  --conn-login <snowflake_username> \
  --conn-password '<snoflake_password'> \
  --conn-schema PUBLIC \
  --conn-extra '{"account": "PQVEFAQ-AN22787", "warehouse": "COMPUTE_WH","database": "QUICK_PRACTICE_DB","role": "ACCOUNTADMIN"}'
