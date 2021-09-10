from datetime import datetime
import pandas as pd
import numpy as np

date_format = "%m/%d/%Y"

# dti = pd.date_range("2021-09-01", periods=3, freq="D")

idx = pd.date_range("2021-09-05", periods=3, freq="D")

# ts = pd.Series(range(len(idx)), index=idx)

ts = pd.Series(pd.date_range("2021-09-05", freq="D", periods=3), dtype=np.dtype("O"))

print(ts)

# a = datetime.strptime(ts, date_format)

# print(dti)

# print(a)
