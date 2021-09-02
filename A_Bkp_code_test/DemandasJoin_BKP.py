import os
import pandas as pd

files = [file for file in os.listdir('.//Demand_Files')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_excel(".//Demand_Files//"+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv", index=False)

df2 = pd.read_csv("all_data.csv")

print(df2)
