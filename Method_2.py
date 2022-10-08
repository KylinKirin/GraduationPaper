import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from date_select import res as etf_date_list

data_h = pd.read_csv("latent.csv", header=None)
data_h_0 = pd.read_csv("latent_0.csv", header=None)
list_h_0 = list(map(float, data_h_0[1].tolist()))
list_h, volit, returns, res = [], [], [], []


def etf_vector(etflist, length):
    n = length
    box = []
    for r in range(n):
        if r in etflist:
            box.append(10)
            continue
        box.append(0)
    return box


def half(x):
    return 0.5*x


for i in range(1, 221):
    list_h.append([])
    list_h[i-1] = list(map(np.exp, map(half, map(float, data_h[i].to_list()))))
# print(list_h[0])
if __name__ == '__main__':
    for i in range(1, 221):
        volit.append([])
        volit[i - 1].append(np.exp(list_h_0[i - 1]) / 2)
        for j in list_h[i - 1]:
            volit[i - 1].append(j)

    # print(volit[0], "\n", len(volit[0]))
    for p, q in enumerate(volit):
        returns.append([])
        for j in range(len(q[1:])):
            temp = np.log(np.asarray(q[j])) - np.log(np.asarray(q[j - 1]))
            returns[p].append(temp)

    # print(returns[:50])
    for i in range(1, 221):
        res.append([])
        res[i - 1] = np.abs(np.array(returns[i - 1])) / np.array(volit[i - 1][1:])
    for i in range(1):
        # plt.plot(res[i][2:62])

        plt.scatter([x for x in range(1, len(res[i]) + 1)], res[i], s=9)
    # print(len(res[0]), etf_vector(etf_date_list, len(res[0])))
    plt.bar([x for x in range(1, len(res[0]) + 1)], etf_vector(etf_date_list, len(res[0])))
    plt.title("Return/Volitility")

    plt.show()
