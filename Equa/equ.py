import time

from scipy import optimize as opt
# from scipy import integrate
import numpy as np
from AR_1 import y_list, data_0, etf_date_list
from matplotlib import pyplot as plt

sigma_squ = [0]


def fuc1(x):
    return x


def fuc2(x, y):
    return x**2+2*y**2

#
# def myequa(x_list):  # Ver.1
#     global sigma_squ
#     c_0, c_1, phi = x_list
#     sum_0, sum_1, sum_2, sum_3 = 0, 0, 0, 0
#     y_temp = y_list[count].to_list()
#     y_0_temp = data_0[count]
#     cap_t = len(y_temp) + 1
#     for i, j in enumerate(y_temp):
#         # print(i, j)
#         if i > 0:
#             temp = j-c_0-c_1*etf_vector[i-1]-phi*y_temp[i-1]
#             sum_0 += temp**2
#             sum_1 += temp
#             sum_2 += etf_vector[i-1]*temp
#             sum_3 += y_temp[i-1]*temp
#     else:
#         sigma_squre = (1 / cap_t) * ((1 - phi ** 2) * (y_0_temp-c_0/(1-phi))**2 + sum_0)
#         # print(sigma_squre)
#         sigma_squ[-1] = sigma_squre
#     return [(1+phi)*(y_0_temp-c_0/(1-phi)) + sum_1,
#             sum_2, -phi*sigma_squre/(1-phi**2) + c_0*((1-phi**2)/(1-phi)**2)*(y_0_temp-c_0/(1-phi)) + sum_3]


def myequa(x_list):  # Ver.2
    global sigma_squ
    c_0, c_1, phi = x_list
    sum_0, sum_1, sum_2, sum_3 = 0, 0, 0, 0
    y_temp = y_list[count].to_list()
    y_0_temp = data_0[count]
    cap_t = len(y_temp) + 1
    for i, j in enumerate(y_temp):
        # print(i, j)
        if i > 0:
            temp = j-c_0*(1-phi)-c_1*etf_vector[i-1]-phi*y_temp[i-1]
            sum_0 += temp**2
            sum_1 += temp*(1-phi)
            sum_2 += etf_vector[i-1]*temp
            sum_3 += (y_temp[i-1]-c_0)*temp
    else:
        sigma_squre = (1 / cap_t) * ((1 - phi ** 2) * (y_0_temp-c_0)**2 + sum_0)
        # print(sigma_squre)
        sigma_squ[-1] = sigma_squre
    return [(1-phi**2)*(y_0_temp-c_0) + sum_1,
            sum_2, -phi*sigma_squre/(1-phi**2) + phi*(y_0_temp-c_0)**2 + (1+phi)*c_1*(y_0_temp-c_0)/(1-phi) + sum_3]


def etf(arr1, n):
    box = []
    for p in range(n):
        box.append(0)
    for p in arr1:
        box[p] = 1
    return box


def y_1(x, theta):
    global sigma_squ
    global etf_vector
    sigma = sigma_squ[theta[1]]
    phi, c_0 = theta[0][2], theta[0][0]
    expo = np.exp(-((1-phi**2)*(x-c_0/(1-phi))**2) / (2*sigma))
    # return np.sqrt((1-phi**2)/(2*np.pi*sigma))*expo*np.sum(etf_vector)
    return np.sqrt((1 - phi ** 2) / (2 * np.pi * sigma)) * expo


etf_vector = etf(etf_date_list, len(y_list[0].to_list()))


if __name__ == '__main__':
    code_num = 220
    count, c1_diff_sum, c1_diff_ave, diff = 0, 0, 100, 0
    print("*"*150)
    res = []
    for m in range(code_num):
        fai, val_1, val_2, val_3 = 1.0, 1, 0.01, 0
        # fai, val_1, val_2, val_3 = 1.0, 1, 0.01, 0.9
        sol = None
        # while fai >= 1.0 or fai <= -1.0 or c1_diff_ave < diff:
        while fai >= 1.0 or fai <= -1.0:
            arr = np.array([val_1, val_2, val_3])
            # print(arr)
            sol = opt.fsolve(myequa, arr)
            fai = sol[2]
            if len(res) > 0:
                diff = np.abs(sol[1] - res[-1][1])
                c1_diff_sum += diff
                c1_diff_ave = c1_diff_sum/count
            val_1 += 0.5
            # val_1 *= -1
            val_2 += 0.05
            val_2 *= -1

            val_3 += 0.1
            val_3 *= -1
            if val_3 >= 0.01:
                val_3 = 0.8
        res.append(sol)
        sigma_squ.append(None)
        count += 1
        print("{0}/{1} Result: ".format(count, code_num), sol)

    plus_count, minus_count = 0, 0
    c_1_res = []
    for m in res:
        c_1_res.append(m[1])
        if m[1] < 0:
            minus_count += 1
        elif m[1] > 0:
            plus_count += 1
    else:
        with open("res_{0}.txt".format(str(time.time())), "wt") as fl:
            fl.write(str(c_1_res)[1:-1])
    print("Sgn_Count: + {0} - {1}".format(plus_count, minus_count))

    a = []
    # for k, h in enumerate(res):
    #     a.append(integrate.quad(y_1, -np.inf, np.inf, args=[h, k]))
    print(sigma_squ)
    print(a)
    # plt.plot(res)
    res = np.array(res).T
    s = 2
    print(res)
    plt.scatter(range(1, code_num+1), res[0], s=s, marker="D", label="c_0")
    plt.scatter(range(1, code_num+1), res[1], s=s, marker="*", label="c_1")
    plt.scatter(range(1, code_num+1), res[2], s=s, marker="^", label="phi")
    plt.legend()

    plt.show()
