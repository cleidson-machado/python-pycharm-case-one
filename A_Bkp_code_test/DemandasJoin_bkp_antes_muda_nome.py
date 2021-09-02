import os
import pandas as pd
from Util import Cleaner as Clean

basic_join_file = "../all_data_join.xlsx"
work_join_file = "../all_data_work_file.xlsx"

files = [file for file in os.listdir('../Demand_Files')]

all_data_tables = pd.DataFrame()

for file in files:
    df = pd.read_excel(".//Demand_Files//" + file)

    all_data_tables = pd.concat([all_data_tables, df])

# SELECTING ONLY THE Month FOR (( THE OPENED DAY COLLUM )) AND STORE IN A NEW COLLUM
all_data_tables['Month'] = all_data_tables['Opened'].str[0:2]

all_data_tables.to_excel(basic_join_file, index=False)

# START CREATION OF A NEW FILE TO STORED ANOTHER PATTERN FILE...
read_data_join = pd.read_excel(basic_join_file)

# CLEANER Opened COLUMN 1
read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_at_sign)

# CLEANER Opened COLUMN 2
read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_letters)

# CLEANER Opened COLUMN 3
read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_some_special_characters)

# OK IT WORKS CONVERTING COLUMN OPENED TO PANDAS DATETIME
read_data_join['Opened'] = pd.to_datetime(read_data_join['Opened'], errors='coerce')

# OK IT WORKS CONVERTING COLUMN Cust IA TO PANDAS DATETIME
read_data_join['Cust IA'] = pd.to_datetime(read_data_join['Cust IA'], errors='coerce')

# RENAME COLUMNS BEFORE SAVE THIS NEW FILE BELOW
read_data_join.set_axis(['SRMS',
                         'COLET_DAY',
                         'IA_NUM',
                         'OPEN_TASK_DAY',
                         'TASK_NUM',
                         'COMPANY',
                         'LOCAL_UF',
                         'SYS_STATUS',
                         'SLA',
                         'PRIORITY',
                         'PRODUCT_CODE',
                         'SYS_SCHEDULE',
                         'COUNTRY',
                         'CHECK_STATUS',
                         'MONTH_NUM'
                         ], axis='columns', inplace=True)

# print(read_data_join.columns)

# DROP UNNECESSARY COLUMN TO SEND REPORT TO EMC.. working good!!!
# read_data_join.drop(['SRMS', 'COLET_DAY', 'IA_NUM', 'COUNTRY', 'MONTH_NUM'], axis=1, inplace=True)

# SAVE AGAIN..
read_data_join.to_excel(work_join_file, index=False)
