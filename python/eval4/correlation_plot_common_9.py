# -------------------------------------------------------------------
# this code list up top potential for each subset
# input :
keyword = ["hbond_top10", "pi_top10", "mix_top10"]
title_kw = ["Hydrogen Bond", "Pi Stacking", "All"]
sub2 = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/mean_pot_list/best_pot_subset2_nocv.csv"
# output:
outfile = "/Users/mac/Documents/RNP_opt/optimize/Eval4_subset2_top10.csv"
figpath = "/Users/mac/Documents/RNP_opt/optimize/corr_9_pi.png"

# -------------------------------------------------------------------

# -------------------------------------------------------------------
# import
# -------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.colors import ListedColormap

# -------------------------------------------------------------------
# constant
# -------------------------------------------------------------------
aminos = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLU', 'GLN', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO',
          'SER', 'THR', 'TRP', 'TYR', 'VAL']
baces = ['A', 'C', 'G', 'U']
aminos_pi = ["ARG", "TRP", "ASN", "HIS", "GLU", "GLN", "TYR", "PHE", "ASP"]
rings = ["HIS", "TRP", "PHE", "TYR"]

pi_type = ["         Pi Stacking"]
separator = '            |'
# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------
import matplotlib.lines as mlines


def make_col_names():
    colnames = []
    for amino in aminos:
        for bace in baces:
            colnames.append(f"   Hydrogen Bond {amino}_{bace}")
    for pi_typ in pi_type:
        for amino in aminos_pi:
            for bace in baces:
                colnames.append(f"{pi_typ} {amino}_{bace}")
    return colnames


def color_list():
    color_list = []
    for item in aminos_pi:
        if item in rings:
            color_list += ["grey"] * 4
        else:
            color_list += ["blue"] * 4
    return color_list


def make_hbond_pair_names():
    colnames = []
    for amino in aminos:
        for bace in baces:
            colnames.append(f"{amino}_{bace}")
    return colnames


def make_pi_pair_names():
    colnames = []
    for amino in aminos_pi:
        for bace in baces:
            colnames.append(f"{amino}_{bace}")
    return colnames


def main():
    import pandas as pd
    low_pot_list = []

    for path in [sub2]:
        best_pot_list = []
        with open(path) as f:
            potlist = f.readlines()[0].replace("\n", "").split(",")
        float_list = [float(x) for x in potlist]
        square_sum = sum([x ** 2 for x in float_list])**0.5
        best_pot_list.append(float_list)
        df = pd.DataFrame(best_pot_list)
        low_pot_list.append(df.min(axis=0).to_list())
    hbond_9pot_list = []
    for amino in aminos:
        if amino in aminos_pi:
            amino_index = aminos_pi.index(amino)
            hbond_9pot_list += float_list[amino_index * 4: 4 * (amino_index + 1)]
    pi_9pot_list = float_list[80:]
    label_list =make_pi_pair_names()
    plt.figure()
    fsize = 8.5
    lsize = 13
    minv = -0.22
    maxv = 0.13
    plt.ylim(minv, maxv)
    plt.xlim(minv, maxv)

    blue_circle = plt.scatter([], [], color='blue')
    green_circle = plt.scatter([], [], color='grey')
    xpoints = ypoints = plt.xlim()
    print(len(color_list()))
    for j in range(0, 36):
        plt.scatter(hbond_9pot_list[j], pi_9pot_list[j], color=color_list()[j], alpha=0.7)
    plt.xlabel("Potential for Hydrogen Bond", size=lsize)
    plt.ylabel("Potential for Pi Stacking", size=lsize)
    for label, x, y in zip(label_list, hbond_9pot_list, pi_9pot_list):
        if label in ["HIS_C", "ASN_G", "TYR_C", "ASN_A", "TRP_C"]:  # lower
            plt.annotate(label, xy=(x + 0.004, y - 0.008), size=fsize)
        elif label in ["ASP_G"]:  # higher
            plt.annotate(label, xy=(x + 0.004, y + 0.006), size=fsize)
        elif label in ["TRP_U", "PHE_U", "ARG_A"]:  # higher left
            plt.annotate(label, xy=(x - 0.029, y + 0.001), size=fsize)
        else:
            plt.annotate(label, xy=(x + 0.004, y), size=fsize)
    plt.plot(xpoints, ypoints, linestyle='--', color='grey', lw=0.4, scalex=False, scaley=False)
    plt.legend([blue_circle, green_circle], ["Non Aromatic Ring", "Aromatic Ring"], fontsize=9)
    plt.savefig(figpath, bbox_inches="tight")
    plt.show()


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    main()
