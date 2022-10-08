import pandas as pd
import numpy as np
from date_select import res as etf_date_list

data = pd.read_csv("/AR_MODEL/latent.csv", header=None)
data_h_0 = pd.read_csv("/AR_MODEL/latent_0.csv", header=None)
# print(data_h_0[1][0])
y_list = []
data = data.drop(columns=0)
for i in range(1, 221):
    y_list.append(data[i])
cap_t = len(y_list[0])


# print(data)
# print(y_list)
# print(y_list[0], "\n", pd.Series.shift(y_list[0], -1))


def newton(hessian, prime_vector, grad):
    return prime_vector - np.matmul(np.pinv(hessian), grad)


def ols(arr):
    y_1 = pd.Series(arr).shift(-1).fillna(0)
    phi = np.dot(arr - np.mean(arr), y_1 - np.mean(y_1)) / np.sum((y_1 - np.mean(y_1)) ** 2)
    c = np.mean(arr) - phi * np.mean(y_1)
    return c, phi


def etf(arr, n):
    box = []
    for p in range(n):
        box.append(0)
    for p in arr:
        box[-p] = 1
    return box


def m_ols(arr_y, arr_etf, fillna=0):
    arr_y = np.asarray(arr_y)
    arr_x = np.ones((len(arr_y), 3))
    arr_x[:, -1], arr_x[:, 1] = pd.Series(arr_y).shift(-1).fillna(fillna), etf(arr_etf, len(arr_y))
    # arr_x[:, 0] *= np.matmul(np.linalg.pinv(np.matmul(arr_x.T, arr_x)), np.matmul(arr_x.T, arr_y))[1]
    # print(arr_x[:, -1], arr_x[:, 1])
    # print(np.linalg.pinv(np.matmul(arr_x.T, arr_x)))
    # print(np.matmul(arr_x.T, arr_y))
    # arr_x[:, 0] *= 0.15
    # print(arr_x)
    result = np.matmul(np.linalg.pinv(np.matmul(arr_x.T, arr_x)), np.matmul(arr_x.T, arr_y))
    if len(result) > 0:
        return result.tolist()


# etf_list_0 = [x for x in range(0, 1218, 4)]
res_list, res_list_origin = [], []
data_0 = data_h_0[1]
for i, y in enumerate(y_list):
    res_list.append(m_ols(y, etf_date_list, data_0[i]))
    res_list_origin.append(ols(y))

print(res_list_origin, "\n", res_list)
c_0_list, c_1_list, phi_list = [], [], []
# print(type(res_list[0]))
for i in res_list:
    c_0_list.append(i[0])
    c_1_list.append(i[1])
    phi_list.append(i[2])
print(c_1_list)
plus_count, not_plus_count, zero_count = 0, 0, 0
for i in c_1_list:
    if i > 0:
        plus_count += 1
    elif i < 0:
        not_plus_count += 1
    else:
        zero_count += 1

print("plus:{0} not +:{1}  Zero:{2}".format(plus_count, not_plus_count, zero_count))

if __name__ == '__main__':
    c_0_prime, c_1_prime, phi_prime = 1, 0, 0.9
    etf_vector = [0 for i in range(cap_t)]
    for i in etf_date_list:
        etf_vector[i - 1] = 1
    print(etf_vector)
    # gradient_vector = np.array([sum(y_list[0].tolist()) - cap_t * (1 - phi_prime) * c_0_prime
    #                             - c_1_prime * sum(etf_vector)
    #                             - phi_prime * sum(pd.Series(y_list[0]).shift(-1).fillna(data_h_0[1][0]).tolist()),
    #                             sum(np.array(y_list[0].tolist()) * etf_vector) - sum(etf_vector) * c_0_prime * (
    #                                     1 - phi_prime)
    #                             - c_1_prime * sum(etf_vector)
    #                             - phi_prime * sum(etf_vector
    #                                               * np.array(pd.Series(y_list[0]).shift(-1).fillna(data_h_0[1][0]).
    #                                                          tolist())),
    #                             sum(np.array(y_list[0].tolist())
    #                                 * np.array(pd.Series(y_list[0]).shift(-1).fillna(data_h_0[1][0]).to_list()))
    #                             - c_0_prime * sum(y_list[0].tolist())
    #                             - sum(np.array((pd.Series((y_list[0]).shift(-1).fillna(data_h_0[1][0])).tolist()) -
    #                                            np.array([c_0_prime for i in range(len(etf_vector))]))
    #                                   * c_0_prime * (1 - phi_prime)
    #                                   + c_1_prime for i in range(len(etf_vector))
    #                                   * np.asarray(etf_vector)
    #                                   + phi_prime
    #                                   * np.array(pd.Series(y_list[0]).shift(-1).fillna(data_h_0[1][0]).tolist()))],
    #                            dtype=object)
    # # print(gradient_vector[1])
    # print(len(gradient_vector))
    # print(gradient_vector)
