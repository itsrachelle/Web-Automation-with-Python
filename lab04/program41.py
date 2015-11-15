import urllib

url = "http://mdp.cdm.depaul.edu/csc299/default/accounts?page=1"

f = open("accounts.1.html", "w")

uor = urllib.urlopen(url).read()

f.write(uor)

f.close()
