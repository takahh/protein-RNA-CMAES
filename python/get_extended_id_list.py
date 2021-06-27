# ----------------------------------------------------------
# returns id list of extended data set
# < ECR 2 within Curtis data
# ----------------------------------------------------------


def get_extended_id_list_cq(remove_list):
    # ----------------------------------------------------------
    # import
    # ----------------------------------------------------------
    import os

    # ----------------------------------------------------------
    # constants
    # ----------------------------------------------------------
    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    path1 = script_dir.replace("python", "data/pdbid_list_lt2_Curtis_PISCES_CQ_novirus_shuffled.csv")

    # ----------------------------------------------------------
    # functions
    # ----------------------------------------------------------

    # ----------------------------------------------------------
    # main
    # ----------------------------------------------------------

    alllist = []
    with open(path1) as f:
        idlist = f.readline().split(',')
        for item in idlist:
            if item[0:4].lower() not in remove_list:
                if item == '':
                    continue
                item = f'{item[0:4].lower()}{item[4:8]}'
                alllist.append(item)
    return alllist

