# ----------------------------------------------------------
# this code is for a function that provides
# a list of chain pair ids that have a range of contacts ratio
# ----------------------------------------------------------


def filter_by_contacts(contacts_ratio):
	# ----------------------------------------------------------
	# import
	# ----------------------------------------------------------
	import pandas as pd
	import os

	# ----------------------------------------------------------
	# constants
	# ----------------------------------------------------------
	script_path = os.path.abspath(__file__)
	script_dir = os.path.split(script_path)[0]
	file = script_dir.replace("python", "data/non_redun_positives.txt")

	# ----------------------------------------------------------
	# functions
	# ----------------------------------------------------------

	# ----------------------------------------------------------
	# main
	# ----------------------------------------------------------
	df = pd.read_csv(file)
	id_list = df[df['all_chains'].astype(float) < contacts_ratio]['vec_id'].tolist()
	return id_list