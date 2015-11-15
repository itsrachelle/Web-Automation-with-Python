from __future__ import with_statement

from fabric.contrib.files import exists

from fabric.api import env,local,run,sudo,cd,get

from fabric.operations import put



env.hosts = ["140.192.30.237"]

env.user = "user1358417tmp"

env.password = "987654321"

def zip_and_retrieve(folder):
  run("zip -r folder.zip %s" %folder)
  get("folder.zip", "%s.zip" %folder)
  

def deploy_and_unzip(zipfile,folder):
  if not exists(folder): 
      run("rm folder")

  put(zipfile,zipfile)
  run("unzip -o %s -d %s" % (zipfile,folder)) #-o for zip -d for folder exist 

def install_facebook_clone():

    local("wget http://www.web2py.com/examples/static/web2py_src.zip")
    put("web2py_src.zip","web2py_src.zip")
    run("unzip -o web2py_src.zip")
  
  
    with cd('web2py/applications'):
      if not exists("fb"):
        run("mkdir fb")
      with cd("fb"):
        run("wget https://github.com/mdipierro/web2py-appliances/raw/master/FacebookClone/web2py.app.FacebookClone.w2p")
        run("tar zxvf web2py.app.FacebookClone.w2p")
    with cd("web2py"):
        run("python web2py.py -i 0.0.0.0 -p 9417 -a csc299lab08")
