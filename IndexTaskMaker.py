import os
import pandas as pd
from tqdm import tqdm  # Progress Bar
import time
import PatternTableViewOne as reportOne
from Util import Cleaner as Clean
from Util import PlaceStorageStrings as Configure


# IndexTaskMaker / PURPOSE: To Read data from excel tables and create new  Join data tables.
# PatternTableViewOne / PURPOSE: .......
# Cleaner             / PURPOSE: .......
# PlaceStorageStrings / PURPOSE: .......

def load_dbase():
    files = tqdm([file for file in os.listdir(Configure.input_folder)])

    all_data_tables = pd.DataFrame()

    for file in files:
        df = pd.read_excel(Configure.input_folder + file)
        time.sleep(0.8)
        all_data_tables = pd.concat([all_data_tables, df])

    # CREATE A ADDITIONAL COLUMN
    all_data_tables['Month'] = all_data_tables['Opened'].str[0:2]

    # CREATE A BASE TABLE
    all_data_tables.to_excel(Configure.output_folder + Configure.basic_join_file, index=False)

    read_data_join = pd.read_excel(Configure.output_folder + Configure.basic_join_file)

    # READING / CLEANING
    read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_at_sign)
    read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_letters)
    read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_some_special_characters)

    # COLUMN AND DATE TIME FORMATTER
    read_data_join['Opened'] = pd.to_datetime(read_data_join['Opened'], errors='coerce')
    read_data_join['Cust IA'] = pd.to_datetime(read_data_join['Cust IA'], errors='coerce')
    read_data_join.set_axis(Configure.output_columns, axis='columns', inplace=True)

    # CREATE A WORKING TABLE
    read_data_join.to_excel(Configure.output_folder + Configure.work_join_file, index=False)


if __name__ == '__main__':
    load_dbase()
    reportOne.company_colet_day_report_maker()
