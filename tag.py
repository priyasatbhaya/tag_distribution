from bs4 import BeautifulSoup
import pickle
import cPickle as pickle
import os

tags = {}
tagsFile = {}

for filename in os.listdir('ontology_files'):
    infile = open(os.path.join('ontology_files', filename),"r")
    contents = infile.read()

    tagList = []

    tree = BeautifulSoup(contents,'lxml')
    node = tree.find('owl:ontology')

    if(node):
        children = node.findChildren()

        for child in children:
            tagList.append(child.name)

    else :
    	node = tree.find('ontology')
    	if (node):
        	children = node.findChildren()
        	for child in children:
        		if(child.name=='annotation'):
	        		grandchildren=child.findChildren();
	        		if(grandchildren):
	        			for greatgrandchildren in grandchildren:
	        				if(greatgrandchildren.name=="annotationproperty"):
	        					tagList.append(greatgrandchildren['abbreviatediri'])

    tagList = list(set(tagList))
      
    for tagElem in tagList:
        if tagElem not in tags.keys() :
            tags[tagElem]=1
            tagsFile[tagElem]=[]
            tagsFile[tagElem].append(filename)
        else : 
            tags[tagElem]=tags[tagElem]+1
            tagsFile[tagElem].append(filename)

print(tags)
print "\n"
print(tagsFile)

with open(os.path.join('pickle', 'totalTags.p'), 'wb') as f:
    pickle.dump(tags, f)

with open(os.path.join('pickle', 'tagsFile.p'), 'wb') as f:
   pickle.dump(tagsFile, f)