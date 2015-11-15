import re

import simplejson

from BeautifulSoup import BeautifulSoup as Soup

of = open("CSC.properties.1.xml","r")

ofw = open("CSC.properties.1.json","wb")

soup = Soup(of)

dit = {}


for tags in soup.findAll(name = re.compile("^d\:\w+")):
    dit[ str(tags.name)[2:] ] = str( tags.next ) 
    
obj = dit

simplejson.dump(obj, open("CSC.properties.1.json", "w"))




