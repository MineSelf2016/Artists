# %%
import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from  matplotlib.ticker import FuncFormatter

plt.rcParams["font.family"] = "Times New Roman"

plt.rc('legend',fontsize = 40)

# plt.legend(fontsize=40)

sns.set(rc={'figure.figsize':(30, 7)})

plt.rcParams['savefig.dpi'] = 300

sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})

fig, ax = plt.subplots(1, 3)

#%%
df = pd.DataFrame()

# pseudo_label_threshold = [0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99]

pseudo_label_threshold = ["0.0", "0.1", "0.2", "0.4", "0.6", "0.8", "0.99"]

test_acc = [0.692133, 0.692133, 0.692983, 0.698783, 0.711283, 0.704683, 0.695567]

test_std = [0.015118, 0.015118, 0.014637, 0.015136, 0.013597, 0.012354, 0.0117]

df["pseudo label threshold"] = pseudo_label_threshold
df["test_acc"] = test_acc
df["test_std"] = test_std

# %%
sns.lineplot(data = df, x = "pseudo label threshold", y = "test_acc", label = "Cora", marker = "o", ax = ax[0], markersize = 15, linewidth = 4)


lower_bound = [M_new - Sigma for M_new, Sigma in zip(test_acc, test_std)]
upper_bound = [M_new + Sigma for M_new, Sigma in zip(test_acc, test_std)]
# ax[0].fill_between(pseudo_label_threshold, lower_bound, upper_bound, alpha=.3)


#%%
test_acc = [0.649033, 0.647917, 0.65005, 0.6688, 0.684083, 0.676533, 0.654217]

test_std = [0.013843, 0.014626, 0.014481, 0.016152, 0.016294, 0.015251, 0.017583]

df["pseudo label threshold"] = pseudo_label_threshold
df["test_acc"] = test_acc
df["test_std"] = test_std

sns.lineplot(data = df, x = "pseudo label threshold", y = "test_acc", label = "Citeseer", marker = "o", ax = ax[1], markersize = 15, linewidth = 4)

lower_bound = [M_new - Sigma for M_new, Sigma in zip(test_acc, test_std)]
upper_bound = [M_new + Sigma for M_new, Sigma in zip(test_acc, test_std)]
# ax[1].fill_between(pseudo_label_threshold, lower_bound, upper_bound, alpha=.3)


#%%
test_acc = [0.734, 0.734, 0.734, 0.738633, 0.743767, 0.745717, 0.75766]

test_std = [0.0261, 0.0261, 0.0261, 0.026983, 0.024452, 0.024766, 0.023277]

df["pseudo label threshold"] = pseudo_label_threshold
df["test_acc"] = test_acc
df["test_std"] = test_std

sns.lineplot(data = df, x = "pseudo label threshold", y = "test_acc", label = "PubMed", marker = "o", ax = ax[2], markersize = 15, linewidth = 4)

# x = "pseudo label threshold",

lower_bound = [M_new - Sigma for M_new, Sigma in zip(test_acc, test_std)]
upper_bound = [M_new + Sigma for M_new, Sigma in zip(test_acc, test_std)]

# ax[2].fill_between(pseudo_label_threshold, lower_bound, upper_bound, alpha=.3)




# ax.set(xlim=(-0.01, 1.05))
# ax.set(ylim=(0.60, 0.82))

for ax_i in ax:

    ax_i.get_legend().remove()
    
    ax[0].set_xlabel(xlabel = "Pseudo Label Threshold (Cora)", fontdict = {
        "fontsize": 20
    })
    ax[1].set_xlabel(xlabel = "Pseudo Label Threshold (CiteSeer)", fontdict = {
        "fontsize": 20
    })
    ax[2].set_xlabel(xlabel = "Pseudo Label Threshold (PubMed)", fontdict = {
        "fontsize": 20
    })

    ax_i.set_ylabel(ylabel = "Performance", fontdict = {
        "fontsize": 20
    })

    # ax_i.set_xticklabels(pseudo_label_threshold, fontsize=20)
    # tmp = ax_i.get_xticks().round(2)
    # tmp[-1] = 0.99
    # tmp[-2] = 0.99
    # ax_i.set_xticklabels(ax_i.get_xticks().round(3), fontsize=20)
    ax_i.set_xticklabels(["0.0", "0.1", "0.2", "0.4", "0.6", "0.8", "0.99"], fontsize = 20)
    ax_i.set_yticklabels(ax_i.get_yticks().round(3), size = 20)
    # ax.set_yticklabels([0.6, "", 0.65, "", 0.7, "", 0.75, "", 0.8], fontsize=20)

# ax.legend(loc = "upper left")
# plt.setp(ax.get_legend().get_texts(), fontsize = '18')
plt.tight_layout()

# plt.savefig('images/lines/node_coauthor_cs.pdf')

# plt.show()

fig

#%%
fig.savefig('images/ablation/random_threshold.pdf')


#%%


