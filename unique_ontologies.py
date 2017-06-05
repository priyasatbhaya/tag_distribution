'''

This script is used to identify the unique ontologies from a collection of ontologies, the ontologies are identified as unique on the basis
of its URI's this information is stored in a dictionary 'file_dict' with URI as the key and filename as the value, we store only one filename
for each URI.

file_from is the directory from where we read the ontology collection.
file_to is the directory where we store the unique ontologies.

We store 'file_dict' as 'file_dict.p' in 'pickle' directory.

'''

from bs4 import BeautifulSoup
import pickle
import os
import shutil

# source directory
file_from ='all_ontologies'
# destination directory
file_to = 'ontology_set'

def parsing(filename,file_dict):
	# reads each ontology file
	infile = open(os.path.join(file_from, filename),"r")
	contents = infile.read()
	# builds a tree
	tree = BeautifulSoup(contents,'lxml')
	# search for xml:base
	node=tree.find('rdf:rdf',{'xml:base':True})
	if (node):
		file_dict[node['xml:base']]=filename
	if node is None:
		node=tree.find('ontology',{'xml:base':True})
		if(node):
			file_dict[node['xml:base']]=filename
	if node is None:
		node=tree.find('owl:ontology',{'xml:base':True})
		if(node):
			file_dict[node['xml:base']]=filename
	if node is None :
		node=tree.find('owl:ontology',{'rdf:about':True})
		if(node):
			file_dict[node['rdf:about']]=filename
	if node is None:
		node = tree.find('rdf:description',{'rdf:about':True})
		if(node):
			x=node['rdf:about'].split('#')[0]+'#'
			file_dict[x]=filename

def main():
	#checks if file_dict exists
	if os.path.isfile(os.path.join('pickle','file_dict.p')):
		with open(os.path.join('pickle','file_dict.p'), 'rb') as f:
			file_dict=pickle.load(f)
	else : file_dict = {}

	#reads all files in the source directory 
	for filename in os.listdir(file_from):
		parsing(filename,file_dict)

	print file_dict

	#pickle 'file_dict' as 'file_dict.p' in 'pickle' directory 
	with open(os.path.join('pickle','file_dict.p'), 'wb') as f:
	    pickle.dump(file_dict, f)

if __name__=='__main__':
	main()