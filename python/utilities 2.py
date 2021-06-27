import pandas as pd

def give_me_np():
    return 12


# def get_fold_num():
#     return 0


def get_all_list():
    # path_file = '/Users/mac/Documents/Optimize_all_data/data/all_path_list.csv'
    path_file = '/Users/mac/Documents/Optimize_all_data/data/all_path_list_no_uu.csv'
    df = pd.read_csv(path_file)
    pathlist = df.values.tolist()
    return pathlist


def remove_remove_id(original_list):
    oldlist = original_list
    remove_list = ["1M8V", "1G1X", "3HHZ", "3HL2", "2JGE", "1HVU"]
    virus_list = ['2QUX', '2AZ0', '1SJ3', '2ZKO', '1R9F', '2BU1', '3OL9', '2QUX', '2AZ0']
    for item2 in original_list:
        for item in remove_list:
            if item.lower() in item2[0] or item.upper() in item2[0]:
                original_list.remove(item2)
        for item in virus_list:
            if item.lower() in item2[0] or item.upper() in item2[0]:
                original_list.remove(item2)
    print(f'{len(oldlist)} to {len(original_list)}')
    return original_list


def remove_remove_id2(original_list):
    remove_list = ["1M8V", "1G1X", "3HHZ", "3HL2", "2JGE", "1HVU"]
    virus_list = ['2QUX', '2AZ0', '1SJ3', '2ZKO', '1R9F', '2BU1', '3OL9', '2QUX', '2AZ0']
    new_list = []
    for item2 in original_list:
        found = 0
        for item in remove_list:
            if item.lower() in item2[0] or item.upper() in item2[0]:
                found = 1
        for item in virus_list:
            if item.lower() in item2[0] or item.upper() in item2[0]:
                found = 1
        if found == 0:
            new_list.append(item2)
    # print(f'{len(original_list)} to {len(new_list)}')
    return new_list


def get_id_list_all():
    from get_virus_list import get_list
    from get_extended_id_list import get_extended_id_list_cq
    virus_list = get_list()
    id_list_all = get_extended_id_list_cq(virus_list)
    id_list_all.remove(remove_id())
    return id_list_all


def get_train_ids(fold_num):
    folding = 5
    id_list_all = get_id_list_all()
    id_list_all = list(set(id_list_all)) # remove
    # fold using constant valid number i(/5)
    eachlen = int(len(id_list_all)/folding)
    if fold_num != folding - 1:
        sub_id_list_to_remove = id_list_all[fold_num * eachlen: (fold_num + 1) * eachlen]
    else:
        sub_id_list_to_remove = id_list_all[fold_num * eachlen: len(id_list_all)]
    # make a 4/5 list
    id_list_train = tuple(list(set(id_list_all) - set(sub_id_list_to_remove)))
    return id_list_train


def get_test_ids(fold_num):
    folding = 5
    id_list_all = get_id_list_all()
    id_list_all = list(set(id_list_all)) # remove repetition
    # fold using constant valid number i(/5)
    eachlen = int(len(id_list_all)/folding)
    if fold_num != folding - 1:
        sub_id_list_to_remove = id_list_all[fold_num * eachlen: (fold_num + 1) * eachlen]
    else:
        sub_id_list_to_remove = id_list_all[fold_num * eachlen: len(id_list_all)]
    # make a 1/5 list
    id_list_test = tuple(set(sub_id_list_to_remove))

    return id_list_test


def get_train_id_list(fold_num, cpu_id=''):  # writing file
    path_file = f'/Users/mac/Documents/Optimize_all_data/data/path_list/path_list_{fold_num}_no_uu.csv'
    with open(path_file, 'w') as fo:
        path_list = get_all_list()
        # length to remove
        eachlen = int(len(path_list)/5) + 1
        print(eachlen)
        # make a list to remove later
        if fold_num != 4:
            sub_id_list_to_remove = path_list[fold_num * eachlen: (fold_num + 1) * eachlen]
        else:
            sub_id_list_to_remove = path_list[fold_num * eachlen:]
        # make a 4/5 list
        id_list_train = [x for x in path_list if x not in sub_id_list_to_remove]
        for item in id_list_train:
            fo.writelines(f'{item[0]},{item[1]}\n')


def get_train_id_list_all():  # writing file
    path_file = f'/Users/mac/Documents/Optimize_all_data/data/path_list/path_list_all_no_uu.csv'
    with open(path_file, 'w') as fo:
        path_list = get_all_list()
        id_list_train = path_list
        for item in id_list_train:
            fo.writelines(f'{item[0]},{item[1]}\n')


