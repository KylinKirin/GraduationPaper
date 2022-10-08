from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fl = pd.read_csv("parameters.csv", header=None).T[1:]
mu_list, phi_list, sigma_list = fl[0].to_list(), fl[1].to_list(), fl[2].to_list()
paras = [mu_list, phi_list, sigma_list]
print(fl)
phi_sigma = np.array(sigma_list)*np.array(phi_list)
plt.plot(phi_sigma)
# plt.plot(sigma_list)
plt.show()
print(max(phi_list))
print(np.average(phi_sigma), np.average(phi_list))
