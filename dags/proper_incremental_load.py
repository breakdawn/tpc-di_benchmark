from datetime import datetime

from airflow import DAG

from utils import construct_gcs_to_bq_operator, get_file_path, execute_sql

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 11),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG('proper_incremental_load', schedule_interval=None, default_args=default_args) as dag:
    load_customer_file_to_staging = construct_gcs_to_bq_operator('load_customer_to_staging',
                                                                 get_file_path(True, 'Customer'), [
                                                                     {"name": "CDC_FLAG", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "CDC_DSN", "type": "INTEGER",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_ID", "type": "INTEGER",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_TAX_ID", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_ST_ID", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_L_NAME", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_F_NAME", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_M_NAME", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_GNDR", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_TIER", "type": "INTEGER",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_DOB", "type": "DATE",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_ADLINE1", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_ADLINE2", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_ZIPCODE", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_CITY", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_STATE_PRO", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_CTRY", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_CTRY_1", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_AREA_1", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_LOCAL_1", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_EXT_1", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_CTRY_2", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_AREA_2", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_LOCAL_2", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_EXT_2", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_CTRY_3", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_AREA_3", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_LOCAL_3", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_EXT_3", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_EMAIL_1", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_EMAIL_2", "type": "STRING",
                                                                      "mode": "NULLABLE"},
                                                                     {"name": "C_LCL_TX_ID", "type": "STRING",
                                                                      "mode": "REQUIRED"},
                                                                     {"name": "C_NAT_TX_ID", "type": "STRING",
                                                                      "mode": "REQUIRED"}],
                                                                 'staging.customer')

    load_batch_date_from_file = construct_gcs_to_bq_operator('load_batch_date_from_file',
                                                             get_file_path(True, 'BatchDate'), [
                                                                 {"name": "BatchDate", "type": "DATE",
                                                                  "mode": "REQUIRED"}
                                                             ], 'staging.batch_date')

    update_batch_id = execute_sql(task_id='increment_batch_id', sql_file_path='queries/increment_batch.sql')

    [load_batch_date_from_file, update_batch_id, load_customer_file_to_staging]
