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
from boxplot_pot import box_plot
import pickle

# -------------------------------------------------------------------
# constant
# -------------------------------------------------------------------
path = '/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/'
logfile = path + 'cmaes_log.txt'
out = path + 'more_test_pot_boxplot.png'
best = path + 'best_pot.csv'
# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


def file2list(file_path):
    pot_list = []
    import pandas as pd
    df = pd.read_csv(file_path)
    print(df)
    with open(file_path) as f:
        for lines in f.readlines():
            rank = float(lines.split(":")[0])
            if rank == 1.0:
                pot_list.append(lines)
    pot_list = [float(x) for x in pot_list]
    return pot_list


def main():
    bestline = ""
    bestrank = 10
    bestline_list = []
    best_pot_list = []

    import pandas as pd
    df = pd.read_csv(logfile, sep=":", header=None)
    lowest_rank = float(min(df[0]))
    with open(logfile) as f:
        for lines in f.readlines():
            rank = float(lines.split(":")[0])
            if rank == lowest_rank:
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
    box_plot(best_pot_list, out)
    # box_plot(best_pot_list, out, best_pot)


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    main()