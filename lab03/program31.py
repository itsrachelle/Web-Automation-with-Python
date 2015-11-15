
import csv

import urllib

url1 = "http://mdp.cdm.depaul.edu/csc299/static/data/1358417.accounts.csv"

url2 = "http://mdp.cdm.depaul.edu/csc299/static/data/1358417.expenses.csv"

urlo1 = urllib.urlopen(url1).read()

urlo2 = urllib.urlopen(url2).read()

acc = open("accounts.csv", "w")

exp = open("expenses.csv", "w")

acc.write(urlo1)

exp.write(urlo2)

acc.close()

exp.close()
