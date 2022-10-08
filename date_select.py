import pandas as pd
from ETF import date_list as etf_date_list

data_0 = pd.read_csv("../FqReport_0.csv", header=None, skiprows=2)
data_1 = pd.read_csv("../FqReport_1.csv", header=None, skiprows=2)
data_2 = pd.read_csv("../FqReport1_nikkeiaverage.csv", header=None, skiprows=2)
date_list, res = [], []
# print(data[0])
for i in data_0[0].tolist():
    i = str(i).replace("/", "")
    date_list.append(int(i))
for i in data_1[0].tolist():
    i = str(i).replace("/", "")
    date_list.append(int(i))
for i in data_2[0].tolist():
    i = str(i).replace("/", "")
    date_list.append(int(i))

for j in etf_date_list:
    if j in date_list:
        res.append(date_list.index(j))

print(res)
for i, j in enumerate(res):
    res[i] = j+1
# res.pop()
print(len(etf_date_list), len(date_list))
print(etf_date_list, "\n", date_list)
