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

        tagList = list(set(tagList))
      
        for tagElem in tagList:
            if tagElem not in tags.keys() :
                tags[tagElem]=1
                tagsFile[tagElem]=[]
                tagsFile[tagElem].append(filename)
            else : 
                tags[tagElem]=tags[tagElem]+1
                tagsFile[tagElem].append(filename)

#print(tags)
#print(tagsFile)

pickle.dump(tags,open("totalTags.p","wb"))
pickle.dump(tagsFile,open("tagsFile.p","wb"))
