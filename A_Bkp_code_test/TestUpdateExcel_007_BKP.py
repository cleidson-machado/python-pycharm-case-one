import pandas as pd
from Util import PlaceStorageStrings as Path
import numpy as np

df = pd.read_excel(Path.output_folder + Path.report_002)

# df_abc = df[df["EMAIL_ACT"] == "RED"] # OPTION VERY SIMPLE TO FIND SOMETHING USE BELOW IF WANT NOT MATH

df_abc = df[~df["EMAIL_ACT"].isin(['RED'])]  # HERE IF I WANT FIND VALUES NOT MATH
#
# for row in df_abc.iterrows():
#     print('Passei aqui!')
#
# print(df_abc['EMAIL_ACT'].value_counts())

df["EMAIL_ACT"] = np.where(df["EMAIL_ACT"] == "43200131", 'EMPTY_VALUE', df["EMAIL_ACT"])

# ERROR..!!
# df["EMAIL_ACT"] = np.where(df_abc, 'EMPTY_VALUE', df["EMAIL_ACT"])

print(df["EMAIL_ACT"].value_counts())

# df.to_excel(Path.output_folder + Path.report_003, index=False)

# UTIL HERE
# https://stackoverflow.com/questions/51800122/using-openpyxl-to-find-rows-that-contain-cell-with-specific-value
