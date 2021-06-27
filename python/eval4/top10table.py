# -------------------------------------------------------------------
# this code list up top potential for each subset
# input :
keyword = ["hbond_top10", "pi_top10", "mix_top10"]
title_kw = ["Hydrogen Bond", "π Stacking", "All"]
sub2 = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/mean_pot_list/best_pot_subset2_nocv.csv"
# output:
outfile = "/Users/mac/Documents/RNP_opt/optimize/Eval4_subset2_top10.csv"
outimg = "/Users/mac/Documents/RNP_opt/optimize/Eval4_subset2_top10.png"

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
pi_type = ["         Pi Stacking"]
separator = '            |'
# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


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
    top10_list = []
    top10_int_list = []
    basic_80_col_names = make_hbond_pair_names()

    for path in [sub2]:
        best_pot_list = []
        with open(path) as f:
            potlist = f.readlines()[0].replace("\n", "").split(",")
        float_list = [float(x) for x in potlist]
        square_sum = sum([x ** 2 for x in float_list])**0.5
        eachpot = [x / square_sum for x in float_list]
        best_pot_list.append(float_list)
        df = pd.DataFrame(best_pot_list)
        low_pot_list.append(df.min(axis=0).to_list())
    collist = make_col_names()
    final_df_int = None
    final_df_str = None
    for sublist1 in low_pot_list:
        for i in range(3):
            sublist = []
            if i == 0:  # hbond
                sublist = sublist1[0:80]
            elif i == 1:  # pi
                sublist = sublist1[80:]
            elif i == 2:  # mix
                sublist = sublist1  # pot values list
            sorted_list = sorted(sublist)[0:10]  # pot list sorted
            subtop10_list = []
            subtop10_int_list = []
            for item in sorted_list:
                name = None
                if i == 2:
                    name = collist[sublist.index(item)].strip()[-5:]
                    subtop10_list.append(f"{str(collist[sublist.index(item)])} ({item:.5f})")
                elif i == 1:
                    name = make_pi_pair_names()[sublist.index(item)].strip()
                    subtop10_list.append(f"{str(make_pi_pair_names()[sublist.index(item)])} ({item:.5f})")
                elif i == 0:
                    name = make_hbond_pair_names()[sublist.index(item)].strip()
                    subtop10_list.append(f"{str(basic_80_col_names[sublist.index(item)])} ({item:.5f})")

                pair_id = basic_80_col_names.index(name)
                subtop10_int_list.append(pair_id//4)
            df_top10 = pd.DataFrame(subtop10_list)
            df_top10_int = pd.DataFrame(subtop10_int_list)
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            top10_array = np.array(df_top10)
            print(top10_array.shape)
            # print(pd.DataFrame(top10_array).to_latex())

            plt.figure(figsize=(14, 5))
            if i == 0:
                final_df_int = df_top10_int
                final_df_str = pd.DataFrame(top10_array)
            else:
                final_df_int = pd.concat([final_df_int, df_top10_int], axis=1)
                final_df_str = pd.concat([final_df_str, pd.DataFrame(top10_array)], axis=1)
        print(final_df_str.to_latex())
        ax = sns.heatmap(final_df_int, alpha=0.5, linecolor="white", cmap='rainbow', linewidths=0.2, fmt="", annot=final_df_str, cbar=False, annot_kws={"color": "black", "fontsize": 14, "ha": 'center'})
        ax.vlines([1, 2], ymin=0, ymax=10, linewidth=5, color="white")
        # ax.hlines([10], xmin=0, xmax=1, linewidth=2, color="black")
        ax.set_yticklabels(nums, rotation=0, size=15)
        ax.set_xticklabels(title_kw, rotation=0, size=17)
        ax.xaxis.tick_top()
        ax.tick_params(left=False, top=False, bottom=False)
        plt.savefig(outimg, dpi=400, bbox_inches='tight')
        plt.show()


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    main()
