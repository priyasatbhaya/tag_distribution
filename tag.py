from bs4 import BeautifulSoup
import pickle
import os
import operator
import xlsxwriter

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
									
def parsing(filename,tags,files,tagsFile):
	infile = open(os.path.join('ontology_set', filename),"r")
	contents = infile.read()
	tagList = []
	tree = BeautifulSoup(contents,'lxml')
	node = tree.find('owl:ontology')

	if(node):
	    children = node.findChildren()
	    for child in children:
			tagList.append(child.name)
	else :
		annotation_property(tree,tagList)
		
	generate_tables(filename,tagList,tags,files,tagsFile)

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

def pickle_files(filename,listname):
	with open(os.path.join('pickle', filename), 'wb') as f:
	    pickle.dump(listname, f)

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

	for filename in os.listdir('ontology_set'):
	    parsing(filename,tags,files,tagsFile)

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