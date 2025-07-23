Environment used in this code example:
1. Snowflake - Free Trail Account
2. Airflow Version 3.0.2
3. Operating System Ubuntu 20.04 LTS (WSL).
4. Check Airflow UI 

Snowflake Setup & Configuration: 
1. Create Snowflake Trial Account
2. Create DB, Schemas
3. Grant access in snowflake:
   
   -- Grant ability to use roles (e.g. ACCOUNTADMIN)
   GRANT ROLE ACCOUNTADMIN TO USER <your_snowflake_user>;

   -- Grant database privileges
   GRANT USAGE ON DATABASE <snowfalek_db> TO ROLE ACCOUNTADMIN;
   GRANT CREATE SCHEMA ON DATABASE <snowfalek_db> TO ROLE ACCOUNTADMIN;
   GRANT USAGE ON SCHEMA <snowfalek_db>.<schema_name> TO ROLE ACCOUNTADMIN;
   GRANT CREATE TABLE ON SCHEMA <snowfalek_db>.<schema_name> TO ROLE ACCOUNTADMIN;
   GRANT INSERT, SELECT ON ALL TABLES IN SCHEMA <snowfalek_db>.<schema_name> TO ROLE ACCOUNTADMIN;

   -- Grant warehouse privileges (e.g. COMPUTE_WH)
   GRANT USAGE ON WAREHOUSE COMPUTE_WH TO ROLE ACCOUNTADMIN;

Installation: 
(Bash)
1. Install python, pip
2. Create a folder in HOME folder (~) of the Ubuntu User (e.g. airflow)
3. export AIRFLOW_HOME=~/airflow
4. pip install apache-airflow
5. airflow db migrate # use migrate for higher version of airflow (otherwise use airflow db init) 
6. airflow standalone ( this will start webserver and scheduler)
   - Airflow User Credentilas will be created automatically in stand alone mode
   - Note down the passwrod for default Airflow Useer 'admin' (Use these credential to be used to Login into Airflow UI)
   - Otherwise, please refer Airflow Documentation to Create User for Airflow.

Run & Test:
- Follow the code in repository in the sequence of file names
