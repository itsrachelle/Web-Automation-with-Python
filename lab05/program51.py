import urllib

from BeautifulSoup import BeautifulSoup as Soup
 
url = "http://www.cdm.depaul.edu/odata/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20'A'%20and%20SubjectId%20eq'CSC'"

ur = urllib.urlopen(url).read()

of = open("CSC.xml", "wb")

of.write(ur)

of.close()


####

of2 = open("CSC.properties.1.xml","wb")

of3 = open("CSC.xml", "r")


soup = Soup(of3)

for m  in soup.findAll('m:properties'):
    of2.write( str(m) )
    break

of2.close()

of3.close()
