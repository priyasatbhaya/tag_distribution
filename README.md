# tag_distribution
Counts the XML tags different ontologies uses, to find the distribution of each tag.

## Building the Project
We are using Python 2.7.13, if you don't have Python run the following command
```
sudo apt-get install python
```

The dependencies to be Installed as follows:
```
sudo apt-get install python-bs4 
sudo apt-get install python-lxml
sudo apt-get install python-setuptools python-dev build-essential
sudo easy_install XlsxWriter
```

## Run the Project
```
cd tag_distribution
```
Copy the ontology files '.owl|.rdf' in the 'all_ontologies' directory and run the scripts as follows
```
python unique_ontologies.py
python tag.py
```

## Result
The result is stored in pickles and excel_files directories. 
