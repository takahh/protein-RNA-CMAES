# pot optimization for five fold is done.
# now apply the potentials to 1/5 data
# 1. normalize pot
# 2. plot pots
# 3. calculate avg rank for 1/5

# from apply_mean_w import apply_mean_cq
import pandas as pd
# from utilities import get_test_ids

# normalize pot
path = '/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval2/'
# /Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval2/eval2cmaes_log_2.txt

# ----------------------------------------------------------
# this code is for plotting potentials whose with rank 1
# ----------------------------------------------------------


def box_plot2(pot_list, figpath, best_pot=None):  # Eval 4
    # ----------------------------------------------------------
    # import
    # ----------------------------------------------------------
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd

    # ----------------------------------------------------------
    # constants
    # ----------------------------------------------------------

    aminos = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLU', 'GLN', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO',
              'SER', 'THR', 'TRP', 'TYR', 'VAL']
    baces = ['A', 'C', 'G', 'U']
    aminos_pi = ["ARG", "TRP", "ASN", "HIS", "GLU", "GLN", "TYR", "PHE", "ASP"]
    pi_type = ["pair", "stack"]
    separator = '          |'

    # ----------------------------------------------------------
    # functions
    # ----------------------------------------------------------

    pair_list = []
    for amino in aminos:
        if amino == 'ILE':
            pair_list.append(f'ACGU\n{amino}\n\nHydrogen Bond')
        elif amino == aminos[-1]:
            pair_list.append(f'ACGU\n{amino}\n{separator}\n{separator}')
        else:
            pair_list.append(f'ACGU\n{amino}')
    for amino in aminos_pi:
        if amino == 'GLU':
            pair_list.append(f'ACGU\n{amino}\n\nπ Interaction')
        elif amino == aminos[3]:
            pair_list.append(f'ACGU\n{amino}\n\n')
        else:
            pair_list.append(f'ACGU\n{amino}\n')

    dic_for_boxplot = {}
    # ----------------------------------------------------------
    # main
    # ----------------------------------------------------------
    fig = plt.figure(1, figsize=[22, 5])

    for i in range(116):
        small_list = []
        for k in range(len(pot_list)):
            try:
                small_list.append(pot_list[k][i])
            except IndexError:
                print(f"k={k}, i={i}")
        dic_for_boxplot[i] = small_list
    df_data = pd.DataFrame.from_dict(dic_for_boxplot, orient='columns')
    g = sns.boxplot(data=df_data)
    g.set(xticklabels=[])
    # for i in range(len(pot_list)):
    #     plt.scatter(list(range(0, 152)), pot_list[i])
    # plt.scatter(list(range(0, 152)), best_pot, s=120, color='black', marker="*")

    ax = fig.add_subplot(1, 1, 1)
    ax.tick_params(length=0)
    minor_ticks = np.arange(1.5, 116.5, 4)
    plt.xticks(minor_ticks, pair_list, size=10)
    plt.hlines(y=0, xmin=-0.5, xmax=116, lw=0.5)
    plt.xlim([0, 114])
    major_ticks = np.arange(-0.5, 119.5, 4)
    plt.tick_params(labelsize=13.5, colors='white', labelcolor='black')
    ax.set_xticks(major_ticks, minor=True)
    ax.set_xticks(minor_ticks)
    plt.grid(b=True, which='minor', ls='--')
    plt.savefig(figpath, bbox_inches='tight', dpi=500)
    plt.show(bbox_inches='tight')


def line2list(line, potlist):
    str_list = line.split('[')[1].split(']')[0].strip().split(',')
    float_list = [float(x) for x in str_list]
    square_sum = sum([x ** 2 for x in float_list])**0.5
    potlist.append([x / square_sum for x in float_list])
    return potlist


def plot_five():
    for i in range(1, 6):
        pot_list = []
        logpath = f'{path}eval2cmaes_log_{i}.txt'
        df = pd.read_csv(logpath, sep=":", header=None)
        bestrank = min(df[0])
        figpath = logpath.replace(".txt", "_potplot.png")  # cmaes_log_4.txt
        best_list = df[df[0] == bestrank][4].tolist()
        for pot_str in iter(best_list):
            pot_list = line2list(pot_str, pot_list)
        print(pot_list)
        box_plot2(pot_list, figpath)


def plot_five_in_one():
    pot_list = []
    figpath = path + "in_one_potplot.png"  # cmaes_log_4.txt
    for i in range(0, 5):
        logpath = f"/Users/mac/Desktop/t3_mnt/RNPopt/optimize/pi_plus_cmaes_log_{i}.txt"
        df = pd.read_csv(logpath, sep=":", header=None)
        bestrank = min(df[0])
        best_list = df[df[0] == bestrank][4].tolist()
        for pot_str in iter(best_list):
            pot_list = line2list(pot_str, pot_list)
    box_plot2(pot_list, figpath)


if __name__ == "__main__":
    # plot_five()
    plot_five_in_one()
