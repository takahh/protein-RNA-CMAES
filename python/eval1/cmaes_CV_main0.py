# ----------------------------------------------------------
# this code is for optimizing potentials with some
# metaheuristics with extended data set up to ECR 2
# ----------------------------------------------------------

from calc_dot import calc_dots
from python.utilities import get_train_ids, give_me_np
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0]
opt_log_path = script_dir.replace("python/eval1", "data/result/eval1/")


def get_avg(init_vec, i):
    print(f'{i}*************')
    import datetime
    from multiprocessing import Pool

    np = give_me_np()
    with Pool(np) as p:
        init_vec_repeat = []
        for k in range(np):
            init_vec_repeat.append([init_vec, i])
        result = p.map(calc_dots, init_vec_repeat)
        print(result)
        # Pool(processes=np, function=calc_dots(init_vec))

    avgrank = sum(result)/len(get_train_ids(i))
    print("len(get_train_ids(i))")
    print(len(get_train_ids(i)))
    dstm = datetime.datetime.now()
    log_file = f'{opt_log_path}cmaes_log_{i}.txt'
    with open(log_file, 'a') as fo:
        fo.writelines(str(avgrank) + ":" + str(dstm) + ":" + str(init_vec.tolist()) + '\n')
    print(avgrank)
    return avgrank


def main():
    import cma
    import pandas as pd
    # ----------------------------------------------------------
    # get an initial vec depending on the fold number
    # ----------------------------------------------------------
    # i = get_fold_num()

    # for i in range(0, 5):
        # def get_the_first_vec():
        #     init_pot_file = f'{opt_log_path}/cmaes_log_0_saved.txt'
        #     with open(init_pot_file) as f:
        #         for lines in f.readlines():
        #             if len(lines) > 6:
        #                 lastline = lines
        #             else:
        #                 pass
        #         print(f'lines is {lastline}')
        #         init_pot0 = lastline.split('[')[1].split(']')[0].split(',')
        #     return init_pot0

        # init_pot_file_start = '/Users/mac/Documents/RNP_opt/optimize/cmaes_2020.5.26.csv'
        # init_pot_start = pd.read_csv(init_pot_file_start)['min_angle']

        # if i == 0:
    i = 0
    init_pot = [0.01]*80
    # else:
    #     init_pot = get_the_first_vec()

    log_file = f'{opt_log_path}cmaes_log_{i}.txt'
    with open(log_file, 'w') as f:
        pass

    # ----------------------------------------------------------
    # run CMA-ES
    # ----------------------------------------------------------
    # cma.CMAEvolutionStrategy(init_pot, 0.5).optimize(get_avg, n_jobs=7)
    cma.CMAEvolutionStrategy(init_pot, 0.5).optimize(get_avg, iterations=1000, args=[i])


# At main, only the initial vec is calculated
if __name__ == "__main__":
    main()