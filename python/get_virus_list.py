# ----------------------------------------------------------
# this code is for providing a list of virus capsid
#
# ----------------------------------------------------------


def get_list(contact_limit=2):
	# ----------------------------------------------------------
	# import
	# ----------------------------------------------------------
	import pandas as pd
	from python.filter_by_contacts import filter_by_contacts
	import os


	# ----------------------------------------------------------
	# constants
	# ----------------------------------------------------------

	script_path = os.path.abspath(__file__)
	script_dir = os.path.split(script_path)[0]
	cif = script_dir.replace("python", "data/virus/xray_cif.csv")

	script_dir = os.path.split(script_path)[0]
	pdb = script_dir.replace("python", "data/virus/xray_pdb.csv")

	virus_id_list_to_remove = []

	# ----------------------------------------------------------
	# preprocess
	# ----------------------------------------------------------
	df1 = pd.read_csv(cif)
	df2 = pd.read_csv(pdb)
	cif_list = df1.id.to_list()
	pdb_list = df2.id.to_list()
	all_virus_list = cif_list + pdb_list

	# ----------------------------------------------------------
	# main
	# ----------------------------------------------------------
	contact_zero_list = filter_by_contacts(contact_limit)
	short_list = [x[0:4] for x in contact_zero_list]
	for item in all_virus_list:
		if item in short_list:
			virus_id_list_to_remove.append(item)
	return virus_id_list_to_remove