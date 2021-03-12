import pandas as pd
from lambdata_mena2.helper_function import CleanFrame
from lambdata_mena2.helper_function import TimeSeriesSplit
from lambdata_mena2.helper_function import RandomSplit

df_oil = pd.read_csv("oil_consumption_per_cap.csv")
df_sp = pd.read_csv("^GSPC.csv")
# print(df_oil.head())
# print(df_oil.isna().sum().sum())
# print(isinstance(df_oil, pd.DataFrame))
# print(len(df_oil))

#print(df_sp.head())
#print(len(df_sp))

split = TimeSeriesSplit(df_sp, 0.8)
print(split.train_test_split()[0])
print(split.train_test_split()[1])
print(len(df_sp))

