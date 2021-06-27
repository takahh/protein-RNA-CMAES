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
    axes.set_title(f'Evaluation 4, Subset {subnum}, Fold {foldnum}', fontsize=18)

    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")

    axes2.set_xlim([3000, 8000])
    if subn == 1:
        axes2.set_ylim([1, 1.1])
    elif subn == 2:
        axes2.set_ylim([1, 1.2])
    elif subn == 3:
        # axes2.set_xlim([0, 17000])
        # axes2.set_ylim([1.4, 2.5])
        axes2.set_xlim([18000, 20000])
        axes2.set_ylim([1.4, 1.7])
    elif subn == 4:
        if foldnum == 0:
            axes2.set_ylim([5.61, 5.65])
            axes2.set_xlim([20000, 27000])
        elif foldnum == 1:
            axes2.set_ylim([4.45, 4.49])
            axes2.set_xlim([20000, 22000])
        elif foldnum == 2:
            axes2.set_ylim([5.37, 5.41])
            axes2.set_xlim([20000, 24000])
        elif foldnum == 3:
            axes2.set_ylim([5.41, 5.46])
            axes2.set_xlim([19000, 23000])
        else:
            axes2.set_ylim([5.4, 5.45])
            axes2.set_xlim([27000, 31000])
        # axes2.set_ylim([1.5, 2.3])
        # axes2.set_xlim([14000, 20000])

    axes2.set_xlabel('Step', fontsize=15)
    axes2.set_ylabel('Average Ranking', fontsize=14)
    axes2.tick_params(axis='both', which='major', labelsize=12)

    plt.savefig(f'{figpath}.png', dpi=400, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    # for subnum in [1, 2, 3, 4]:
    # for subnum in [3]:
    for subnum in [4]:
        for foldnum in [0, 1, 2, 3, 4]:
            figpath = f"/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/progress{subnum}_{foldnum}.png"
            if subnum == 4:
                path1 = f"/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/cmaes_log_{foldnum}_subset{subnum}_2021_02_10.txt"
                path2 = f"/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/cmaes_log_{foldnum}_subset{subnum}_2021_02_09.txt"
                path3 = f'/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/cmaes_log_{foldnum}_subset{subnum}.txt'
                df1 = pd.read_csv(path1, sep=':', header=None)
                df2 = pd.read_csv(path2, sep=':', header=None)
                df3 = pd.read_csv(path3, sep=':', header=None)
                df_t = pd.concat([df2, df1])
                df = pd.concat([df3, df_t])
                if foldnum in [0, 4]:
                    path4 = f"/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/cmaes_log_{foldnum}_subset{subnum}_2021_02_11.txt"
                    df4 = pd.read_csv(path4, sep=':', header=None)
                    df = pd.concat([df, df4])

            elif subnum == 3:
                path1 = f"/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/cmaes_log_{foldnum}_subset{subnum}_2021_02_08.txt"
                path2 = f'/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/cmaes_log_{foldnum}_subset{subnum}.txt'
                df1 = pd.read_csv(path1, sep=':', header=None)
                df2 = pd.read_csv(path2, sep=':', header=None)
                df = pd.concat([df2, df1])
            plot(df, subnum)