def get_train_ids_from_all():
    id_list_all = get_id_list_all()
    id_list_all = list(set(id_list_all)) # remove
    return id_list_all


def get_test_id_list(fold_num, cpu_id=''):  # writing file
    path_file = f'/Users/mac/Documents/Optimize_all_data/data/path_list/test_path_list_{fold_num}.csv'
    with open(path_file, 'w') as fo:
        path_list = get_all_list()
        # length to remove
        eachlen = int(len(path_list)/10)
        # make a list to remove later
        if fold_num != fold_num - 1:
            sub_id_list_to_remove = path_list[fold_num * eachlen: (fold_num + 1) * eachlen]
        else:
            sub_id_list_to_remove = path_list[fold_num * eachlen: len(path_list)]
        # make a 4/5 list

        # id_list_train = [x for x in path_list if x not in sub_id_list_to_remove]
        for item in sub_id_list_to_remove:
            fo.writelines(f'{item[0]},{item[1]}\n')


def get_length(fold_num):
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/path_list/path_list_{fold_num}_no_uu.csv')
    id_list_train = remove_remove_id2(df.values.tolist())
    return len(id_list_train)


def get_length_nocv():
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/all_path_list_no_uu.csv')
    id_list_train = remove_remove_id2(df.values.tolist())
    return len(id_list_train)


def get_length_nocv2():
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/all_path_list_no_uu2.csv', header=None)
    id_list_train = df.values.tolist()
    return len(id_list_train)


def read_train_id(input_path, fold_num, j):  # j: cpu num
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/path_list/path_list_{fold_num}_no_uu.csv')
    id_list_train = df.values.tolist()
    # decide batch list
    batchsize = int(len(id_list_train)/28) + 1
    if j == 28 - 1:
        batch_list = id_list_train[j * batchsize:]
    else:
        batch_list = id_list_train[j * batchsize:(j + 1) * batchsize]
    return batch_list


def read_train_id_nocv(j):  # j: cpu num
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/all_path_list_no_uu.csv')
    id_list_train = df.values.tolist()
    # decide batch list
    batchsize = int(len(id_list_train)/12) + 1
    if j == 12 - 1:
        batch_list = id_list_train[j * batchsize:]
    else:
        batch_list = id_list_train[j * batchsize:(j + 1) * batchsize]
    return batch_list


def read_train_id_nocv_137(j):  # j: cpu num
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/all_path_list_no_uu2.csv')
    id_list_train = df.values.tolist()
    # decide batch list
    batchsize = int(len(id_list_train)/12) + 1
    if j == 12 - 1:
        batch_list = id_list_train[j * batchsize:]
    else:
        batch_list = id_list_train[j * batchsize:(j + 1) * batchsize]
    return batch_list


def return_train_id_list(fold_num):
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/path_list/path_list_{fold_num}.csv')
    id_list_train = df.values.tolist()
    return id_list_train


def read_test_id(fold_num, j):  # j: cpu num
    df = pd.read_csv(f'/Users/mac/Documents/Optimize_all_data/data/path_list/path_list_{fold_num}.csv')
    id_list_train = df.values.tolist()
    # decide batch list
    batchsize = int(len(id_list_train)/10) + 1
    if j == 10 - 1:
        batch_list = id_list_train[j * batchsize:]
    else:
        batch_list = id_list_train[j * batchsize:(j + 1) * batchsize]
    return batch_list


# chain quality bad list to the optimization on all data final
def get_bad_chain_quality_pdbid():
    filepath = '/Volumes/HDCZ-UT/Research/RNP/Extra_Test/ECR/OFF_TARGET/7.Plot.Pot/chain_quality.csv'
    df = pd.read_csv(filepath, header=None)
    return df[df[3] >= 0.3][1].tolist()


# bad ecr data for final all data optimization
def get_bad_ecr():
    bad_list = []
    # path = '/Volumes/HDCZ-UT/Research/RNP/Extra_Test/ECR/OFF_TARGET/6.VECS_AND_ECR/ecr.csv'
    path = '/Volumes/HDCZ-UT/Research/RNP/Extra_Test/ECR/OFF_TARGET/6.VECS_AND_ECR/ecr_enaergy_based.csv'
    df = pd.read_csv(path, header=None)
    df_bad = df[df[2] > 2]
    for index, rows in df_bad.iterrows():
        bad_list.append(f'{rows[0].split("_")[0]}_{rows[1]}')
    return bad_list


# get virus list data for final all data optimization
def get_virus_list():
    return ["1WNE", "2AZO", "2GIC", "2R7R", "3BSO"]


# if __name__ == '__main__':
#     print(get_bad_ecr())