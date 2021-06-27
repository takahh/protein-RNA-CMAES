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
log_eval4_1 = f"{path}/eval4/cmaes_log_all_subset1_2021_02_23.txt"
log_eval4_2 = f"{path}/eval4/cmaes_log_all_subset2_2021_02_23.txt"
log_eval4_3 = f"{path}/eval4/cmaes_log_all_subset3_2021_02_23.txt"
log_eval4_4 = f"{path}/eval4/cmaes_log_all_subset4_2021_02_23.txt"
log_eval4_4_2 = f"{path}/eval4/cmaes_log_all_subset4_2021_02_24.txt"

# output:
figpath2 = f'{path}all_time_plot_eval4.png'

xrange = [0, 20000]
x_zoomed_range = [3000, 20000]

# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


def plot_1_asis(fig, bottm_or_not, gs, x, df):
    axes = fig.add_subplot(gs[0, 0])
    axes.set_xlim(xrange)
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'', fontsize=18)
    axes.set_title(f'Subset 1', fontsize=18)
    if not bottm_or_not:
        axes.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_1_zoom(fig, bottm_or_not, gs, x, df):
    axes2 = fig.add_subplot(gs[0, 1])
    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    axes2.set_ylim([1, 1.1])
    axes2.set_xlim(x_zoomed_range)
    # axes2.set_ylabel('Average Ranking', fontsize=14)
    axes2.set_title(f'Enlarged at Convergence', fontsize=18)
    axes2.tick_params(axis='both', which='major', labelsize=12)
    if not bottm_or_not:
        axes2.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_1(fig, gs):
    df = pd.read_csv(log_eval4_1, sep=':', header=None)
    x = np.arange(len(df))
    plot_1_zoom(fig, False, gs, x, df)
    plot_1_asis(fig, False, gs, x, df)


def plot_2_asis(fig, bottm_or_not, gs, x, df):
    axes = fig.add_subplot(gs[1, 0])
    axes.set_xlim(xrange)
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'Subset 2', fontsize=18)
    if not bottm_or_not:
        axes.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_2_zoom(fig, bottm_or_not, gs, x, df):
    axes2 = fig.add_subplot(gs[1, 1])
    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    axes2.set_ylim([1, 1.15])
    axes2.set_xlim(x_zoomed_range)
    # axes2.set_ylabel('Average Ranking', fontsize=14)
    # axes2.set_title(f'Evaluation 2, Fold:1', fontsize=18)
    axes2.tick_params(axis='both', which='major', labelsize=12)
    if not bottm_or_not:
        axes2.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_2(fig, gs):
    df = pd.read_csv(log_eval4_2, sep=':', header=None)
    x = np.arange(len(df))
    plot_2_zoom(fig, False, gs, x, df)
    plot_2_asis(fig, False, gs, x, df)


def plot_3_asis(fig, bottm_or_not, gs, x, df):
    axes = fig.add_subplot(gs[2, 0])
    axes.set_xlim(xrange)
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_xlabel('Step', fontsize=15)
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'Subset 3', fontsize=18)
    if not bottm_or_not:
        axes.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_3_zoom(fig, bottm_or_not, gs, x, df):
    axes2 = fig.add_subplot(gs[2, 1])
    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    axes2.set_ylim([3.44, 3.54])
    axes2.set_xlim(x_zoomed_range)
    axes2.set_xlabel('Step', fontsize=15)
    # axes2.set_ylabel('Average Ranking', fontsize=14)
    # axes2.set_title(f'Evaluation 3', fontsize=18)
    axes2.tick_params(axis='both', which='major', labelsize=12)
    if not bottm_or_not:
        axes2.tick_params(axis='x', labelbottom=False, which='both', bottom=False, top=False)


def plot_3(fig, gs):
    df = pd.read_csv(log_eval4_3, sep=':', header=None)
    x = np.arange(len(df))
    plot_3_zoom(fig, False, gs, x, df)
    plot_3_asis(fig, False, gs, x, df)



def plot_4_asis(fig, bottm_or_not, gs, x, df):
    axes = fig.add_subplot(gs[3, 0])
    axes.set_xlim(xrange)
    axes.plot(x, df[0], 'b', linewidth=0.7, alpha=0.6, color="blue")
    axes.set_xlabel('Step', fontsize=15)
    axes.set_ylabel('Average Ranking', fontsize=18)
    axes.tick_params(axis='both', which='major', labelsize=12)
    axes.set_title(f'Subset 4', fontsize=18)


def plot_4_zoom(fig, bottm_or_not, gs, x, df):
    axes2 = fig.add_subplot(gs[3, 1])
    axes2.plot(x, df[0], 'r', linewidth=0.5, alpha=0.6, color="blue")
    axes2.set_ylim([12.4, 13])
    axes2.set_xlim(x_zoomed_range)
    axes2.set_xlabel('Step', fontsize=15)
    # axes2.set_ylabel('Average Ranking', fontsize=14)
    # axes2.set_title(f'Evaluation 3', fontsize=18)
    axes2.tick_params(axis='both', which='major', labelsize=12)


def plot_4(fig, gs):
    df1 = pd.read_csv(log_eval4_4, sep=':', header=None)
    df2 = pd.read_csv(log_eval4_4_2, sep=':', header=None)
    df = pd.concat([df1, df2])
    x = np.arange(len(df))
    plot_4_zoom(fig, False, gs, x, df)
    plot_4_asis(fig, False, gs, x, df)


    # plot_each(its_list1, cur_list1, figpath, dbname, bindtype[0, 0], 3600, 20, cur_avg1, its_avg1, ax, "upper")
    # ax.set_ylabel(f'{name_dict[dbname]}\n{btype_dict[bindtype[0, 0]]}', size=14)

    # # second plot
    # ax = fig.add_subplot(gs[1], sharex=ax)
    # plot_each(its_list2, cur_list2, figpath, dbname, bindtype[1], 3600, 20, cur_avg2, its_avg2, ax, "bottom")
    # ax.set_ylabel(f'{name_dict[dbname]}\n{btype_dict[bindtype[1]]}', size=14)

    plt.savefig(figpath2, dpi=300, bbox_inches='tight')
    plt.show()


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    fig = plt.figure(figsize=(9, 16))
    gs = gridspec.GridSpec(4, 2)
    plot_1(fig, gs)
    plot_2(fig, gs)
    plot_3(fig, gs)
    plot_4(fig, gs)