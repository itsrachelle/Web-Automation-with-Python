import mechanize

br = mechanize.Browser()

br.addheaders = [("csc299", "true")]

br.open('http://mdp.cdm.depaul.edu/csc299a7/default/user/register')

l = ["Rachel","Ramos","rachelle.r.chan@gmail.com","bogus","bogus","1358417"]

br.select_form(nr=0)

br.form['first_name']= l[0] 

br.form['last_name']= l[1]

br.form['email']= l[2]

br.form['password']= l[3]



br.form['password_two']= l[4]

br.form['student_id']= l[5]


br.submit()



