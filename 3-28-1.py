from urllib.request import urlopen 
from urllib.error import HTTPError
from bs4 import BeautifulSoup 
import json 
import datetime 
import random 
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl) :
    try :
        html = urlopen("http://en.wikipedia.org"+articleUrl)
    except :
        print("Can not open!")
    try :
        bs0bj = BeautifulSoup(html)
    except :
        return None 
    return bs0bj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki)((?!:).)*$"))

def getHistoryIPs(pageUrl) :
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipendia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history is"+historyUrl)
    try :
        html = urlopen(historyUrl) 
    except :
        print ("Can not open historyUrl")
    try :
        bs0bj = BeautifulSoup(html)
    except :
        pass 
    ipAddresses = bs0bj.findAll("a",{"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses :
        addressList.add(ipAddress.get_text())
    return addressList 
def getCountry(ipAddress) :
    try :
        response =  urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except HTTPError :
        pass 
    responseJson = json.loads(response)
    return responseJson 

links = getLinks("/wiki/Python_(progamming_language)")

while ( links is not None ) :
    for link in links  :
        print ("---------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs :
            country in getCountry(historyIP)
            if country is not None :
                print (historyIP+" is from "+country)
                
    newLink = links[random.randint(0,len(links)-1)].attrs["href"]
    links = getLinks(newLink)

