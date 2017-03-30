import requests
url ='http://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016&currentPage=1'
request = requests.get(url)

import re 
json = re.findall('\"rateList\":(\[.*?\])\,\"tags\"',myweb.text)[0] 

import pandas 
table = pandas.read_json(json)

table.to_csv('table.txt')
