# ----------------------------------------------------------
# this code is for optimizing potentials on all data
# including original and extra data except bad ids
# ----------------------------------------------------------

# ----------------------------------------------------------
# import
# ----------------------------------------------------------
import pandas as pd
import copy
import numpy as np
import multiprocessing
from python.utilities import remove_remove_id2, give_me_np, get_length
import datetime

# ----------------------------------------------------------
# constant
# ----------------------------------------------------------
current_date = datetime.date.today().strftime('%Y_%m_%d')
np = 168
# ----------------------------------------------------------
# functions
# ----------------------------------------------------------


def get_previous_pot(previous_result):
    with open(previous_result) as f:
        for lines in f.readlines():
            if len(lines) > 6:
                lastline = lines
            else:
                pass
        init_pot0 = lastline.split('[')[1].split(']')[0].split(',')
    return init_pot0


def replace_for_t3(path):
    rep_dic = {"/Volumes/HDCZ-UT/Research/RNP/Extra_Test/": "/gs/hs0/tga-science/kimura/RNPopt/data/benchmark/",
               "/Users/mac/Documents/RNP_opt/": "/gs/hs0/tga-science/kimura/RNPopt/data/",
               "/Volumes/HDCZ-UT/Research/RNP/": "/gs/hs0/tga-science/kimura/RNPopt/data/benchmark/"}
    for keyword in rep_dic.keys():
        if keyword in path:
            path = path.replace(keyword, rep_dic[keyword])
    return path


def apply_mean_final(test_id, pot_vec, df_nega, df_posi):
    df_nega_target = df_nega
    try:
        if 'Zou' in test_id or 'perez' in test_id:  # test_id: perez_ub_1WPU
            #  /gs/hs0/tga-science/kimura/RNPopt/data/benchmark/non_native_combined_vecs/Zou/bb/2ANR.out
            #
            posi_vec = df_posi[df_posi['vec_id'] == test_id].values.tolist()[0][2:154]
        else:
            posi_vec = df_posi[df_posi['vec_id'] == test_id].values.tolist()[0][2:154]

    except IndexError:
        print(f"{test_id} INDEX ERROR")
        return np.array([0, 0])  # rank, count

    wx_list = []
    # calcluate wx and make a dataframe
    for index, row in df_nega_target.iterrows():
        if 'Zou' in test_id or 'perez' in test_id:
            n_vec = row.tolist()[1:153]
        else:
            n_vec = row.tolist()[2:154]
        wx = sum([x * y for x, y in zip(n_vec, pot_vec)])  # use numpy?
        wx_list.append([0, wx])
    try:
        wx = sum([x * y for x, y in zip(posi_vec, pot_vec)])
    except TypeError:
        print(test_id)
    except UnboundLocalError:
        print(test_id)
    wx_list.append([1, wx])

    ####  write raw wx data to a file  ####
    wx_list2 = copy.deepcopy(wx_list)
    for item in wx_list2:
        item.insert(0, test_id)
    df_result_sorted = pd.DataFrame(wx_list, columns=['p_or_n', 'wx']).sort_values('wx', ascending=True)

    # find the ranking of the positive
    i = 1
    rank = ""
    for index, row in df_result_sorted.iterrows():
        if row['p_or_n'] == 1:
            rank = i
            break
        else:
            i += 1
    # print(f'{test_id}:{rank}')
    return rank


def get_id(negafile):
    if '_h_pi_' in negafile:  # 4ohy_A_B,EM,0,0
        set_id = negafile.split('/')[-1].replace('.csv', '')
    elif 'perez_bb' in negafile:
        ele = negafile.split('/')
        set_id = f'perez_bb_{ele[-1].replace(".out", "")}'
    else:  # Zou_bb_1C0A /gs/hs0/tga-science/kimura/RNPopt/data/benchmark/non_native_combined_vecs/Zou/bb/2ANR.out
        ele = negafile.split('/')
        set_id = f'{ele[9]}_{ele[10]}_{ele[11].replace(".out", "")}'
    return set_id


# read a file, foldnum, and cpu id and returns a list of id
def read_all_id(j, input_path):  # j: cpu num
    df = pd.read_csv(input_path)
    id_list_all = df.values.tolist()
    batchsize = int(len(id_list_all) / np) + 1
    if j == np - 1:
        batch_list = id_list_all[j * batchsize:]
    else:
        batch_list = id_list_all[j * batchsize:(j + 1) * batchsize]
    return batch_list


# a function executed at each cpu
#     - read nega and posi path
#     - return avg rank sum
def calc_dots(arg_list):  # init_vec, fold_num, input_path
    j = int(multiprocessing.current_process().name.split('-')[1])  # 1-20 when np is 20
    j = (j - 1) % np  # cpu number
    # prepare id_list
    # i = arg_list[1]  # fold num [init_vec, i, inputpath]
    init_vec = arg_list[0]
    input_path = arg_list[1]
    train_list = remove_remove_id2(read_all_id(j, input_path))

    rank_sum = 0
    for sublist in train_list:
        nega_file = replace_for_t3(sublist[0])

        set_id = get_id(nega_file)
        if '.DS' in set_id:
            continue
        elif 'natives' in set_id:
            continue
        posi_file = replace_for_t3(sublist[1])
        df_nega = pd.read_csv(nega_file)
        df_posi = pd.read_csv(posi_file)
        if '_h_pi_' not in nega_file:
            df_posi.drop('all_chains', axis=1, inplace=True)
        rank_sum += apply_mean_final(set_id, init_vec, df_nega, df_posi)
    return [rank_sum, len(train_list)]


# object function, multiprocessing calcdots
def get_avg(init_vec, logfile, inputpath):  # i : fold number
    import datetime
    from multiprocessing import Pool

    init_vec_repeat = []
    for k in range(np):
        init_vec_repeat.append([init_vec, inputpath])

    with Pool(np) as p:
        result = p.map(calc_dots, init_vec_repeat)  # [rank_sum, len(train_list)]
    avgrank = sum([x[0] for x in result])/sum([x[1] for x in result])
    # avgrank = sum(result) / len(result)
    dstm = datetime.datetime.now()
    with open(logfile, 'a') as fo:
        fo.writelines(str(avgrank) + ":" + str(dstm) + ":" + str(init_vec.tolist()) + '\n')
    return avgrank


# call cmaes for each fold
def main(inp_path, o_dir, subset_n, previous_log_file=None):
    import cma
    sd0 = 0.5
    log_file = f'{o_dir}cmaes_log_all_subset{subset_n}_{current_date}.txt'
    with open(log_file, 'w') as f:
        pass
    if previous_log_file:
        init_pot = get_previous_pot(previous_log_file)
        sd0 = 0.01
    else:
        init_pot = [0.01] * 152
    cma.CMAEvolutionStrategy(init_pot, sd0).optimize(get_avg, iterations=900, args=[log_file, inp_path])


# At main, only the initial vec is calculated
# command eg.: python N1_cmaes_eval4.py input_path out_dir subset_num foldnum
# out_dir = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval4/"
# subset_num = 1
# input_path = "/Users/mac/Documents/Optimize_all_data/data/ecr2_and_eye/all_path_list_no_uu2_137.csv"
if __name__ == "__main__":
    import sys
    input_path = sys.argv[1]
    out_dir = sys.argv[2]
    subset_num = sys.argv[3]
    if len(sys.argv) == 5:
        pre_result_path = sys.argv[4]
        main(input_path, out_dir, subset_num, pre_result_path)
    else:
        main(input_path, out_dir, subset_num)
