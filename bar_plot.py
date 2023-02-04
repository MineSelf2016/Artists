# %%
import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from  matplotlib.ticker import FuncFormatter

from matplotlib.patheffects import PathPatchEffect, SimpleLineShadow, Normal

plt.rcParams["font.family"] = "Times New Roman"

# plt.rc('legend',fontsize = 40)

# plt.legend(fontsize=40)

sns.set(rc={'figure.figsize':(10, 6)})

plt.rcParams['savefig.dpi'] = 300

sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})

# %%
df = pd.DataFrame(columns = ["Perturb Rate (%)", "Models", "Accuracy (%)"])

models = [["RRCL", "AGE", "LSCALE", "GRAIN", "ALG", "Random"] for i in range(4)]

pt_rates = [[5, 10, 15, 20] for i in range(6)]

pt_rates = np.array(pt_rates)

pt_rates = pt_rates.T

pt_rates = pt_rates.tolist()


accs = [

    [78.54, 73.82, 75.99, 76.14, 75.57, 73.13],

    [77.55, 72.8, 74.39, 74.96, 73.15, 70.86],

    [77.21, 71.22, 72.95, 73.01, 70.92, 69.59],

    [76.65, 69.71, 70.48, 69.9, 70.92, 67.96]

]

# accs = [

#     [71.71, 52.62, 67.43, 65.05, 66.95, 63.38],

#     [71.75, 51.2, 66.24, 56.72, 64.17, 62.04],

#     [70.65, 47.88, 64.54, 56.83, 63.22, 60.7],

#     [69.96, 47.89, 62.85, 58.95, 63.29, 59.81]

# ]

# accs = [

#     [79.26, 74.94, 73.01, 76.66, 74.33, 69.46],

#     [79.24, 74.1, 71.93, 75.52, 75.59, 67.98],

#     [77.44, 72.53, 70.95, 75.4, 63.29, 66.73],

#     [76.59, 71.15, 70.99, 75.05, 72.35, 65.81]

# ]

# accs = [

#     [85.60, 31.6, 69.32, 58.2, 64.43, 51.15],

#     [86.17, 38.9, 63.67, 41.92, 57.78, 53.96],

#     [85.83, 33.44, 59.05, 28.46, 51.86, 47.49],

#     [83.04, 31.6, 54.44 , 52.12, 47.61, 41.66]

# ]


# accs = [

#     [87.38, 79.28, 85.13, 86.86, 90.93, 85.62],

#     [86.80, 83.27, 84.95, 81.53, 89.37, 84.77],

#     [84.93, 80.95, 82.64, 78.70, 87.61, 83.44],

#     [84.2, 79.28, 80.86, 74.81, 86.32, 82.46]

# ]


for i in range(4):
    for  j in range(6):
        record = [pt_rates[i][j], models[i][j], accs[i][j]]
        df.loc[len(df.index)] = record

df

# %%

# g = sns.lineplot(data = df, x = "Perturb Rate (%)", y = "Accuracy (%)", hue="Models", style="Models", err_style="bars", markers = True)

# g = sns.lineplot(data = df, x = "Perturb Rate (%)", y = "Accuracy (%)", hue = "Models", markers = ["o", "v", "^", "<", ">", "+"], markersize = 15)

# g = sns.lineplot(data = df, x = "Perturb Rate (%)", y = "Accuracy (%)", hue = "Models", style = "Models", markers = True, markersize = 12, linestyle = ["solid", "solid", "solid", "solid", "solid", "solid"])

g = sns.barplot(data = df, x = "Perturb Rate (%)", y = "Accuracy (%)", hue = "Models", errorbar = "ci", estimator = "mean", path_effects = [SimpleLineShadow(shadow_color = "gray", linewidth = 1), Normal()])
# g = sns.catplot(data = df, x = "Perturb Rate (%)", y = "Accuracy (%)", hue = "Models",  kind = "bar", errorbar = "ci", legend_out = False)

# for i, _bar in enumerate(g.containers):
#     # print(i)
#     g.bar_label(i,)

# n = 0
# for i in g.containers:

#     for r in i:
#         r.set(shadow)

# g.containers[0][1]
# g.bar_label(g.containers[4], )

g.legend(loc='upper center', bbox_to_anchor = (0.5, 1.12), ncol = 6, fancybox = True, shadow = False)
plt.setp(g.get_legend().get_texts(), fontsize = '16')

# set xticks style
g.set_xticklabels([5, 10, 15, 20], size = 24)

g.set_yticklabels(g.get_yticks(), size = 24)

# g.xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))

g.yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))

# set xlabel style

g.set_xlabel(xlabel = "Perturb Ratio (%)", fontsize = 24)

g.set_ylabel(ylabel = "Accuracy (%)", fontsize = 24)

g.legend_.set_title(None)

g.set(ylim=(65, 80))

plt.tight_layout()

plt.savefig('images/bars/un_node_cora.pdf')

plt.show()

# %%

# https://wellsr.com/python/seaborn-line-plot-data-visualization/


#%%
