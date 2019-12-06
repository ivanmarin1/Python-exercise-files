import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.style as mplstyle
import matplotlib.image as mpimg
from PIL import Image

# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="linear")
# plt.plot(x, x**2, label="quadratic")
# plt.plot(x, x**3, label="cubic")

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], [1, 8, 27, 64])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro", label = "dots")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")

# plt.legend()

# plt.show()

# def my_plotter(ax, data1, data2, param_dict):
#     """A helper function to make graph"""
#     out = ax.plot(data1, data2, **param_dict)
#     return out

# # use it as
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(1, 1)
# my_plotter(ax, data1, data2, {"marker" : "x"})

# plt.show()

# y = np.random.randn(100000)
# y[50000:] *= 2
# y[np.logspace(1,np.log10(50000), 400).astype(int)] = -1
# mpl.rcParams["path.simplify"] = True
# mplstyle.use(["dark_background", "ggplot", "fast"])

# mpl.rcParams["agg.path.chunksize"] = 0.0
# plt.plot(y)
# plt.show()

# mpl.rcParams["agg.path.chunksize"] = 1000
# plt.plot(y)
# plt.show()

# names = ["groupA", "groupB", "groupC"]
# values = [1, 100, 1000]
# plt.figure(figsize=(9, 3))
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle("Categorical Plotting")
# plt.show()

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# # plt.subplot(221)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# # plt.figure(2)
# # plt.subplot(222)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.text(1.5, .75, r"$ovo je pretop$")
# plt.show()

# img = mpimg.imread("../theEarth.png")
# # plt.figure()
# lum_img = img[:, :, 0]
# imgplot = plt.imshow(lum_img)
# plt.show()

img = Image.open("../theEarth.png")
img.thumbnail((64, 64), Image.ANTIALIAS)
imgplot = plt.imshow(img)
plt.show()