import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use("ggplot")
data = np.random.randn(50)
fig, ax = plt.subplots()
plt.plot(data)
plt.show()