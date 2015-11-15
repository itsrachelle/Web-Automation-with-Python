import urllib

from BeautifulSoup import BeautifulSoup as Soup

f1 = open("accounts.1.html","r")

f2 = open("amount.1.txt","w")

soup = Soup(f1)

inside = 0.0

for name in soup.findAll("td"):
    if "$" in name.text:
        inside +=  float( name.text[1:] )

inside = str(inside)

f2.write( inside )

f1.close()

f2.close()
