import csv


head = ["USER_ID","FIRST_NAME","LAST_NAME","BEGIN_BALANCE","END_BALANCE"]

co = open("accounts.csv", "r")

co2 = open("totals.csv", "r")

co3 = open("results.csv", "wb")

cr = [row for row in csv.reader(co)]  

cr2 = [row for row in csv.reader(co2)]

dit = {}

for row in cr[1:]:     #cr[1:] skips header  #row is each row in csv
    
    if row[0] not  in dit:
        dit[row[0]] = 0
    dit[row[0]] += float(row[3][1:])

ditf = {}

for row in cr2[1:]:
    if row[0] not in ditf:
        ditf[row[0]] = 0
    ditf[row[0]] = dit[row[0]] - float(row[1])

co3w = csv.writer(co3)

co3w.writerow(head)


for key in ditf:
    for row in cr[1:]:
        if row[0]== key:
           row.append(ditf[key] )
           co3w.writerow( row )
           
