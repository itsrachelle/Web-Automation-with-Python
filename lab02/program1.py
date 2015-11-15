from random import randint
myfile = open("data.csv","w")
for k in range (1000):
    myfile.write(",".join([str(randint(0,1000)) for i in "0123"]) + "\n")
