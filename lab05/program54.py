import json
import simplejson
import sys


copy = simplejson.load(open("CSC.json", "r"))


for dit in copy:
  #  print dit
    for key in dit:
        print key
