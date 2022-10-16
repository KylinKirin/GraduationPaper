import matplotlib.pyplot as plt
from AR_1 import c_1_list, c_0_list, phi_list
import numpy as np
import pandas as pd


def split_code(string):
    temp = string.split(",")
    res = ""
    for v in temp:
        res += "'"+v+"',"
    res = res.rstrip(",")
    return res


if __name__ == '__main__':
    a = "T1332,T1333,T1605,T1721,T1801,T1802,T1803,T1808,T1812,T1925,T1928,T1963,T2002,T2269,T2282,T2413,T2432,T2501," \
        "T2502,T2503,T2531,T2768,T2801,T2802,T2871,T2914,T3086,T3099,T3101,T3103,T3289,T3382,T3401,T3402,T3405,T3407," \
        "T3436,T3659,T3861,T3863,T4004,T4005,T4021,T4042,T4043,T4061,T4063,T4151,T4183,T4188,T4208,T4324,T4452,T4502," \
        "T4503,T4506,T4507,T4519,T4523,T4543,T4568,T4578,T4631,T4689,T4704,T4751,T4755,T4901,T4902,T4911,T5019,T5020," \
        "T5101,T5108,T5201,T5202,T5214,T5232,T5233,T5301,T5332,T5333,T5401,T5406,T5411,T5541,T5631,T5703,T5706,T5707," \
        "T5711,T5713,T5714,T5801,T5802,T5803,T6098,T6103,T6113,T6178,T6301,T6302,T6305,T6326,T6361,T6367,T6471,T6472," \
        "T6473,T6479,T6501,T6503,T6504,T6506,T6645,T6674,T6701,T6702,T6703,T6724,T6752,T6753,T6758,T6762,T6770,T6841," \
        "T6857,T6861,T6902,T6952,T6954,T6971,T6976,T6981,T6988,T7003,T7004,T7011,T7012,T7013,T7186,T7201,T7202,T7203," \
        "T7205,T7211,T7261,T7267,T7269,T7270,T7272,T7731,T7733,T7735,T7751,T7752,T7762,T7832,T7911,T7912,T7951,T7974," \
        "T8001,T8002,T8015,T8031,T8035,T8053,T8058,T8233,T8252,T8253,T8267,T8304,T8306,T8308,T8309,T8316,T8331,T8354," \
        "T8355,T8411,T8591,T8601,T8604,T8628,T8630,T8697,T8725,T8750,T8766,T8795,T8801,T8802,T8804,T8830,T9001,T9005," \
        "T9007,T9008,T9009,T9020,T9021,T9022,T9064,T9101,T9104,T9107,T9147,T9202,T9301,T9432,T9433,T9434,T9501,T9502," \
        "T9503,T9531,T9532,T9602,T9613,T9735,T9766,T9983,T9984 "
    # print(split_code(a))

    c_1_ave, sq_sum = np.average(c_1_list), 0
    for i in c_1_list:
        sq_sum += (i-c_1_ave)**2
    # se = np.sqrt(sq_sum/225)
    s = 2
    x = range(1, len(c_1_list)+1)
    # x = split_code(a)
    # plt.plot([c_1_ave+2*se for i in range(len(c_1_list))])
    # plt.plot([c_1_ave-2*se for i in range(len(c_1_list))])
    plt.scatter(x, c_0_list, s=s, marker="D", label="c_0")
    plt.scatter(x, c_1_list, s=s, marker="*", c="orange", label="c_1")
    plt.scatter(x, phi_list, s=s, marker="^", c="green", label="phi")
    plt.legend(loc="lower right")
    for i, c in enumerate([c_0_list, c_1_list, phi_list]):
        with open("ols_res1_"+str(i)+".csv", "wt") as fl:
            fl.write(pd.DataFrame(c).to_csv())

    plt.show()
