# -------------------------------------------------------------------
# this code score benchmarks with all the best (avg rank 1) potential sets
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# import
# -------------------------------------------------------------------
import pandas as pd
import copy
import numpy as np
import multiprocessing
import ast
import os, sys

# -------------------------------------------------------------------
# constant
# -------------------------------------------------------------------
native_vec_file = '/Volumes/HDCZ-UT/Research/RNP/Extra_Test/native/combined_vec.csv'
non_native_file = '/Volumes/HDCZ-UT/Research/RNP/Extra_Test/non_native_combined_vecs/perez/ub/1B7F.out'
result_dir = '/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/ranking/'
pot_file = '/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/best_pot.csv'

# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


def get_nega_df(pdbid, name, btype):
    path = non_native_file.replace('perez', name).replace('/ub/', f'/{btype}/').replace('1B7F', pdbid)
    df = pd.read_csv(path)
    return df


def get_id_list(name2, btype2):
    id_list = []
    with open(native_vec_file) as f:
        for lines in f.readlines():
            keyword = f'{name2}_{btype2}_'
            ele = lines.split(',')
            if keyword in ele[0]:
                id_list.append(ele[0].replace(keyword, ''))
    return id_list


def score_poses(test_id, pot_vec, df_nega, dfposi, name, btype):
    # ----------------------------------------------------------
    # main
    # ----------------------------------------------------------
    df_nega_target = df_nega
    # pd.concat([df, df['row'].str.partition(' ')[[0, 2]]], axis=1)
    # pd.concat([dfposi, dfposi['vec_id'].str.partition('_')[['name', 'btype', 'pid']]], axis=1)
    df = pd.concat([dfposi, dfposi['vec_id'].str.split('_', expand=True)], axis=1)
    try:
        # posilist = df[(df[2] == test_id) & (df[0] == name) & (df[1] == btype)]
        posilist = df[(df[2] == test_id) & (df[0] == name) & (df[1] == btype)].values[0]
        posi_vec = list(posilist[1:81]) + list(posilist[117:153])
    except IndexError:
        print('INDEX ERROR')
        print(test_id)

    wx_list = []

    # calcluate wx and make a dataframe
    for index, row in df_nega_target.iterrows():
        blist = row.tolist()
        n_vec = blist[1:81] + blist[117:153]
        # wx = sum([x * y for x, y in zip(n_vec, pot_vec)]) # use numpy?
        wx = np.dot(n_vec, pot_vec)
        wx_list.append([0, wx])
    # wx = sum([x * y for x, y in zip(posi_vec, pot_vec)])
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
            # fo.writelines(test_id + ',' + str(rank) + ',')
            break
        else:
            i += 1
    print(f'{test_id}:{rank}')
    return rank


def proceed(name, btype, pot, df_posi, fo):
    idlist = get_id_list(name, btype)
    for pdbid in idlist:
        nega_df = get_nega_df(pdbid, name, btype)
        rank = score_poses(pdbid, pot, nega_df, df_posi, name, btype)
        fo.writelines(f'{pdbid},{rank}\n')


def get_pot():
    pot_list = []
    with open(pot_file) as f:
        for lines in f.readlines():
            pot_list.append([float(x) for x in lines.replace("\n", "").split(',')])
    return pot_list


def get_df_posi():
    df = pd.read_csv(native_vec_file)
    df.drop(columns=['all_chains', 'exp'], inplace=True)
    return df


def score_ranking(arg_list):
    i = 0
    cpu_num = arg_list[0]
    poten_list = arg_list[1]
    eachnum = arg_list[2]
    for pot in poten_list:
        print("eachnum")
        print(eachnum)
        print("cpu")
        print(cpu_num)
        pot_index = eachnum * cpu_num + i
        df_posi = get_df_posi()
        for name in ['perez', 'Zou']:
            if name == 'perez':
                for btype in ['ub', 'uu']:
                    output_path = f'{result_dir}{name}_{btype}_{pot_index}_rankings.csv'
                    if os.path.isfile(output_path):
                        continue
                    with open(output_path, 'w') as fo:
                        proceed(name, btype, pot, df_posi, fo)
            else:
                for btype in ['bb', 'uu']:
                    output_path = f'{result_dir}{name}_{btype}_{pot_index}_rankings.csv'
                    if os.path.isfile(output_path):
                        continue
                    with open(output_path, 'w') as fo:
                        proceed(name, btype, pot, df_posi, fo)
        i += 1


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    n = 12
    potlist = get_pot()
    pot_num = len(potlist)  # 894
    each_num = int(pot_num/12) + 1  # 77
    pot_index_list = []
    for i in range(12):
        if i != 11:
            pot_index_list.append([i, potlist[each_num*i: each_num*(i+1)], each_num])
        else:
            pot_index_list.append([i, potlist[each_num*i: pot_num], each_num])

    with multiprocessing.Pool(n) as p:
        p.map(score_ranking, pot_index_list)
