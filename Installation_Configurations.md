# HandsOnAirflow

Setup:
1. Airflow Version 3.0.2
2. Operating System Ubuntu 20.04 LTS (WSL).
3. Snowflake - Free Trail Account

Snowflake Config: 
1. Grant All Privillages (in advance) to the Role and Databas, Schema, Tables in Snowflake
e.g.
-- Grant ability to use roles
GRANT ROLE ACCOUNTADMIN TO USER <your_snowflake_user>;

-- Grant database privileges (assuming QUICK_PRACTICE_DB exists)
GRANT USAGE ON DATABASE QUICK_PRACTICE_DB TO ROLE ACCOUNTADMIN;
GRANT CREATE SCHEMA ON DATABASE QUICK_PRACTICE_DB TO ROLE ACCOUNTADMIN;
GRANT USAGE ON SCHEMA QUICK_PRACTICE_DB.PUBLIC TO ROLE ACCOUNTADMIN;
GRANT CREATE TABLE ON SCHEMA QUICK_PRACTICE_DB.PUBLIC TO ROLE ACCOUNTADMIN;
GRANT INSERT, SELECT ON ALL TABLES IN SCHEMA QUICK_PRACTICE_DB.PUBLIC TO ROLE ACCOUNTADMIN;

-- Grant warehouse privileges (replace YOUR_WAREHOUSE)
GRANT USAGE ON WAREHOUSE COMPUTE_WH TO ROLE ACCOUNTADMIN;

2. Set snowflake connection paramters accuratly 
