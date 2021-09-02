import os
import pandas as pd
import re

files = [file for file in os.listdir('.//Demand_Files')]

all_data_tables = pd.DataFrame()

for file in files:
    df = pd.read_excel(".//Demand_Files//" + file)

    all_data_tables = pd.concat([all_data_tables, df])

# SELECTING ONLY THE Month FOR (( THE OPENED DAY COLLUM )) AND STORE IN A NEW COLLUM
all_data_tables['Month'] = all_data_tables['Opened'].str[0:2]

all_data_tables.to_excel("all_data_join.xlsx", index=False)

read_data_join = pd.read_excel("all_data_join.xlsx")


# HERE REMOVE JUST THE @ SYMBOL AND PUT A SPACE IR YOUR PLACE..
def remove_at_sign(s):
    return re.sub('@', ' ', s)


# HERE REMOVE JUST THE leathers
def remove_letters(s):
    return re.sub('[a-zA-Z]', '', s)


# HERE REMOVE JUST THE SOME SPECIAL CHARACTERS
def remove_some_special_characters(s):
    return re.sub(r"[-()\"#;<>{}`+=~|.!?,]", "", s)


# CLEANER Opened COLUMN 1
read_data_join['Opened'] = read_data_join['Opened'].apply(remove_at_sign)

# CLEANER Opened COLUMN 2
read_data_join['Opened'] = read_data_join['Opened'].apply(remove_letters)

# CLEANER Opened COLUMN 3
read_data_join['Opened'] = read_data_join['Opened'].apply(remove_some_special_characters)

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
                         'UF_LOCAL',
                         'SYS_STATUS',
                         'SLA',
                         'PRIORITY',
                         'PRODUCT_CODE',
                         'SYS_SCHEDULE',
                         'COUNTRY',
                         'CHECK_STATUS',
                         'MONTH_NUM'
                         ], axis='columns', inplace=True)

print(read_data_join.columns)

# SAVE AGAIN..
read_data_join.to_excel("all_data_join_date_time.xlsx", index=False)
