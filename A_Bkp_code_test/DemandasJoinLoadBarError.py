import os
import pandas as pd
from tqdm import tqdm
import time
from A_Bkp_code_test import PatternTableView001 as reportOne
from Util import Cleaner as Clean
from Util import PlaceStorageStrings as Path


def load_base_data():
    files = tqdm([file for file in os.listdir(Path.input_folder)])

    all_data_tables = pd.DataFrame()

    for file in files:
        df = pd.read_excel(Path.input_folder + file)
        time.sleep(0.8)

    all_data_tables = pd.concat([all_data_tables, df])

    all_data_tables['Month'] = all_data_tables['Opened'].str[0:2]

    all_data_tables.to_excel(Path.output_folder + Path.basic_join_file, index=False)

    read_data_join = pd.read_excel(Path.output_folder + Path.basic_join_file)

    read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_at_sign)

    read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_letters)

    read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_some_special_characters)

    read_data_join['Opened'] = pd.to_datetime(read_data_join['Opened'], errors='coerce')

    read_data_join['Cust IA'] = pd.to_datetime(read_data_join['Cust IA'], errors='coerce')

    read_data_join.set_axis(Path.output_columns, axis='columns', inplace=True)

    read_data_join.to_excel(Path.output_folder + Path.work_join_file, index=False)


if __name__ == '__main__':
    load_base_data()

    # using_base_data()

    reportOne.company_colet_day_report_maker()
