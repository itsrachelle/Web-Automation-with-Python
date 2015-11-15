import urllib 

from BeautifulSoup import BeautifulSoup as Soup

f = open("amount.total.txt", "w")

num  = 0.0


for i in range(1,11):
   url = urllib.urlopen("http://mdp.cdm.depaul.edu/csc299/default/accounts?page=%d" % i).read()
   soup = Soup(url)
   for name in soup.findAll("td"):
      if "$" in name.text:
         num += float( name.text[1:] )      
 
num = str( num )

f.write(num)

f.close()
