from bs4 import BeautifulSoup
import pickle
import os
import shutil

file_from ='all_ontologies'
file_to = 'ontology_set'

def copy_files(file_dict):
	for key in file_dict.keys():
			shutil.copy2(os.path.join(file_from, file_dict[key]), os.path.join(file_to, file_dict[key]))

def main():
	if os.path.isfile(os.path.join('pickle','file_dict.p')):
		with open(os.path.join('pickle','file_dict.p'), 'rb') as f:
			file_dict=pickle.load(f)
	else : file_dict = {}

	copy_files(file_dict,files)

	print file_dict

if __name__=='__main__':
	main()