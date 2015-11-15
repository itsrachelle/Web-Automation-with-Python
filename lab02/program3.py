import os

dit  = {}

lengths = [len(item) for item in os.listdir("/bin")]


for length in lengths:
    if length in dit:
        dit[length] += 1
    else:
        dit[length] = 1
f = open("bincount.csv","w")

for key in sorted( dit ):
    f.write( "%s, %s\n" % (key, dit[key]) )
