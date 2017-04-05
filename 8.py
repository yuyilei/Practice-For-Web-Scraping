
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class Tool:
    img = re.compile('<img.*?>| {7}|')
    adder = re.compile('<a.*?>|</a>')
    line = re.compile('<tr>|<div>|</div>|</p>')
    t = re.compile('<td>')
    para = re.compile('<p.*?>')
    br = re.compile('<br><br>|<br>')
    other = re.compile('<.*?>')

    def remove(self,x) :
        x = re.sub(self.img,"",x)
        x = re.sub(self.adder,"",x)
        x = re.sub(self.line,"\n",x)
        x = re.sub(self.t,"\t",x)
        x = re.sub(self.para,"\n   ",x)
        x = re.sub(self.br,"\n",x)
        x = re.sub(self.other,"",x)
        return x.strip()



class BD :
    def __init__(self,url,see,floortag) :
        self.url = url
        self.see = '?see_lz=' + str(see)
        self.tool = Tool()
        self.floor = 1
        self.file = None
        self.default = u'百度贴吧'
        self.floortag = floortag

    def get(self,page) :
        try :
            Url = self.url + self.see + '&pn=' + str(page)
            request = urllib2.Request(Url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError ,e :
            if hasattr(e,"reason") :
                print u"错误原因" ,  e.reason
                return  None

    def page(self,page) :
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result :
            return result.group(1).strip()
        else :
            return None

    def content(self,page) :
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items  :
            content = "\n" + self.tool.remove(item)+"\n"
            contents.append(content.encode('utf-8'))
        return contents

    def gettitle(self,page) :
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result :
            return result.group(1).strip()
        else :
            return None


    def title(self,title) :
        if title is not None :
            self.file = open(title+".txt","w+")
        else :
            self.file = open(self.default+".txt","w+")

    def write(self,contents) :
        for item in contents :
            if self.floortag == '1' :
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self) :
        index = self.get(1)
        page = self.page(index)
        title = self.gettitle(index)
        self.title(title)
        if page == None :
            print 'url已失效'
            return
        try :
            print "该帖子共有" + str(page) + "页"
            for i in range(1,int(page)+1):
                print "正在写入第" + str(i) + "页数据"
                pages = self.get(i)
                contents = self.content(pages)
                self.write(contents)
        #出现写入异常
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"


baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = BD(baseURL,seeLZ,floorTag)
bdtb.start()
