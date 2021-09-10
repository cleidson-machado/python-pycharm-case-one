import pandas as pd
from Util import PlaceStorageStrings as Path

df = pd.read_excel(Path.output_folder + Path.report_002)

df_abc2 = df[~df["EMAIL_ACT"].isin(['RED'])]  # HERE IF I WANT FIND VALUES NOT MATH

df_abc = df[~df["EMAIL_ACT"].isin(['RED'])]  # HERE IF I WANT FIND VALUES NOT MATH

# OK! FIRST TEST!
# for row in df_abc.iterrows():
#     # print('um RED encontrado...')
#     df.loc[df["EMAIL_ACT"] == "RED", "EMAIL_ACT"] = "ALTERED"

# for row in df_abc.iterrows():
#     df.loc[df["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "RED"

for row in df_abc.iterrows():
    df.loc[df["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "RED"

df.to_excel(Path.output_folder + Path.report_003, index=False)

print(df["EMAIL_ACT"].value_counts())
