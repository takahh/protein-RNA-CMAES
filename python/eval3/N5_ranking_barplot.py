# Plot ranking histograms for Eval3 and ITScore-PR

path1 = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/"
figpath = f'{path1}ranking_histo_eval_its.png'  # cmaes_log_4.txt
log1 = f'{path1}best_performance_pot.csv'
# ranking data : f"{path1}/ranking/perez_ub_{best_index}_rankings.csv"
itscore_path = '/Volumes/HDCZ-UT/Research/RNP/Extra_Test/itscore/results/rankings/'  # Zou_bb.csv
bench_names = ["Zou_uu", "Zou_bb", "perez_uu", "perez_ub"]
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
    # df.hist(bins=max(df['rank'].values.tolist())-1)
    this_list1 = df1['rank'].values.tolist()

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