import pandas as pd

temp, amount_list, date_list = [], [], []
data = pd.read_csv("/AR_MODEL/ETF_files/ETF_auto.csv", header=None)
# print(data[0], data[1])
for i in data[0].tolist():
    format_date = []
    format_date = str(i).split("/")
    for j in range(1, 3):
        if int(format_date[j]) < 10:
            format_date[j] = "0" + format_date[j]
    temp.append(int(format_date[0] + format_date[1] + format_date[2]))

for p, q in enumerate(data[1].tolist()):
    if pd.isnull(q):
        temp.pop(p)
        temp.insert(p, 0)
    else:
        amount_list.append(int(q))

for date in temp:
    if date != 0:
        date_list.append(date)

# print(date_list, amount_list)

