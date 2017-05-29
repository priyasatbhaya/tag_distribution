import httplib2
import urllib
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()

cookies='c24696abaf71e3dbacdb0f681d1bab0a=6592cc0a591ba8e587771388401756a3; expires=Tuesday, 30 May 2017 at 15:14:04; path=/,mosvisitor=1'

headers = {'Cookie': cookies}

thefile = open('test.txt', 'w')
array=[]
for i in range(1,992):
	url='http://swoogle.umbc.edu/2006/index.php?option=com_frontpage&service=search&queryType=search_swd_ontology&searchString=rdf&searchStart='+str(i)
	status, response = http.request(url, 'GET', headers=headers)
	tree = BeautifulSoup(response,'lxml')
	node = tree.find_all('a')
	for nodes in node:
		if(nodes.has_attr('class')):
			if(nodes['class']==['external']):
				array.append(nodes['href'])
	i=i+10;

a=set(array)
for item in a:
	thefile.write("%s\n" % item)
