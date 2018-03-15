# DBLP Parser

This application parses the DBLP data set and generates multiple CSV files as an output:

* Title | Author | Name of the conference
* Author | Publication Title A | Publication Title B | ...
* Author | Journal A | Journal B | ...
* Author | Phd Title 
* Author | Book


## Dependencies

* Java SDK 8
* Maven 


## Building the application

* mvn clean install


## Getting the source data

* wget http://dblp.uni-trier.de/xml/dblp.xml.gz
* gunzip dblp.xml.gz
* mv dblp.xml input


## Run the application

* ./run.sh

