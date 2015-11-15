from __future__ import with_statement

from fabric.contrib.files import exists

from fabric.api import env,local,run,sudo,cd,get

from fabric.operations import put

import glob

env.hosts = ["140.192.30.237"]

env.user = "user1358417tmp"

env.password = "987654321"



def zip_and_retrieve(folder):
  
  run("zip -r folder.zip %s" %folder)
  get("folder.zip", "%s.zip" %folder)
  
def clone():
  
  run("git clone https://itsrachelle@bitbucket.org/itsrachelle/csc299.git") 

  
def runfiles():
  files = glob.glob("*/*.py")
  files.sort()
  for py in files:
    run("python " + py)

 
