##  Convergence Plot for Eval 3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

evalnum = 3
figpath = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/progress.png"


def plot():
    path = f'/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/cmaes_log.txt'
    df = pd.read_csv(path, sep=':', header=None)
    figure = plt.figure()
    axes = figure.add_axes([0.14, 0.12, 0.83, 0.81])
    axes2 = figure.add_axes([0.4, 0.4, 0.52, 0.48])  # rested
    x = np.arange(len(df))
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_xlabel('Step', fontsize=15)
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    if evalnum == 2:
        axes.set_title(f'Evaluation {evalnum}', fontsize=18)
    else:
        axes.set_title(f'Evaluation {evalnum}', fontsize=18)

    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    if evalnum == 2:
        axes2.set_ylim([1, 1.05])
        axes2.set_xlim([1000, 5000])
    else:
        axes2.set_ylim([1, 1.1])
        axes2.set_xlim([3000, 7000])
    axes2.set_xlabel('Step', fontsize=15)
    axes2.set_ylabel('Average Ranking', fontsize=14)
    axes2.tick_params(axis='both', which='major', labelsize=12)

    plt.savefig(f'{figpath}.png', dpi=400, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    plot()
