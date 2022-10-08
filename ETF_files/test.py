from AR_1 import c_1_list, cap_t
from Equa.equ import etf_vector
import numpy as np
from matplotlib import pyplot as plt


def normalize(arr, mu0, sigma_2):
    arr = np.array(arr)
    return (arr-mu0)/np.sqrt(sigma_2)


if __name__ == '__main__':
    z_val = 1.28  # one-side 10%
    # z_val = 1.64  # one-side 5%
    count, codes_num = 0, 220
    fisher = np.sum(etf_vector)
    sigma = (1/fisher)/cap_t
    c_1_norm_list = normalize(c_1_list, 0, sigma)
    print(c_1_norm_list)
    fl_ver2_name = "../Equa/res_1656814116.6972976.txt"
    fl_ver1_name = "../Equa/res_1656815125.673747.txt"
    with open(fl_ver2_name, "rt") as fl:
        mle_c1 = list(map(float, fl.read().split(",")))
        mle_c1_norm = normalize(mle_c1, 0, sigma)
        c_1_norm_list = mle_c1_norm
    for v in c_1_norm_list:
        if v >= z_val:
            count += 1

    print("null hypo: ok: {0}, rejected: {1}".format(codes_num-count, count))
    plt.plot(c_1_norm_list)
    plt.plot([z_val for i in range(codes_num)])
    plt.show()
