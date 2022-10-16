import numpy

from AR_1 import c_0_list, c_1_list, phi_list
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # diff_c_0, diff_c_1, diff_phi = 0, 0, 0
    fl_ver1_name_c0 = "../Equa/mle_res_v1_0.csv"
    fl_ver1_name_c1 = "../Equa/mle_res_v1_1.csv"
    fl_ver1_name_phi = "../Equa/mle_res_v1_2.csv"

    mle_c_0 = pd.read_csv(fl_ver1_name_c0, index_col=0).values
    mle_c_1 = pd.read_csv(fl_ver1_name_c1, index_col=0).values
    mle_phi = pd.read_csv(fl_ver1_name_phi, index_col=0).values
    # print("mle c0", mle_c_0)
    diff_c_0 = np.array(c_0_list) - np.array(mle_c_0)
    diff_c_1 = np.array(c_1_list) - np.array(mle_c_1)
    diff_phi = np.array(phi_list) - np.array(mle_phi)
    # print(np.array(mle_phi))
    diff_c_0 = np.abs(diff_c_0)
    diff_c_1 = np.abs(diff_c_1)
    diff_phi = np.abs(diff_phi)
    s = 2
    x_range = range(1, len(diff_phi)+1)
    print(len(mle_phi), len(phi_list), len(x_range), len(diff_phi))
    plt.scatter(x_range, diff_c_0[0], s=s, marker="D", label="c_0")
    plt.scatter(x_range, diff_c_1[0], s=s, marker="*", c="orange", label="c_1")
    plt.scatter(x_range, diff_phi[0], s=s, marker="^", c="green", label="phi")
    print("C_0: ", np.sum(np.square(diff_c_0[0])), "C_1: ", np.sum(np.square(diff_c_1[0])),
          "PHI: ", np.sum(np.square(diff_phi[0])))
    plt.legend(loc="upper right")
    plt.title("Plot of the absolute difference between the estimates of OLS and MLE")
    plt.show()
