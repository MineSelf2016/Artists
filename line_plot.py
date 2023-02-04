# %%
import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from  matplotlib.ticker import FuncFormatter

plt.rcParams["font.family"] = "Times New Roman"

plt.rc('legend',fontsize = 40)

# plt.legend(fontsize=40)

sns.set(rc={'figure.figsize':(10, 6)})

plt.rcParams['savefig.dpi'] = 300

sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})

# %%
df = pd.DataFrame(columns = ["Perturb Rate ()", "Models", "Accuracy ()"])

models = [["RRCL", "AGE", "LSCALE", "GRAIN", "ALG", "Random"] for i in range(6)]

pt_rates = [[0, 20, 40, 60, 80, 100] for i in range(6)]

pt_rates = np.array(pt_rates)

pt_rates = pt_rates.T

pt_rates = pt_rates.tolist()

# accs = [

#     [78.56, 75.62, 77.65, 77.71, 77.68, 75.66],

#     [76.78, 70.32, 71.21, 74.60, 71.42, 68.67],

#     [74.97, 65.64, 64.92, 67.07, 65.35, 62.25],

#     [73.32, 60.20, 58.42, 59.37, 60.34, 56.44],

#     [71.86, 55.96, 53.22, 56.01, 55.46, 52.22],

#     [70.40, 52.74, 50.31, 54.02, 52.1, 47.4]

# ]

# accs = [

# [72.3, 68.21, 68.79, 67.16, 69.44, 64.36],

# [71.1, 61.74, 59.64, 62.4, 63.74, 57.8],

# [70.66, 56.97, 54.48, 57.9, 57.85, 52.84],

# [70.05, 52.62, 50.4, 51.13, 53.19, 47.99],

# [68.96, 49.43, 47.03, 51.86, 49.25, 44.31],

# [67.65, 45.95, 44.5, 49.7, 47.54, 41.35]

# ]

# accs = [

#     [79.34, 76.52, 78.39, 78.27, 78.66, 71.02],

#     [77.45, 66.99, 65.72, 70.03, 69.3, 61.4],

#     [76.76, 62.31, 60.47, 63.25, 64.59, 56.3],

#     [75.45, 58.91, 57.04, 59.01, 59.94, 52.97],

#     [75.76, 56.24, 54.3, 57.26, 58.12, 51.06],

#     [75.76, 54.91, 53.48, 56.81, 56.81, 50.13]

# ]

accs = [
    [85.47, 57.71, 76.28, 68.06, 69.19, 57.88],
    
    [83.35, 28.16, 53.89, 36.52, 49.91, 37.42],
    
    [80.87, 29.73, 35.81, 18.55, 35.73, 30.67],
    
    [78.55, 27.44, 31.72, 17.28, 30.52, 33.54],
    
    [76.99, 27.00, 26.49, 11.56 , 25.2, 29.89],
    
    [75.68, 26.9, 25.56, 13.06, 23.71, 29.01]
]


# accs = [
#     [87.6, 91.19, 90.26, 89.67, 89.66, 86.28],

#     [84.53, 82.61, 79.65, 76.65, 86.21, 80.48],

#     [83.35, 77.11, 71.79, 77.37, 81.02, 77.37],

#     [80.54, 69.96, 62.33, 72.11, 75.35, 68.46],

#     [79.36, 63.97, 51.15, 64.79, 63.63, 68.35],

#     [78.44, 60.38, 43.89, 35.12, 51.03, 62.8]
# ]


for i in range(6):
    for  j in range(6):
        record = [pt_rates[i][j], models[i][j], accs[i][j]]
        df.loc[len(df.index)] = record

# %%
g = sns.lineplot(data = df, x = "Perturb Rate ()", y = "Accuracy ()", hue = "Models", style = "Models", markers = True, markersize = 12)

lines = g.get_lines()

for line in lines:
    line.set_linestyle("solid")

lines[0].set_markersize(10)

glines = g.legend_.get_lines()

for line in glines:
    line.set_linestyle("solid")

# set legend font size

plt.setp(g.get_legend().get_texts(), fontsize = '20')

# set xticks style

g.set_xticklabels(g.get_xticks(), size = 24)

g.set_yticklabels(g.get_yticks(), size = 24)

g.xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))

g.yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))

# set xlabel style

g.set_xlabel(xlabel = "Perturb Ratio (%)", fontsize = 24)

g.set_ylabel(ylabel = "Accuracy (%)", fontsize = 24)

g.legend_.set_title(None)

# g.set_title("CiteSeer", fontname = "Times New Roman")

g.set(ylim=(10, 90))

plt.tight_layout()

plt.savefig('images/lines/node_coauthor_cs.pdf')

plt.show()

# %%




# https://wellsr.com/python/seaborn-line-plot-data-visualization/