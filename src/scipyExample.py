import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def add(a, b):
    return a+b

d = [1, 2, 3, 4]
e = [5, 6, 7, 8]

c = [d[i] + e[i] for i in range(len(d))]
print(c)
