import urllib 
import csv
import re

from BeautifulSoup import BeautifulSoup as Soup

co  = open("professors.csv","wb")

cw = csv.writer(co)

cw.writerow(["NAME", "RATING", "QUALITY", "EASINESS", "TID"])

ur = "http://www.ratemyprofessors.com/SelectTeacher.jsp?sid=1389"

url = urllib.urlopen(ur)

soup = Soup(url)

l = []
d = []
tr = []
oq = []
e = []
tid = []


for div in soup.findAll("div", {"class":"profName"}):
    if "SORT"  in  str(div.text):
        pass
    else:
       l += [  div.text   ]






for dept in soup.findAll("div", {"class":"profDept"}):
    if "DEPARTMENT" in dept.text:
        pass
    else:
        d += [str(dept.text)]



for rating  in soup.findAll("div", {"class":"profRatings"}):
    if "Total" in rating.text:
        pass
    else:
       tr += [str(rating.text)]



for avg  in soup.findAll("div", {"class":"profAvg"}):
    if "Overall" in avg.text:
        pass
    else:
       oq += [str(avg.text)]

for easy in soup.findAll("div", {"class":"profEasy"}):
    if "Eas" in easy.text:
        pass
    else:
       e+= [str(easy.text)]

for n in range(len(l)):
    names = l[n]
    dept = d[n]
    total = tr[n]
    avg = oq[n]
    easy = e[n]
    teachid = tid #####
    cw.writerow([names,dept,total,avg,easy,teachid])
   
#for tid in soup.findAll("div", href=True ):
#    print tid



