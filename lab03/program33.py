import csv 

co = open("expenses.csv","r")

co2 = open("totals.csv", "wb") 

cr = [row for row in csv.reader(co)]

dit = {}

for row in cr[1:]:
    if row[0] not in dit:
        dit[row[0]] = 0
    dit[row[0]] += float(row[1][1:])

dit = dit.items()

co2writer = csv.writer(co2)

co2writer.writerow(["USER_ID", "TOTAL_EXPENSE"])

for row in dit:
   co2writer.writerow(row)

#print row


