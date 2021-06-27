
path2 = '/Users/mac/Documents/RNPopt/data/result/eval2/' # cmaes_log_4.txt
log2 = f'{path2}five_fold_cv_test.log'

path1 = '/Users/mac/Documents/RNP_opt/optimize/hbond_optimized/'  # cmaes_log_4.txt
figpath = '/Users/mac/Documents/RNP_opt/optimize/hbond_optimized/its_this_histo_for_hb_and_pi.png'  # cmaes_log_4.txt
log1 = f'{path1}five_fold_cv_test.log'

itscore_path = '/Users/mac/Documents/RNP_opt/rankings.csv'

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_avg(rank_list):
    return sum(rank_list)/len(rank_list)


def bar_plot_rankings():
    plt.figure(figsize=(9, 3))
    plt.xlim([1, 20])
    plt.title('')
    plt.tick_params(labelsize=12)
    plt.xlabel('Rank', fontsize=15)
    plt.ylabel('Frequency', fontsize=15)
    ticks = np.arange(1,20)
    hticks = ticks + 0.5
    plt.xticks(hticks, ticks)
    # for log in [log1, log2]:
    df1 = pd.read_csv(log1, names=['id', 'rank'])
    df2 = pd.read_csv(log2, names=['id', 'rank'])
    # df.hist(bins=max(df['rank'].values.tolist())-1)
    this_list1 = df1['rank'].values.tolist()
    this_list2 = df2['rank'].values.tolist()

    its_list = pd.read_csv(itscore_path)[' its_rank'].tolist()
    # bins = int(max(its_list)/1)
    bins = max(its_list)
    # plt.hist(this_list, bins, alpha=0.5,  color='red')
    col_list = ["blue", "green", "red"]
    label_list = [f'Current (Eval 1, avg. {get_avg(this_list1):.1f})', f'Current (Eval 2, avg. {get_avg(this_list2):.1f})', f'ITSCore-PR (avg. {get_avg(its_list):.1f})']
    plt.hist([this_list1, this_list2, its_list], bins, color=col_list, alpha=0.5, label=label_list)

    plt.legend(fontsize=12)
    plt.savefig(figpath, dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    bar_plot_rankings()