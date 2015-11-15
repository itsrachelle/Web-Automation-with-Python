import csv

ocsv = open("accounts.csv","r")

cr = csv.reader(ocsv)

bal = 0.0 

for row in cr:
   if "$" in row[3]:
      num = float(row[3][1:])
      bal = bal + num

print bal

f = open("balance.txt","w")

f.write(str(bal))

f.close()     
