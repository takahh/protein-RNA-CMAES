##  Convergence Plot for Eval 3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 4 subsets, 5 folds, 20 plots


def plot(df, subn):
    figure = plt.figure()
    axes = figure.add_axes([0.14, 0.12, 0.83, 0.81])
    axes2 = figure.add_axes([0.4, 0.4, 0.52, 0.48])  # rested
    x = np.arange(len(df))
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_xlabel('Step', fontsize=15)
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'Evaluation 4, Subset {subnum}', fontsize=18)

    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")

    if subn == 1:
        axes2.set_xlim([4000, 8000])
        axes2.set_ylim([1, 1.1])
    elif subn == 2:
        axes2.set_ylim([1, 1.15])
        axes2.set_xlim([2500, 6500])
    elif subn == 3:
        axes2.set_xlim([12000, 16000])
        axes2.set_ylim([3.44, 3.54])
    elif subn == 4:
        axes2.set_ylim([12.43, 12.65])
        axes2.set_xlim([15000, 19500])

    axes2.set_xlabel('Step', fontsize=15)
    axes2.set_ylabel('Average Ranking', fontsize=14)
    axes2.tick_params(axis='both', which='major', labelsize=12)

    plt.savefig(f'{figpath}.png', dpi=400, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    path = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/"
    for subnum in range(4, 5):
        figpath = f"{path}progress_subset{subnum}_all.png"
        if subnum != 4:
            path1 = f"{path}cmaes_log_all_subset{subnum}_2021_02_23.txt"
            df = pd.read_csv(path1, sep=':', header=None)
        else:
            path1 = f"{path}cmaes_log_all_subset{subnum}_2021_02_23.txt"
            path2 = f"{path}cmaes_log_all_subset{subnum}_2021_02_24.txt"
            df1 = pd.read_csv(path1, sep=':', header=None)
            df2 = pd.read_csv(path2, sep=':', header=None)
            df = pd.concat([df1, df2])

        # df2 = pd.read_csv(path2, sep=':', header=None)
        # df3 = pd.read_csv(path3, sep=':', header=None)
        # df_t = pd.concat([df2, df1])
        # df = pd.concat([df3, df_t])

        plot(df, subnum)
