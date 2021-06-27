# -------------------------------------------------------------------
# this code makes a plot to compare the current results and ITS
# on the four benchmarks
# input :
#    ITS: /Volumes/HDCZ-UT/Research/RNP/Extra_Test/itscore/results/rankings/Zou_bb.csv
#    current: /Volumes/HDCZ-UT/Research/RNP/Extra_Test/scoring/perez_ub_21_rankings.csv
# output:
#    /Volumes/HDCZ-UT/Research/RNP/Extra_Test/plot/compare_rankings/Zou_bb.png
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
path = "/Volumes/HDCZ-UT/Research/RNP/Extra_Test/"
path2 = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/"
its_path = f"{path}itscore/results/rankings/"
current_path = f"{path2}ranking/"
output_dir = f"/{path}plot/compare_rankings/"
namelist = ['Zou', 'perez']
zou_type = ['uu', 'bb']
perez_type = ['ub', 'uu']
btype_dict = {'bb': 'bound-bound', 'ub': 'unbound-bound', 'uu': 'unbound-unbound'}
name_dict = {'perez': 'Perez', 'Zou': 'Zou'}

# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


def plot_each(its_list, this_list, figpath, name, btype, bin_num, upper_lim, cur_mean, its_mean, ax, upper_or_bottom):
    # bins = int(max(its_list))
    # plt.hist(this_list, bins, alpha=0.5,  color='red')
    # plt.hist([this_list, its_list], bins, alpha=1, label=['Current', 'ITSCore-PR'])
    ax.set_xlim([1, upper_lim - 2.5])
    # plt.title(f'{name_dict[name]}, {btype_dict[btype]}', fontsize=18)
    # plt.tick_params(labelsize=12)
    if upper_or_bottom == "bottom":
        print("here")
        ticks_loc = np.arange(1, upper_lim, 0.93)
        ticks = np.arange(1, upper_lim + 1)
        hticks = ticks_loc + 0.45
        plt.xticks(hticks, ticks)
        plt.xlabel('Rank', fontsize=15)
        plt.ylabel('Frequency', fontsize=15)

    else:
        # plt.rcParams['xtick.bottom'] = False
        # plt.rcParams['xtick.labelbottom'] = False
        ax.tick_params(
            axis='x',  # changes apply to the x-axis
            labelbottom=False,
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False)        # ticks along the top edge are off)
    plt.xlim([1, upper_lim - 1.5])
    ax.hist([this_list, its_list], alpha=1, bins=bin_num, label=[f'Current (Avg.{cur_mean:.1f})',
                                                                  f'ITSCore-PR (Avg.{its_mean:.1f})'])
    plt.legend(fontsize=12)


def get_score_list(ranking_file):
    df = pd.read_csv(ranking_file, header=None)
    score_list = df[1].tolist()
    return score_list


def remove_nan(original_list):
    new_list = [x for x in original_list if not math.isnan(x)]
    return new_list


def bar_plot(dbname, bindtype):
    # input :
    #    ITS: /Volumes/HDCZ-UT/Research/RNP/Extra_Test/itscore/results/rankings/Zou_bb.csv
    #    current: /Volumes/HDCZ-UT/Research/RNP/Extra_Test/scoring/perez_ub_21_rankings.csv
    its_ranking1 = f'{its_path}{dbname}_{bindtype[0]}.csv'
    its_ranking2 = f'{its_path}{dbname}_{bindtype[1]}.csv'
    curr_ranknig1 = f'{current_path}{dbname}_{bindtype[0]}_656_rankings.csv'
    curr_ranknig2 = f'{current_path}{dbname}_{bindtype[1]}_656_rankings.csv'
    # /Volumes/HDCZ-UT/Research/RNP/Extra_Test/plot/compare_rankings/Zou_bb.png
    figpath = f'{path2}{dbname}.png'

    # 1
    cur_list1 = remove_nan(get_score_list(curr_ranknig1))
    cur_avg1 = sum(cur_list1)/len(cur_list1)
    its_list1 = remove_nan(get_score_list(its_ranking1))
    its_avg1 = sum(its_list1)/len(its_list1)

    print('here1')
    # 2
    cur_list2 = remove_nan(get_score_list(curr_ranknig2))
    cur_avg2 = sum(cur_list2)/len(cur_list2)
    print('here2')
    its_list2 = remove_nan(get_score_list(its_ranking2))
    its_avg2 = sum(its_list2)/len(its_list2)

    gs = gridspec.GridSpec(2, 1)
    fig = plt.figure()
    print('here3')
    # first plot
    ax = fig.add_subplot(gs[0])
    plot_each(its_list1, cur_list1, figpath, dbname, bindtype[0], 3600, 20, cur_avg1, its_avg1, ax, "upper")
    ax.set_ylabel(f'{name_dict[dbname]}\n{btype_dict[bindtype[0]]}', size=14)
    # ax.get_yaxis().set_label_coords(-0.1, 0.5)
    # plt.tick_params(
    #     axis='x',  # changes apply to the x-axis
    #     labelbottom='off')  # labels along the bottom edge are off

    # second plot
    ax = fig.add_subplot(gs[1], sharex=ax)
    plot_each(its_list2, cur_list2, figpath, dbname, bindtype[1], 3600, 20, cur_avg2, its_avg2, ax, "bottom")
    ax.set_ylabel(f'{name_dict[dbname]}\n{btype_dict[bindtype[1]]}', size=14)
    # ax.get_yaxis().set_label_coords(-0.1, 0.5)

    # plot_each(its_list, cur_list, figpath, dbname, bindtype, 3600, 21, cur_avg, its_avg)
    # plt.rcParams["figure.figsize"] = (20, 40)
    plt.savefig(figpath, dpi=300)
    plt.show()


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    for name in namelist:
        if name == 'perez':
            bar_plot(name, perez_type)
        else:
            bar_plot(name, zou_type)
