# ----------------------------------------------------------
# import
# ----------------------------------------------------------
from apply_mean_w_pi_plus import apply_mean_cq
import pandas as pd
import multiprocessing
from python.utilities import get_train_ids, give_me_np, get_train_ids_from_all
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0]

vec_path = script_dir.replace("python/eval2", "data/combined_h_pi_vec/")
script_dir = os.path.split(script_path)[0]
positive = script_dir.replace("python/eval2", "data/combined_h_pi_vec/natives.csv")

# vec_path = '/Users/mac/Documents/RNP_opt/combined_h_pi_vec/'
# positive = "/Users/mac/Documents/RNP_opt/combined_h_pi_vec/natives.csv"  # hbplus


def calc_dots(arg_list):
    # ----------------------------------------------------------
    # constants
    # ----------------------------------------------------------
    np = give_me_np()
    j = int(multiprocessing.current_process().name.split('-')[1]) # 1-20 when np is 20
    j = (j -1) % np

    # ----------------------------------------------------------
    # preprocess for argument
    # ----------------------------------------------------------
    df_posi = pd.read_csv(positive)

    # prepare id_list
    i = arg_list[1]
    init_vec = arg_list[0]
    id_list_train = get_train_ids(i)

    # decide batch list
    batchsize = int(len(id_list_train)/np) + 1
    if j == np - 1:
        batch_list = id_list_train[j * batchsize:]
    else:
        batch_list = id_list_train[j * batchsize:(j + 1) * batchsize]

    # make a dictionary of nega_df
    df_nega_dic = {}
    for test_id in batch_list:
        df = pd.read_csv(vec_path + test_id + '.csv')
        df_nega_dic[test_id] = df

    rank_sum = 0
    for test_id in batch_list:
        rank_sum += apply_mean_cq(test_id, init_vec, df_nega_dic, df_posi)
    return rank_sum



def calc_dots_all(arg_list):
    # ----------------------------------------------------------
    # constants
    # ----------------------------------------------------------
    np = give_me_np()
    j = int(multiprocessing.current_process().name.split('-')[1]) # 1-20 when np is 20
    j = (j -1) % np

    # ----------------------------------------------------------
    # preprocess for argument
    # ----------------------------------------------------------
    df_posi = pd.read_csv(positive)

    # prepare id_list
    i = arg_list[1]
    init_vec = arg_list[0]

    id_list_train = get_train_ids(i)

    # decide batch list
    batchsize = int(len(id_list_train)/np) + 1
    if j == np - 1:
        batch_list = id_list_train[j * batchsize:]
    else:
        batch_list = id_list_train[j * batchsize:(j + 1) * batchsize]

    # make a dictionary of nega_df
    df_nega_dic = {}
    for test_id in batch_list:
        df = pd.read_csv(vec_path + test_id + '.csv')
        df_nega_dic[test_id] = df

    rank_sum = 0
    for test_id in batch_list:
        rank_sum += apply_mean_cq(test_id, init_vec, df_nega_dic, df_posi)
    return rank_sum