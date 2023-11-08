import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json

sns.set_style("darkgrid")

with open('experimental_results/p2_without_bf_small.json', 'r') as fr:
    data = json.load(fr)

n_list = list(data.keys())

algo_list = ['1', '2A', '2B', '3', '4', '5', '6A', '6B', '7', '8']
p_list = {'1': 1, '2A': 1, '2B': 1, '3': 1, '4': 1, '5': 2, '6A': 2, '6B': 2, '7': 2, '8': 2}

data_list = [[algo, int(n), data[n]["runtime"][algo], p_list[algo]] for n in n_list for algo in algo_list]

df = pd.DataFrame(data_list, columns=['Algo', 'n', 'Runtime', 'Problem'])

sns.lineplot(df.query("Problem == 2"), x='n', y='Runtime', hue='Algo', markers=True, style='Algo').set_title("Problem 2")
plt.show()