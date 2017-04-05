import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'email' : 'yyl1352091742@gamil.com' ,
    'password' : 'qazwsx1352091742'
    })

login = 'http://www.imooc.com/user/newlogin'
grade = 'http://www.imooc.com/u/5143599'
result = opener.open(login,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
res = opener.open(grade)
print res.read()
