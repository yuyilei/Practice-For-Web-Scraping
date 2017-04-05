
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class BD :
    def __init__(self,url,see) :
        self.url = url
        self.see = '?see_lz=' + str(see)

    def get(self,page) :
        try :
            Url = self.url + self.see + '&pn=' + str(page)
            request = urllib2.Request(Url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError ,e :
            if hasattr(e,"reason") :
                print u"错误原因" ,  e.reason
                return  None
url = 'http://tieba.baidu.com/p/3138733512'
baidu = BD(url,1)
baidu.get(1)

