from bs4 import BeautifulSoup
import pickle
import os
import shutil

file_from ='all_ontologies'
file_to = 'ontology_set'

def copy_files(file_dict,files):
	for key in file_dict.keys():
		if(file_dict[key] in files):
			shutil.copy2(os.path.join(file_from, file_dict[key]), os.path.join(file_to, file_dict[key]))

def parsing(filename,file_dict):
	
	infile = open(os.path.join(file_from, filename),"r")
	contents = infile.read()
	tree = BeautifulSoup(contents,'lxml')
	node = tree.find('rdf:rdf',{'xml:base':True})
	if(node):
		node=node
	else: 
		node = tree.find('ontology',{'xml:base':True})
	if(node):
	   	file_dict[node['xml:base']]=filename

def main():
	files=[]
	if os.path.isfile(os.path.join('pickle','file_dict.p')):
		with open(os.path.join('pickle','file_dict.p'), 'rb') as f:
			file_dict=pickle.load(f)
	else : file_dict = {}

	for filename in os.listdir(file_from):
		files.append(filename)
		parsing(filename,file_dict)

	copy_files(file_dict,files)

	print file_dict

	with open(os.path.join('pickle','file_dict.p'), 'wb') as f:
	    pickle.dump(file_dict, f)


if __name__=='__main__':
	main()