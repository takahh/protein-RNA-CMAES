# ----------------------------------------------------------
# this code is for optimizing potentials with some
# metaheuristics with extended data set up to ECR 2
# ----------------------------------------------------------

# ----------------------------------------------------------
# import
# ----------------------------------------------------------
import copy
import numpy as np
import pandas as pd
import multiprocessing
from python.utilities import get_train_ids_from_all

# ----------------------------------------------------------
# constant
# ----------------------------------------------------------
base_path = "/gs/hs0/tga-science/kimura/RNPopt/data/"
vec_path = f'{base_path}combined_h_pi_vec/'
positive = f'{base_path}combined_h_pi_vec/natives.csv'
log_file = f'{base_path}result/eval3/cmaes_log.txt'


def give_me_np():
    return 56


def calc_dots(arg_list):
    np = give_me_np()
    j = int(multiprocessing.current_process().name.split('-')[1]) # 1-20 when np is 20
    j = (j -1) % np

    df_posi = pd.read_csv(positive)

    # prepare id_list
    init_vec = arg_list[0]

    id_list_train = get_train_ids_from_all()
    # decide batch list
    batchsize = int(len(id_list_train)/np) + 1
    if j == np - 1:
        batch_list = id_list_train[j * batchsize:]
    else:
        batch_list = id_list_train[j * batchsize:(j + 1) * batchsize]    # make a dictionary of nega_df
    df_nega_dic = {}
    for test_id in batch_list:
        df = pd.read_csv(vec_path + test_id + '.csv')
        df_nega_dic[test_id] = df

    rank_sum = 0
    k = 0
    for test_id in batch_list:
        rank_sum += apply_mean_cq(test_id, init_vec, df_nega_dic, df_posi, k)
        k += 1
    return rank_sum


def apply_mean_cq(test_id, pot_vec, df_nega_dic, df_posi, k):
    try:
        df_nega = df_nega_dic[test_id]
    except FileNotFoundError:
        print('not found')
    df_nega_target = df_nega
    try:
        target_posi_list = df_posi[df_posi['vec_id'] == test_id].values.tolist()[0]
        posi_vec = target_posi_list[2:82] + target_posi_list[118:154]
    except IndexError:
        print('INDEX ERROR')
        print(test_id)
        print(df_posi[df_posi['vec_id'] == test_id].values.tolist())

    wx_list = []

    # calcluate wx and make a dataframe
    for index, row in df_nega_target.iterrows():
        # n_vec = row.tolist()[2:154]
        n_vec = row.tolist()[2:82] + row.tolist()[118:154]
        wx = np.dot(n_vec, pot_vec)
        wx_list.append([0, wx])
    wx = np.dot(pot_vec, posi_vec)
    wx_list.append([1, wx])

    ####  write raw wx data to a file  ####
    wx_list2 = copy.deepcopy(wx_list)
    for item in wx_list2:
        item.insert(0, test_id)

    # sort by wx values
    df_result_sorted = pd.DataFrame(wx_list, columns=['p_or_n', 'wx']).sort_values('wx', ascending=True)

    # find the ranking of the positive
    i = 1
    for index, row in df_result_sorted.iterrows():
        if row['p_or_n'] == 1:
            rank = i
            break
        else:
            i += 1
    print(f'{k}-{test_id}:{rank}')
    return rank


def get_avg_all(init_vec):
    print(f'*************')
    import datetime
    from multiprocessing import Pool

    np = give_me_np()
    with Pool(np) as p:
        init_vec_repeat = []
        for k in range(np):
            init_vec_repeat.append([init_vec])
        result = p.map(calc_dots, init_vec_repeat)

    avgrank = sum(result)/len(get_train_ids_from_all())
    dstm = datetime.datetime.now()
    with open(log_file, 'a') as fo:
        fo.writelines(str(avgrank) + ":" + str(dstm) + ":" + str(init_vec.tolist()) + '\n')
    print(avgrank)
    return avgrank


def main():
    import cma
    init_pot = [0.01]*116
    with open(log_file, 'w') as f:
        pass
    cma.CMAEvolutionStrategy(init_pot, 0.5).optimize(get_avg_all, iterations=300)


if __name__ == "__main__":
    main()
