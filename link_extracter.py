'''

This script extracts all external(download) links from Swoogle website for all the pages from 1-100 and stores it in a text file 'links.txt'.
The we wget the text file to download all the files from the extracted links to a given directory from the terminal with the command

cd to the directory where you want to download the files
wget -t 1 --timeout=60 -i links.txt

'''

import httplib2
import urllib
from bs4 import BeautifulSoup

http = httplib2.Http()

# change the cookie as per your session
cookies='c24696abaf71e3dbacdb0f681d1bab0a=6592cc0a591ba8e587771388401756a3; expires=Tuesday, 30 May 2017 at 15:14:04; path=/,mosvisitor=1'

headers = {'Cookie': cookies}
# destination file
thefile = open('links.txt', 'w')
array=[]

for i in range(1,992):
	# the search url
	url='http://swoogle.umbc.edu/2006/index.php?option=com_frontpage&service=search&queryType=search_swd_ontology&searchString=rdf&searchStart='+str(i)
	# http request
	status, response = http.request(url, 'GET', headers=headers)
	# builds a tree and finds all external links
	tree = BeautifulSoup(response,'lxml')
	node = tree.find_all('a')
	for nodes in node:
		if(nodes.has_attr('class')):
			if(nodes['class']==['external']):
				array.append(nodes['href'])
	i=i+10;

# removes dublicate elements
a=set(array)
# write all the links in the 'links.txt' file
for item in a:
	thefile.write("%s\n" % item)
