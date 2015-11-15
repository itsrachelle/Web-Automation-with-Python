
first = 0
second = 0
third = 0
fourth = 0
f  = open("data.csv")
for line in f.readlines():
     newl =  line.strip().split(",")
     first += int( newl[0] )
     second += int(newl[1])
     third += int(newl[2])
     fourth += int(newl[3])

first = str(first)
second = str(second)
third = str(third)
fourth = str (fourth)

sum = first+","+second+","+third+","+fourth

f.close()

f2 = open("sums.csv", "w")
f2.write(sum)

f2.close()
