import mechanize
import cookielib
import re

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

r = br.open('http://store.nike.com/us/en_us/pw/mens-shoes/7puZbrk')
#html = r.read()

p = re.compile('lebron.*12', re.IGNORECASE)

for link in br.links():
	m1 = p.search(link.url)
	m2 = p.search(link.url)
	if m1 or m2:
    		print link.text, link.url

# Actually clicking the link
#req = br.click_link(text='Weekend codes')
#br.open(req)
#print br.response().read()
#print br.geturl()
