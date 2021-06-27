# pot optimization for five fold is done.
# now apply the potentials to 1/5 data
# 1. normalize pot
# 2. plot pots
# 3. calculate avg rank for 1/5

from boxplot_eval1 import box_plot1
from apply_mean_w import apply_mean_cq
import pandas as pd
from utilities import get_test_ids

# normalize pot
path = '/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval1/'


def line2list(line, potlist):
    str_list = line.split('[')[1].split(']')[0].strip().split(',')
    float_list = [float(x) for x in str_list]
    square_sum = sum([x ** 2 for x in float_list])
    potlist.append([x / square_sum for x in float_list])
    return potlist


def plot_five():
    for i in range(5):
        pot_list = []
        logpath = f'{path}cmaes_log_{i}.txt'
        df = pd.read_csv(logpath, sep=":", header=None)
        bestrank = min(df[0])
        figpath = logpath.replace(".txt", "_potplot.png")  # cmaes_log_4.txt
        best_list = df[df[0] == bestrank][4].tolist()
        for pot_str in iter(best_list):
            pot_list = line2list(pot_str, pot_list)
        box_plot1(pot_list, figpath)


def plot_five_in_one():
    pot_list = []
    figpath = path + "in_one_potplot.png"  # cmaes_log_4.txt
    for i in range(5):
        logpath = f'{path}cmaes_log_{i}.txt'
        df = pd.read_csv(logpath, sep=":", header=None)
        bestrank = min(df[0])
        best_list = df[df[0] == bestrank][4].tolist()
        for pot_str in iter(best_list):
            pot_list = line2list(pot_str, pot_list)
    box_plot1(pot_list, figpath)


if __name__ == "__main__":
    # plot_five()
    plot_five_in_one()
