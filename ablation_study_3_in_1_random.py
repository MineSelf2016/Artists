# %%
import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

plt.rc('legend',fontsize = 40)

# plt.legend(fontsize=40)

sns.set(rc={'figure.figsize':(10, 7)})

plt.rcParams['savefig.dpi'] = 300

sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})

fig, ax = plt.subplots(1, 1)

#%%

df = pd.DataFrame(columns = ["pos_conf", "test_acc"])

pseudo_label_threshold = ["0.0", "0.1", "0.2", "0.4", "0.6", "0.8", "0.99"]

test_acc = [0.692133, 0.692133, 0.692983, 0.698783, 0.711283, 0.704683, 0.695567]

test_std = [0.015118, 0.015118, 0.014637, 0.015136, 0.013597, 0.012354, 0.0117]

df["pseudo label threshold"] = pseudo_label_threshold
df["test_acc"] = test_acc
df["test_std"] = test_std

# %%
sns.lineplot(data = df, x = "pseudo label threshold", y = "test_acc", ax = ax, label = "Cora", marker = "o", markersize = 10)


lower_bound = [M_new - Sigma for M_new, Sigma in zip(test_acc, test_std)]
upper_bound = [M_new + Sigma for M_new, Sigma in zip(test_acc, test_std)]
ax.fill_between(pseudo_label_threshold, lower_bound, upper_bound, alpha=.3)


#%%
test_acc = [0.649033, 0.647917, 0.65005, 0.6688, 0.684083, 0.676533, 0.654217]

test_std = [0.013843, 0.014626, 0.014481, 0.016152, 0.016294, 0.015251, 0.017583]

df["pseudo label threshold"] = pseudo_label_threshold
df["test_acc"] = test_acc
df["test_std"] = test_std

sns.lineplot(data = df, x = "pseudo label threshold", y = "test_acc", ax = ax, label = "Citeseer", marker = "^", markersize = 12)


lower_bound = [M_new - Sigma for M_new, Sigma in zip(test_acc, test_std)]
upper_bound = [M_new + Sigma for M_new, Sigma in zip(test_acc, test_std)]
ax.fill_between(pseudo_label_threshold, lower_bound, upper_bound, alpha=.3)


#%%
test_acc = [0.734, 0.734, 0.734, 0.738633, 0.743767, 0.745717, 0.75766]

test_std = [0.0261, 0.0261, 0.0261, 0.026983, 0.024452, 0.024766, 0.023277]

df["pseudo label threshold"] = pseudo_label_threshold
df["test_acc"] = test_acc
df["test_std"] = test_std

sns.lineplot(data = df, x = "pseudo label threshold", y = "test_acc", ax = ax, label = "PubMed", marker = "v", markersize = 12)

# x = "pseudo label threshold",

lower_bound = [M_new - Sigma for M_new, Sigma in zip(test_acc, test_std)]
upper_bound = [M_new + Sigma for M_new, Sigma in zip(test_acc, test_std)]

ax.fill_between(pseudo_label_threshold, lower_bound, upper_bound, alpha=.3)


ax.set_xlabel(xlabel = "Pseudo Label Threshold", fontdict = {
    "fontsize": 20
})
ax.set_ylabel(ylabel = "Performance", fontdict = {
    "fontsize": 20
})

# ax.set(xlim=(-0.01, 1.05))
ax.set(ylim=(0.60, 0.82))

# ax.set_xticklabels(pseudo_label_threshold, fontsize=20)
ax.set_xticklabels(["0.0", "0.1", "0.2", "0.4", "0.6", "0.8", "0.99"], fontsize = 20)
ax.set_yticklabels([0.6, "", 0.65, "", 0.7, "", 0.75, "", 0.8], fontsize=20)
# plt.close(g1.fig)
# plt.close(g2.fig) 
# plt.show()
ax.legend(loc = "upper left")
plt.setp(ax.get_legend().get_texts(), fontsize = '18')


# set xticks style

# g.set_xticklabels(g.get_xticks(), size = 24)

# g.set_yticklabels(g.get_yticks(), size = 24)

# g.xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))

# g.yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))

# set xlabel style

# g.set_xlabel(xlabel = "pseudo label threshold", fontsize = 24)

# g.set_ylabel(ylabel = "Accuracy (%)", fontsize = 24)

# g.legend_.set_title(None)

# g.set_title("CiteSeer", fontname = "Times New Roman")

# g.set(ylim=(10, 90))

plt.tight_layout()

# plt.savefig('images/lines/node_coauthor_cs.pdf')

# plt.show()

fig


#%%
fig.savefig("images/ablation/random_threshold_3_in_1.pdf")


# %%
