from bs4 import BeautifulSoup 
import urllib.request
import requests
t=input("enter username:")
html=urllib.request.urlopen("https://instagram.com/"+t)
soup=BeautifulSoup(html,features="html.parser")
x=soup.find("meta",{"property":"og:image"})['content']
y=soup.find("meta",{"property":"og:description"})['content']
like=requests.get(x)
if like.status_code==200:
    with open('crush','wb') as f:
		       f.write(like.content)
    print("crush pic on pc")
    print(y)
else:
	print("oops")

