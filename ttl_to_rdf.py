'''

We are using apache-jena-3.3.0, please download it and follow the instructions in the website to configure it with your system.

This script calls the jena rdfcat for all files in the source directory to convert ontologies from ttl or n3 format to rdf format and 
stores them in the current directory.

'''

import os

# source directory 
file_from='ttl'

for filename in os.listdir(file_from):
	# name of the convert rdf format file
	newname=filename[:-4]
	# converts ttl ontology files to rdf 
	# change ttl to n3 in case you want n3 to rdf conversions
	command="rdfcat -out rdf %s > %s.rdf" % (os.path.join('ttl',filename),newname)
	os.system(command)