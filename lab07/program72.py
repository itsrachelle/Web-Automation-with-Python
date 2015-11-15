import mechanize

from BeautifulSoup import BeautifulSoup as Soup


br = mechanize.Browser()

br.addheaders = [('csc299','true')]

br.open('http://mdp.cdm.depaul.edu/csc299a7/default/index')

br.select_form(nr=0)

br.form['email'] = "rachelle.r.chan@gmail.com"

br.form['password'] = "bogus"

br.submit()

soup = Soup(br.open('http://mdp.cdm.depaul.edu/csc299a7/default/index#').read())

sumi = 0



for span in soup.findAll( "span", {"class":"number"} ):

    sumi += int(span.text) 

  

for link in  br.links():
    if "Next" in  link.text:
        req = br.click_link(link)
        resp = br.follow_link(link)
        


br.select_form(nr=0)

br.form['total'] = str(sumi)

x = br.submit()


