
import urllib 
import csv
import re


from BeautifulSoup import BeautifulSoup as Soup

co  = open("professors.csv","wb")

cw = csv.writer(co)

cw.writerow(["NAME"])

ur = "http://www.ratemyprofessors.com/SelectTeacher.jsp?sid=1389"

url = urllib.urlopen(ur)

soup = Soup(url)

#print soup

l = []

for div in soup.findAll("div", {"class":"profName"}):
    if "SORT"  in  str(div.text):
        pass
    else:
       l += [  div.text   ]

for name in l:
    cw.writerow([name])


co.close()
