'''

This script counts the XML tags different ontologies uses, to find the distribution of each tag. We are storing the result in pickle format,

'tag.p' contains the number of times each tag appears in all the ontologies

'files.p' contains how many unique tags appear in each ontology file

'tagsFile.p' contains the list of file each tag appeared in



We also generate excel files to store the result for data analysis,

'tags.xlsx' have two columns, the first column is the name of the tag and the second is the total number of times the tag appeared in all 
ontologies

'file.xlsx' have two columns, the first column is the file name and the second column is the count of total number of unique tags appeared 
in that file.


It reads the ontologies from the source directory 'ontology_set'

'''

from bs4 import BeautifulSoup
import pickle
import os
import operator
import xlsxwriter

# source directory
file_from='ontology_set'

# builds the dictionaries
def generate_tables(filename,tagList,tags,files,tagsFile):
	tagList = list(set(tagList))
	files[filename]=len(tagList)

	for tagElem in tagList:
		if tagElem not in tags.keys() :
			tags[tagElem]=1
			tagsFile[tagElem]=[]
			tagsFile[tagElem].append(filename)
		else : 
			tags[tagElem]=tags[tagElem]+1
			tagsFile[tagElem].append(filename)

# counts the tags if they are defined under annotation property tag
def annotation_property(tree,tagList):
	node = tree.find('ontology')
	if (node):
		children = node.findChildren()
		if (children):
			for child in children:
				if(child.name=='annotation'):
					grandchildren=child.findChildren()
					if(grandchildren):
						for greatgrandchildren in grandchildren:
							node1=greatgrandchildren.find("annotationproperty",{'abbreviatediri':True})
							if(node1):
								tagList.append(greatgrandchildren['abbreviatediri'])
							#if(greatgrandchildren.name=="annotationproperty"):
							#	if (greatgrandchildren['abbreviatediri']):

# counts the tags in each ontology file								
def parsing(filename,tags,files,tagsFile):
	# read the file
	infile = open(os.path.join(file_from, filename),"r")
	contents = infile.read()
	tagList = []
	# build a tree of the tags and search for ontology tag
	tree = BeautifulSoup(contents,'lxml')
	node = tree.find('owl:ontology')

	if(node):
	    children = node.findChildren()
	    for child in children:
			tagList.append(child.name)
	else : # incase the ontology, defines the tags under annotation property tags
		annotation_property(tree,tagList)
		
	generate_tables(filename,tagList,tags,files,tagsFile)

# generates excel files from the dictionaries
def xlsx_file(filename,listname):
	workbook = xlsxwriter.Workbook(os.path.join('excel_files', filename))
	worksheet = workbook.add_worksheet()
	row=0
	col=0

	for i in range(0,len(listname)):
	    row+=1
	    worksheet.write(row, col, listname[i][0])
	    worksheet.write(row, col+1,listname[i][1] )

	workbook.close()

# stored the dictionaries in pickle format in 'pickle' directory 
def pickle_files(filename,listname):
	with open(os.path.join('pickle', filename), 'wb') as f:
	    pickle.dump(listname, f)

# prints the dictionaries
def print_func(tags,files,tagsFile):
	print '\n'+'Count of each tag'+'\n'
	print tags 
	print '\n'+'Tags present in respective files '+'\n'
	print(tagsFile)
	print '\n'+'Total tags in each file'+'\n'
	print files

def main():
	tags = {}
	tagsFile = {}
	files={}
	# read each ontology file from the source directory 
	for filename in os.listdir(file_from):
	    parsing(filename,tags,files,tagsFile)
	# sorts the dictionaries with the most popular tags at the top
	tags=sorted(tags.items(), key=operator.itemgetter(1),reverse=True)
	files=sorted(files.items(), key=operator.itemgetter(1),reverse=True)

	xlsx_file('tags.xlsx',tags)
	xlsx_file('files.xlsx',files)


	pickle_files('tags.p',tags)
	pickle_files('tagsFile.p',tagsFile)
	pickle_files('files.p',files)

	print_func(tags,files,tagsFile)

if __name__=='__main__':
	main()