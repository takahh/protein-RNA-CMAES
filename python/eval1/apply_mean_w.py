# ----------------------------------------------------------
# this code is for testing ** mean ** w as solution
# 1. take the mean w as a list from the file
# 2. multiply it to 3600 dekois and 1 native
# 3. see how largest the native score is
# 4. compare the #3 results with the svm results
#    (maybe make a plot)
# ----------------------------------------------------------


def apply_mean_cq(test_id, pot_vec, df_nega_dic, df_posi):
    # ----------------------------------------------------------
    # import
    # ----------------------------------------------------------
    import pandas as pd
    import math, csv, copy
    import numpy as np
    from python.get_extended_id_list import get_extended_id_list_cq

    # ----------------------------------------------------------
    # main
    # ----------------------------------------------------------
    # with open(ranking_results, 'a') as fo:
    try:
        df_nega = df_nega_dic[test_id]
    except FileNotFoundError:
        print('not found')
    df_nega_target = df_nega
    try:
        posi_vec = df_posi[df_posi['vec_id'] == test_id].values.tolist()[0][2:82]
    except IndexError:
        print('INDEX ERROR')
        print(test_id)
        print(df_posi[df_posi['vec_id'] == test_id].values.tolist())

    # ----------------------------------------------------------
    # get w mean/median
    # ----------------------------------------------------------
    # mean_w = pol2car(mean_angles)

    wx_list = []

    # calcluate wx and make a dataframe
    for index, row in df_nega_target.iterrows():
        n_vec = row.tolist()[2:82]
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

    # with open(ranking_results.replace('ranking_', 'scores_'), 'a') as fo2:
    # 	writer = csv.writer(fo2)
    # 	writer.writerows(wx_list2)

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
