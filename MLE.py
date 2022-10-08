import numpy as np
from Method_2 import list_h, list_h_0

print(len(list_h[0]))
for i, j in enumerate(list_h_0):
    list_h[i].insert(0, j)
print(len(list_h[0]))
for i in list_h:
    y = np.array(i)
