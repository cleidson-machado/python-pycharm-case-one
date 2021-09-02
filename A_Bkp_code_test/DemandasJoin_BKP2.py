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


def remove_letters(s):
    return re.sub('[^0-9]+', '', s)


# CLEANER 1
read_data_join['Opened'] = read_data_join['Opened'].apply(remove_letters)

time_column = read_data_join['Opened']

special_character = "!@#$)("

for char in special_character:
    time_column = time_column.replace(char, "")

# CLEANER 2 DON'T WORK GOOD
# read_data_join['Opened'] = read_data_join.Opened.str.replace(r"[a-zA-Z]", '')

# READ JUST DATE TIME COLLUM
# day_time_collum = read_data_join['Opened']

# SAVE AGAIN..
read_data_join.to_excel("all_data_join_date_time.xlsx", index=False)

# print(day_time_collum)

# SAVE TO CSV
# all_data_tables.to_csv("all_data.csv", index=False)


# TESTE
# all_data = pd.read_csv('all_data.csv')

# TESTE
# clean_the_day = all_data['Opened']

# TESTE
# cleaner = clean_the_day.replace('[A-Za-z]', '', regex=True)

# print(clean_the_day)


# all_data_tables["Opened"].replace({"(BTZ)": ""})
# clean_the_day = all_data['Opened']

# clean_the_day.replace("(BTZ)", "X")

# print(all_data.tail())
# print(clean_the_day.tail())
# print(clean_the_day.replace("(BTZ)", "X"))


# print(all_months_data.tail())
# print(all_months_data['Opened'])

# CONVERTING DATE TIME ERROR 1.....
# all_months_data['Month2'] = pd.to_datetime(all_months_data['Opened'])

# CONVERTING DATE TIME ERROR 1.....
# all_months_data['Month2'] = pd.to_datetime(all_months_data['Opened'])

# CONVERTING DATE TIME ERROR 3..... remove btz
# all_months_data['Opened'] = all_months_data['Opened'].str.replace(r'(BTZ)', '')

# all_months_data["Opened"].replace({"(BTZ)": ""})

# df2 = pd.read_csv("all_data.csv")

# print(df2)