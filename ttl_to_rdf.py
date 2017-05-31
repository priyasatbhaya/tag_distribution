import os

for filename in os.listdir('ttl'):
	newname=filename[:-4]
	command="rdfcat -out rdf %s > %s.rdf" % (os.path.join('ttl',filename),newname)
	os.system(command)