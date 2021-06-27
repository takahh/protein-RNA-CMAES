
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
            pair_list.append(f'A\nHydrogen Bond              {amino} C\nG\nU')
        elif amino == aminos[-1]:
            pair_list.append(f'A\n{amino} C\n G\nU')
        else:
            pair_list.append(f'A\n{amino} C\nG\nU')
    for amino in aminos_pi:
        if amino == 'GLU':
            pair_list.append(f'Pseudo-Base Pair              A\n{amino} C\nG\nU')
        elif amino == 'ARG':
            pair_list.append(f'A\n{amino} C\nG\n__________              U')
        else:
            pair_list.append(f'A\n{amino} C\nG\nU')
    for amino in aminos_pi:
        if amino == 'GLU':
            pair_list.append(f'Pi Stack              A\n{amino} C\nG\nU')
        elif amino == 'ARG':
            pair_list.append(f'A\n{amino} C\nG\n__________              U')
        else:
            pair_list.append(f'A\n{amino} C\nG\nU')

    dic_for_boxplot = {}
    # ----------------------------------------------------------
    # main
    # ----------------------------------------------------------
    fig = plt.figure(1, figsize=[10, 37])

    for i in range(152):
        small_list = []
        for k in range(len(pot_list)):
            small_list.append(pot_list[k][i])
        dic_for_boxplot[i] = small_list
    df_data = pd.DataFrame.from_dict(dic_for_boxplot, orient='columns')
    g = sns.boxplot(data=df_data, orient="h")
    # g.set(yticklabels=[])

    ax = fig.add_subplot(1, 1, 1)
    ax.tick_params(length=0)
    minor_ticks = np.arange(1.5, 152.5, 4)
    plt.yticks(minor_ticks, pair_list, size=10)
    plt.vlines(x=0, ymin=-0.5, ymax=152, lw=0.5)
    for loc in [-0.01, -0.005, 0.005, 0.01]:
        plt.vlines(x=loc, ymin=-0.5, ymax=152, lw=0.4, ls='dotted')
    plt.ylim([0, 150])
    major_ticks = np.arange(-0.5, 155.5, 4)
    plt.tick_params(labelsize=13.5, colors='white', labelcolor='black')
    ax.set_yticks(major_ticks, minor=True)
    ax.set_yticks(minor_ticks)
    plt.grid(b=True, which='minor', ls='--')
    plt.savefig(figpath, bbox_inches='tight', dpi=100)
    plt.show(bbox_inches='tight')

