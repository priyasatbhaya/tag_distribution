from bs4 import BeautifulSoup
import pickle
import os
import shutil

def copy_files(file_dict):
	for key in file_dict.keys():
		shutil.copy2(os.path.join('all_ontologies', file_dict[key]), os.path.join('ontology_set', file_dict[key]))

def parsing(filename,file_dict):
	infile = open(os.path.join('all_ontologies', filename),"r")
	contents = infile.read()
	tree = BeautifulSoup(contents,'lxml')
	node = tree.find('rdf:rdf',{'xml:base':True})
	if(node):
	   	file_dict[node['xml:base']]=filename

def main():
	file_dict = {}

	for filename in os.listdir('all_ontologies'):
	    parsing(filename,file_dict)

	copy_files(file_dict)

	print file_dict

	with open(os.path.join('pickle','file_dict.p'), 'wb') as f:
	    pickle.dump(file_dict, f)


if __name__=='__main__':
	main()