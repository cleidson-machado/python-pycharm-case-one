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


# HERE REMOVE EVERYTHING
def remove_letters(s):
    return re.sub('[^0-9]+', '', s)


# HERE REMOVE JUST THE @ SYMBOL AND PUT A SPACE IR YOUR PLACE..
def remove_letters1(s):
    return re.sub('@', ' ', s)


# HERE REMOVE JUST THE leathers
def remove_letters2(s):
    return re.sub('[a-zA-Z]', '', s)


# HERE REMOVE JUST THE ALL SPECIAL CHARACTERS
def remove_letters3(s):
    return re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", s)


# HERE REMOVE JUST THE ALL SPECIAL CHARACTERS
def remove_letters4(s):
    return re.sub(r"[-()\"#;<>{}`+=~|.!?,]", "", s)


# CLEANER 1
read_data_join['Opened'] = read_data_join['Opened'].apply(remove_letters1)

# CLEANER 2
read_data_join['Opened'] = read_data_join['Opened'].apply(remove_letters2)

# CLEANER 2
read_data_join['Opened'] = read_data_join['Opened'].apply(remove_letters4)

# SAVE AGAIN..
read_data_join.to_excel("all_data_join_date_time.xlsx", index=False)

