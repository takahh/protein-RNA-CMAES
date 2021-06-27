# -------------------------------------------------------------------
# this code gathers time plots for Eval 1, 2, 3,
#                            and 4 subsets in Eval 4
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# import
# -------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import matplotlib.gridspec as gridspec

# -------------------------------------------------------------------
# constant
# -------------------------------------------------------------------
path = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/"

# input :
log_eval1 = f"{path}/eval1/cmaes_log_0.txt"
log_eval2 = f"{path}/eval2/eval2cmaes_log_1.txt"
log_eval3 = f"{path}/eval3/cmaes_log.txt"

# output:
figpath1 = f'{path}all_time_plot_eval1_3.png'
# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


def plot_1_asis(fig, bottm_or_not, gs, x, df):
    axes = fig.add_subplot(gs[0, 0])
    axes.set_xlim([0, 5500])
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'', fontsize=18)
    axes.set_title(f'Evaluation 1, Fold:1', fontsize=18)
    if not bottm_or_not:
        axes.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_1_zoom(fig, bottm_or_not, gs, x, df):
    axes2 = fig.add_subplot(gs[0, 1])
    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    axes2.set_ylim([1, 1.35])
    axes2.set_xlim([1000, 6000])
    # axes2.set_ylabel('Average Ranking', fontsize=14)
    axes2.set_title(f'Enlarged at Convergence', fontsize=18)
    axes2.tick_params(axis='both', which='major', labelsize=12)
    if not bottm_or_not:
        axes2.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_1(fig, gs):
    df = pd.read_csv(log_eval1, sep=':', header=None)
    x = np.arange(len(df))
    plot_1_zoom(fig, False, gs, x, df)
    plot_1_asis(fig, False, gs, x, df)


def plot_2_asis(fig, bottm_or_not, gs, x, df):
    axes = fig.add_subplot(gs[1, 0])
    axes.set_xlim([0, 5500])
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'Evaluation 2, Fold:1', fontsize=18)
    if not bottm_or_not:
        axes.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_2_zoom(fig, bottm_or_not, gs, x, df):
    axes2 = fig.add_subplot(gs[1, 1])
    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    axes2.set_ylim([1, 1.1])
    axes2.set_xlim([1000, 6000])
    # axes2.set_ylabel('Average Ranking', fontsize=14)
    # axes2.set_title(f'Evaluation 2, Fold:1', fontsize=18)
    axes2.tick_params(axis='both', which='major', labelsize=12)
    if not bottm_or_not:
        axes2.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_2(fig, gs):
    df = pd.read_csv(log_eval2, sep=':', header=None)
    x = np.arange(len(df))
    plot_2_zoom(fig, False, gs, x, df)
    plot_2_asis(fig, False, gs, x, df)


def plot_3_asis(fig, bottm_or_not, gs, x, df):
    axes = fig.add_subplot(gs[2, 0])
    axes.set_xlim([0, 5500])
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_xlabel('Step', fontsize=15)
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'Evaluation 3', fontsize=18)


def plot_3_zoom(fig, bottm_or_not, gs, x, df):
    axes2 = fig.add_subplot(gs[2, 1])
    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    axes2.set_ylim([1, 1.1])
    axes2.set_xlim([1000, 6000])
    axes2.set_xlabel('Step', fontsize=15)
    # axes2.set_ylabel('Average Ranking', fontsize=14)
    # axes2.set_title(f'Evaluation 3', fontsize=18)
    axes2.tick_params(axis='both', which='major', labelsize=12)


def plot_3(fig, gs):
    df = pd.read_csv(log_eval3, sep=':', header=None)
    x = np.arange(len(df))
    plot_3_zoom(fig, False, gs, x, df)
    plot_3_asis(fig, False, gs, x, df)


def plot_1_3(fig):
    gs = gridspec.GridSpec(3, 2)
    plot_1(fig, gs)
    plot_2(fig, gs)
    plot_3(fig, gs)

    # plot_each(its_list1, cur_list1, figpath, dbname, bindtype[0, 0], 3600, 20, cur_avg1, its_avg1, ax, "upper")
    # ax.set_ylabel(f'{name_dict[dbname]}\n{btype_dict[bindtype[0, 0]]}', size=14)

    # # second plot
    # ax = fig.add_subplot(gs[1], sharex=ax)
    # plot_each(its_list2, cur_list2, figpath, dbname, bindtype[1], 3600, 20, cur_avg2, its_avg2, ax, "bottom")
    # ax.set_ylabel(f'{name_dict[dbname]}\n{btype_dict[bindtype[1]]}', size=14)

    plt.savefig(figpath1, dpi=300, bbox_inches='tight')
    plt.show()


def plot4():
    pass


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    fig = plt.figure(figsize=(9, 12))
    plot_1_3(fig)
    plot4()