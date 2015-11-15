import re 
import simplejson
import sys

keywords = [ k.lower() for k in sys.argv[1:] ] 

courses = simplejson.load(open('CSC.json'))

for course in courses:
    found = all( [ (k in course['coursetitlelong'].lower() ) for k in keywords] )
    if found:
        print course['subjectid'], course['catalognbr'],course['coursetitlelong']
