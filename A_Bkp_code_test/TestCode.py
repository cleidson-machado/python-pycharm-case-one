import os
import pandas as pd

full_path = 'C:\Users\PMachadC\OneDrive - Unisys\ACTION_CENTER_WORK\PROJECTS\01_02_03_DELL\03_DELL_EMC\00_TODO_Daily_Routine\EMC_REPORTS_CALL_by_email\new_way\python_stuff\ReadTabs01\Demand_Files\scsummaryreport_22_08_2021.CSV'

files = [file for file in os.listdir('.//Demand_Files')] # START REBUILD WITH A SIMPLE CODE...
all_months_data = pd.DataFrame()

# Demand_Files/scsummaryreport_22_08_2021.CSV
# C:\Users\PMachadC\OneDrive - Unisys\ACTION_CENTER_WORK\PROJECTS\01_02_03_DELL\03_DELL_EMC\00_TODO_Daily_Routine\EMC_REPORTS_CALL_by_email\new_way\python_stuff\ReadTabs01\Demand_Files\scsummaryreport_22_08_2021.CSV

for file in files:
    df = pd.read_csv("./Demand_Files/"+file)
    all_months_data = pd.concat([all_months_data, df])

arr = os.listdir('.//Demand_Files')
print(arr)