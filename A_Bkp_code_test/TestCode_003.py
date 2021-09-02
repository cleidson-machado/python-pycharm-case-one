import pandas as pd

# TEST TO FIND A WAY TO SHOW THE DATE COLUMNS IN A
# SPECIFIC DATE TIME FORMAT.. USING PANDAS YET

df = pd.read_excel("all_data_join_date_time.xlsx")

column_a = df["Opened"].dt.strftime("%m/%d/%Y")

column_b = df["Cust IA"].dt.strftime("%m/%d/%Y")

print(column_a)
print("----------------------")
print(column_b)

