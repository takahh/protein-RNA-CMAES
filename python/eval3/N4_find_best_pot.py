# -------------------------------------------------------------------
# this code finds representative potential set from the rankings
# by best average ranking of extra sets
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# import
# -------------------------------------------------------------------
import pandas as pd
from eval3.N3_calculate_rankings_with_all_pot_pattern import get_pot

# -------------------------------------------------------------------
# constant
# -------------------------------------------------------------------
base_path = '/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/ranking/'
# base_path = '/Users/tkimura/Desktop/t3_mnt/RNPopt/data/result/eval3/ranking/'
file1 = f'{base_path}Zou_uu__rankings.csv'
file2 = f'{base_path}Zou_bb__rankings.csv'
file3 = f'{base_path}perez_ub__rankings.csv'
file4 = f'{base_path}perez_uu__rankings.csv'
file_list = [file1, file2, file3, file4]

output = "/Users/mac/Desktop/t3_mnt/RNPopt/data/result/eval3/best_performance_pot.csv"

# -------------------------------------------------------------------
# function
# -------------------------------------------------------------------


def main():
    summary_dict = {}
    for files in file_list:

        # make four big dataframes for four subsets
        integrated_df = pd.read_csv(files.replace('__', f'_0_'), header=None)
        integrated_df.columns = [0, f'c0']
        for i in range(1, 894):
            df_new = pd.read_csv(files.replace('__', f'_{i}_'), header=None)
            df_new.columns = [0, f'c{i}']
            integrated_df = pd.merge(df_new, integrated_df, on=0)

        # instead of average, calculate sum of ranking for four sets per each plot
        for cols in integrated_df.columns:
            if cols != 0:
                if cols in summary_dict.keys():
                    summary_dict[cols] += sum(integrated_df[cols].tolist())
                else:
                    summary_dict[cols] = sum(integrated_df[cols].tolist())

    # find indices of best potentials
    min_sum = min(summary_dict.values())
    best_key_list = []
    for keys in summary_dict:
        if summary_dict[keys] == min_sum:
            best_key_list.append(keys)
    print(best_key_list)

    # write potential values to a file
    with open(output, 'w') as fo:
        for best_key in best_key_list:
            best_pot_num = best_key.replace("c", "")
            best_pot = get_pot()[int(best_pot_num)]
            fo.writelines(f"{best_pot_num}:")
            for item in best_pot:
                fo.writelines(f'{item},')
            fo.writelines('\n')


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    main()