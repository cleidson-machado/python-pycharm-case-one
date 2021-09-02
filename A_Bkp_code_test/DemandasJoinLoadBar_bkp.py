import os
import pandas as pd
from tqdm import tqdm
import time
import PatternTableViewOne as reportOne
from Util import Cleaner as Clean
from Util import PlaceStorageStrings as Path

# files = [file for file in os.listdir(Path.input_folder)]

# How To Add A Progress Bar In Python With Just One Line - Python Tutorial
# LOAD BAR FROM HERE: https://youtu.be/FptVpIPhdpM

# Progress Bars With Tkinter - Python Tkinter GUI Tutorial #78
# https://youtu.be/Grbx15jRjQA

# Python Progress Bars in 9 minutes
# https://youtu.be/AntTxtOWyAI

files = tqdm([file for file in os.listdir(Path.input_folder)])

all_data_tables = pd.DataFrame()

for file in files:
    df = pd.read_excel(Path.input_folder + file)
    time.sleep(0.8)

    all_data_tables = pd.concat([all_data_tables, df])

# SELECTING ONLY THE Month FOR (( THE OPENED DAY COLLUM )) AND STORE IN A NEW COLLUM
all_data_tables['Month'] = all_data_tables['Opened'].str[0:2]

# CREATE A BASIC FIRST JOIN FILE
all_data_tables.to_excel(Path.output_folder + Path.basic_join_file, index=False)

# START CREATION OF A NEW FILE TO STORED ANOTHER PATTERN FILE...
read_data_join = pd.read_excel(Path.output_folder + Path.basic_join_file)

# CLEANER Opened COLUMN TASK 1
read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_at_sign)

# CLEANER Opened COLUMN TASK 2
read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_letters)

# CLEANER Opened COLUMN TASK 3
read_data_join['Opened'] = read_data_join['Opened'].apply(Clean.remove_some_special_characters)

# OK IT WORKS CONVERTING COLUMN Opened TO PANDAS DATETIME
read_data_join['Opened'] = pd.to_datetime(read_data_join['Opened'], errors='coerce')

# OK IT WORKS CONVERTING COLUMN Cust IA TO PANDAS DATETIME
read_data_join['Cust IA'] = pd.to_datetime(read_data_join['Cust IA'], errors='coerce')

# RENAME COLUMNS BEFORE SAVE THIS NEW FILE BELOW
read_data_join.set_axis(['SRMS',
                         'COLET_DAY',
                         'EMAIL_ACT',
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
                         'OPEN_TASK_MONTH'
                         ], axis='columns', inplace=True)

# SAVE AGAIN..
read_data_join.to_excel(Path.output_folder + Path.work_join_file, index=False)

# CREATE THE FIRST REPORT...
reportOne.company_colet_day_report_maker()
