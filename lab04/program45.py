import re 
import sys
import simplejson


keywords =  sys.argv[1:]

courses = simplejson.load(open('CSC.json'))

for course in courses:
    found = True
    for keyword in keywords:
        if keyword not in course['coursetitlelong'].lower():
            found = False
            break
        if found:
            print course['subjectid'],course['coursetitlelong'],course['catalognbr']
