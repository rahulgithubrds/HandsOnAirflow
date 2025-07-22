#Bash
# This code will create an airflow connection with Snowflake

airflow connections add snowflake_default    \ 
  --conn-type snowflake \
  --conn-login <your_snowflake_username> \
  --conn-password '<your_snoflake_password'> \
  --conn-schema PUBLIC \
  --conn-extra '{"account": "PQVEFAQ-AN22787", "warehouse": "COMPUTE_WH","database": "QUICK_PRACTICE_DB","role": "ACCOUNTADMIN"}'
