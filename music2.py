#encoding=utf8
import requests 
from bs4 import BeautifulSoup 

headers = {
        
        'Referer' : 'http://music.163.com/' ,
        'Host' : 'music.163.com' ,
        'User-Agent' : 'Mozilla/5.0 (xll; Linux x86_64; rv:38.0) Geoko/20100101 Firefox/38.0 Iceweasel/38.0',
        'Accept' :
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*,q=0.8'
        ,
        }
url = 'http://music.163.com/playlist?id=627620651'
s = requests.session()
s = BeautifulSoup(s.get(url,headers = headers).content,'lxml')
main = s.find('ul',{'class':'f-hide'})

for music in main.find_all('a') :
    print('{} : {}'.format(music.text,music['href']))
