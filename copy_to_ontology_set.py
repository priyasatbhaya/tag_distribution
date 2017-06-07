'''

This script copies unique ontologies listed in 'file_dict' dictionary from the source directory to the destination directory.

'''

from bs4 import BeautifulSoup
import pickle
import os
import shutil

# source directory
file_from ='all_ontologies'
# destination directory
file_to = 'ontology_set'

# function to copy files
def copy_files(file_dict):
	# for each URI copies the corresponding file
	for key in file_dict.keys():
		shutil.copy2(os.path.join(file_from, file_dict[key]), os.path.join(file_to, file_dict[key]))

def main():
	#reads 'file_dict.p'
	if os.path.isfile(os.path.join('pickle','file_dict.p')):
		with open(os.path.join('pickle','file_dict.p'), 'rb') as f:
			file_dict=pickle.load(f)
	else : file_dict = {}

	copy_files(file_dict)

	print file_dict

if __name__=='__main__':
	main()