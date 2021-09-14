import os
import pandas as pd
from tqdm import tqdm  # Progress Bar
import time
import ControllerOutput001 as ActionTaskOne
from Util import PlaceStorageStrings as Configure


# IndexTaskMaker      / PURPOSE: To Read data from excel tables and create new Join data tables.
# Cleaner             / PURPOSE: To Clean all my data source special Character such as: the @ symbol and others besides letters from fields date time
# PlaceStorageStrings / PURPOSE: To storage strings used to configure the program or status words and phrases.
# ControllerOutput001 / PURPOSE: To storage the methods with actions and specific behaviors, such as: report maker, filters, output viewers to cmd prompt.

def load_dbase():
    files = tqdm([file for file in os.listdir(Configure.input_folder)])

    all_data_tables = pd.DataFrame()

    for file in files:
        df = pd.read_excel(Configure.input_folder + file)
        time.sleep(0.8)
        all_data_tables = pd.concat([all_data_tables, df])

    # CREATE A ADDITIONAL COLUMN
    all_data_tables['Month'] = all_data_tables['Opened'].str[0:2]
    # HERE INITIALLY STORAGE A MONTH NUMBER DAY FROM THE COLUMN Opened ( Day of creation for this task )

    # CREATE A BASE TABLE
    all_data_tables.to_excel(Configure.output_folder + Configure.basic_join_file, index=False)


if __name__ == '__main__':
    # ATTENTION USE THESE EXECUTION METHODS BELOW IN THIS SPECIFIC ORDER.....
    load_dbase()                                                # ORDER EXECUTION 000
    ActionTaskOne.company_work_join_file_maker()                # ORDER EXECUTION 001
    ActionTaskOne.company_colet_day_report_maker()              # ORDER EXECUTION 002
    ActionTaskOne.filter_task_red_phrases()                     # ORDER EXECUTION 003 -> RED
    ActionTaskOne.filter_task_scheduled_phrases()               # ORDER EXECUTION 004 -> BLUE
    ActionTaskOne.filter_task_no_red_phrases()                  # ORDER EXECUTION 005 -> YELLOW
    ActionTaskOne.filter_count_today_phrases_status()           # ORDER EXECUTION 006
    ActionTaskOne.count_all_day_phrases_status()                # ORDER EXECUTION 007
    ActionTaskOne.count_live_day_task()                         # ORDER EXECUTION 009 -> JUST A TEST
