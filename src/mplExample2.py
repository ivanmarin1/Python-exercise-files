import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {
    'Barton LLC': 109438.50,
    'Frami, Hills and Schmidt': 103569.59,
    'Fritsch, Russel and Anderson': 112214.71,
    'Jerde-Hilpert': 112591.43,
    'Keeling LLC': 100934.30,
    'Koepp Ltd': 103660.54,
    'Kulas Inc': 137351.96,
    'Trantow-Barrows': 123381.38,
    'White-Trantow': 135841.99,
    'Will LLC': 104437.60
}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

# print(group_data)
# print(group_names)
# print(group_mean)

# fig, ax = plt.subplots()
# ax.barh(group_names, group_data)
# ax = plt.show()
# print(plt.style.available)

def currency(x, pos):
    """The two args are the value and tick position"""
    if x >= 1e6:
        s = "${:1.1f}M".format(x*1e-6)
    else:
        s = "${:1.0f}K".format(x*1e-3)
    return s
formatter = FuncFormatter(currency)

plt.rcParams.update({"figure.autolayout": True})
plt.style.use("seaborn-darkgrid")
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment="right")
ax.set(xlim=[-10000, 140000], xlabel="Total Revenue", ylabel="Company", 
    title="Company Revenue")
ax.xaxis.set_major_formatter(formatter)
# Add a vertical line
ax.axvline(group_mean, ls="--", color="r")
# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")
# Now we'll move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
#fig.subplots_adjust(right=.1)
# print(fig.canvas.get_supported_filetypes())
fig.savefig("sales.png", transparent=False, dpi=80, bbox_inches="tight")
plt.show()