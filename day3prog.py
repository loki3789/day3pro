import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#fhand=open("sample.txt",'w')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tagshttps://wordpress.com/post/intershipcom.wordpress.com/9
#soup = BeautifulSoup(page.content, 'html.parser')
lst=soup.find_all('tr',attrs={ "class":"alternate1"})
#table=soup.find("table","alternate1")
#lst=table.find("tr",attrs={ "class":"alternate1"})
l=[]
count=0
#i1=table.find_all("a")
#print(soup.p.text)
for i in lst:
    #1=list(i.string)
    #i1=re.findall("http://www.\S+",i)
    i1=i.find_all('a',limit=20)
    for g in i1:
        if(count<20):
          l.append(g.get('href'))
          count+=1
    
listlist=[]
for z in l:
    url=z
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    lst=soup.find_all('a',attrs={ "class":"link6"})
    for l1 in lst:
        listlist.append(l1.get('href'))

print(listlist)


