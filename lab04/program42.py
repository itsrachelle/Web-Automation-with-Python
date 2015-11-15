from BeautifulSoup import BeautifulSoup as Soup

html = open("accounts.1.html", "r")

f = open("amount.luise.txt","w")

soup = Soup(html)

inside = []

for name in soup.findAll("td"):
    inside += [name.text]

for i in range(len(inside)):
    if "Luise Carpentier" in inside[i]:
        f.write( inside[i+1] )


f.close()

