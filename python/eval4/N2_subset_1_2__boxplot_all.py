# -------------------------------------------------------------------
# this code take all the potential and
#  1. collect best potentials and normalize them
#  2. write to "best_pot.csv"
#  3. plot boxplot
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# import
# -------------------------------------------------------------------
# from pot_plot_more_tests import plot_pot_pi_plus2, plot_pot_pi_plus
from eval4_boxplot_nopbp import box_plot
import pickle
import pandas as pd

# -------------------------------------------------------------------
# constant
# -------------------------------------------------------------------
path = '/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/'
test = '/Users/mac/Desktop/test'
out = path + 'more_test_pot_boxplot.png'
best = path + 'best_pot.csv'
# "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/cmaes_log_all_subset2_2021_02_13.txt"
# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


def file2list(file_path):
    pot_list = []
    with open(file_path) as f:
        for lines in f.readlines():
            rank = float(lines.split(":")[0])
            if rank == 1.0:
                pot_list.append(lines)
    pot_list = [float(x) for x in pot_list]
    return pot_list


def main():
    for subset in range(1, 5):
        out = path + f'plots/no_cv_pot_boxplot_subset{subset}_all.png'
        best = path + f'optimized_normed_pot_list/best_pot_subset{subset}_nocv.csv'
        mean = path + f'mean_pot_list/best_pot_subset{subset}_nocv.csv'
        if subset == 4:
            logfile = path + f"cmaes_log_all_subset{subset}_2021_02_24.txt"
            # logfile = test
        elif subset == 3:
            logfile = path + f"cmaes_log_all_subset{subset}_2021_02_23.txt"
        elif subset == 2:
            logfile = path + f"cmaes_log_all_subset{subset}_2021_02_23.txt"
        else:
            logfile = path + f"cmaes_log_all_subset{subset}_2021_02_23.txt"
        bestline = ""
        bestrank = 10
        bestline_list = []
        best_pot_list = []
        df = pd.read_csv(logfile, header=None, sep=":")
        lowest_rank = min(df[0])
        print(lowest_rank)
        with open(logfile) as f:
            for lines in f.readlines():
                rank = float(lines.split(":")[0])
                if (rank - lowest_rank) < 1e-14:
                    bestline_list.append(lines)
        with open(best, "w") as f:
            for bestline in bestline_list:
                str_list = bestline.split('[')[1].split(']')[0].strip().split(',')
                float_list = [float(x) for x in str_list]
                square_sum = sum([x ** 2 for x in float_list])**0.5
                eachpot = [x / square_sum for x in float_list]
                potlength = len(eachpot)
                for i in range(potlength):
                    if i < potlength - 1:
                        f.writelines(f"{eachpot[i]},")
                    else:
                        f.writelines(f"{eachpot[i]}\n")
                best_pot_list.append(eachpot)
        # plot_pot_pi_plus(best_pot_list, out)
        # plot_pot_pi_plus2(best_pot_list, out, best_pot)
        box_plot(best_pot_list, out, subset, mean)
        # box_plot(best_pot_list, out, best_pot)


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    main()
