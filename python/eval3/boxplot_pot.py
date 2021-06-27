
# ----------------------------------------------------------
# this code is for plotting potentials whose with rank 1
# ----------------------------------------------------------


def box_plot(pot_list, figpath, best_pot=None):  # Eval 4
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
    separator = '            |'

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
            small_list.append(pot_list[k][i])
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

