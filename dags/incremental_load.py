from datetime import datetime

from airflow import DAG

from utils import construct_gcs_to_bq_operator, get_file_path

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 11),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG('incremental_load', schedule_interval=None, default_args=default_args) as dag:
    load_account_file_to_staging = construct_gcs_to_bq_operator('load_account_to_staging',
                                                                get_file_path(True, 'Account'), [
                                                                    {"name": "CDC_FLAG", "type": "STRING",
                                                                     "mode": "REQUIRED"},
                                                                    {"name": "CDC_DSN", "type": "INT64",
                                                                     "mode": "REQUIRED"},
                                                                    {"name": "CA_ID", "type": "INT64",
                                                                     "mode": "REQUIRED"},
                                                                    {"name": "CA_B_ID", "type": "INT64",
                                                                     "mode": "REQUIRED"},
                                                                    {"name": "CA_C_ID", "type": "INT64",
                                                                     "mode": "REQUIRED"},
                                                                    {"name": "CA_NAME", "type": "STRING",
                                                                     "mode": "NULLABLE"},
                                                                    {"name": "CA_TAX_ST", "type": "INT64",
                                                                     "mode": "REQUIRED"},
                                                                    {"name": "CA_ST_ID", "type": "STRING",
                                                                     "mode": "REQUIRED"}], 'staging.account')
    load_cash_transaction_file_to_staging = construct_gcs_to_bq_operator('load_cash_transaction_to_staging',
                                                                         get_file_path(True, 'CashTransaction'), [
                                                                             {"name": "CDC_FLAG", "type": "STRING",
                                                                              "mode": "REQUIRED"},
                                                                             {"name": "CDC_DSN", "type": "INTEGER",
                                                                              "mode": "REQUIRED"},
                                                                             {"name": "CT_CA_ID", "type": "INTEGER",
                                                                              "mode": "REQUIRED"},
                                                                             {"name": "CT_DTS", "type": "DATETIME",
                                                                              "mode": "REQUIRED"},
                                                                             {"name": "CT_AMT", "type": "FLOAT",
                                                                              "mode": "REQUIRED"},
                                                                             {"name": "CT_NAME", "type": "STRING",
                                                                              "mode": "REQUIRED"}],
                                                                         'staging.cash_transaction')
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

    load_daily_market_file_to_staging = construct_gcs_to_bq_operator('load_daily_market_to_staging',
                                                                     get_file_path(True, 'DailyMarket'), [
                                                                         {"name": "CDC_FLAG", "type": "STRING",
                                                                          "mode": "REQUIRED"},
                                                                         {"name": "CDC_DSN", "type": "INTEGER",
                                                                          "mode": "REQUIRED"},
                                                                         {"name": "DM_DATE", "type": "DATE",
                                                                          "mode": "REQUIRED"},
                                                                         {"name": "DM_S_SYMB", "type": "STRING",
                                                                          "mode": "REQUIRED"},
                                                                         {"name": "DM_CLOSE", "type": "NUMERIC",
                                                                          "mode": "REQUIRED"},
                                                                         {"name": "DM_HIGH", "type": "NUMERIC",
                                                                          "mode": "REQUIRED"},
                                                                         {"name": "DM_LOW", "type": "NUMERIC",
                                                                          "mode": "REQUIRED"},
                                                                         {"name": "DM_VOL", "type": "INTEGER",
                                                                          "mode": "REQUIRED"}],
                                                                     'staging.daily_market')

    load_holding_history_file_to_staging = construct_gcs_to_bq_operator('load_holding_history_to_staging',
                                                                        get_file_path(True, 'HoldingHistory'), [
                                                                            {"name": "CDC_FLAG", "type": "STRING",
                                                                             "mode": "REQUIRED"},
                                                                            {"name": "CDC_DSN", "type": "INTEGER",
                                                                             "mode": "REQUIRED"},
                                                                            {"name": "HH_H_T_ID", "type": "INTEGER",
                                                                             "mode": "REQUIRED"},
                                                                            {"name": "HH_T_ID", "type": "INTEGER",
                                                                             "mode": "REQUIRED"},
                                                                            {"name": "HH_BEFORE_QTY", "type": "INTEGER",
                                                                             "mode": "REQUIRED"},
                                                                            {"name": "HH_AFTER_QTY", "type": "INTEGER",
                                                                             "mode": "REQUIRED"}],
                                                                        'staging.holding_history')

    load_trade_file_to_staging = construct_gcs_to_bq_operator('load_trade_to_staging',
                                                              get_file_path(True, 'Trade'), [
                                                                  {"name": "CDC_FLAG", "type": "STRING",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "CDC_DSN", "type": "INTEGER",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_ID", "type": "INTEGER",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_DTS", "type": "DATETIME",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_ST_ID", "type": "STRING",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_TT_ID", "type": "STRING",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_IS_CASH", "type": "BOOLEAN",
                                                                   "mode": "NULLABLE"},
                                                                  {"name": "T_S_SYMB", "type": "STRING",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_QTY", "type": "INTEGER",
                                                                   "mode": "NULLABLE"},
                                                                  {"name": "T_BID_PRICE", "type": "NUMERIC",
                                                                   "mode": "NULLABLE"},
                                                                  {"name": "T_CA_ID", "type": "INTEGER",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_EXEC_NAME", "type": "STRING",
                                                                   "mode": "REQUIRED"},
                                                                  {"name": "T_TRADE_PRICE", "type": "NUMERIC",
                                                                   "mode": "NULLABLE"},
                                                                  {"name": "T_CHRG", "type": "NUMERIC",
                                                                   "mode": "NULLABLE"},
                                                                  {"name": "T_COMM", "type": "NUMERIC",
                                                                   "mode": "NULLABLE"},
                                                                  {"name": "T_TAX", "type": "NUMERIC",
                                                                   "mode": "NULLABLE"}],
                                                              'staging.trade')

    load_watch_history_file_to_staging = construct_gcs_to_bq_operator('load_watch_history_to_staging',
                                                                      get_file_path(True, 'WatchHistory'), [
                                                                          {"name": "CDC_FLAG", "type": "STRING",
                                                                           "mode": "REQUIRED"},
                                                                          {"name": "CDC_DSN", "type": "INTEGER",
                                                                           "mode": "REQUIRED"},
                                                                          {"name": "W_C_ID", "type": "INTEGER",
                                                                           "mode": "REQUIRED"},
                                                                          {"name": "W_S_SYMB", "type": "STRING",
                                                                           "mode": "REQUIRED"},
                                                                          {"name": "W_DTS", "type": "DATETIME",
                                                                           "mode": "REQUIRED"},
                                                                          {"name": "W_ACTION", "type": "STRING",
                                                                           "mode": "NULLABLE"}],
                                                                      'staging.watch_history')
