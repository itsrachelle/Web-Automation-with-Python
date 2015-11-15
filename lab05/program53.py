from BeautifulSoup import BeautifulSoup as Soup

import simplejson

import re

f3 = open("CSC.xml","r")

soup = Soup(f3)

l = []

for m in soup.findAll('m:properties'):
    dit = {}
    for tags in m.findAll(name = re.compile("^d\:\w+")):
        dit[ str(tags.name)[2:] ] = str( tags.next )
    l += [dit]

obj = l 

simplejson.dump(obj, open("CSC.json","w"))
