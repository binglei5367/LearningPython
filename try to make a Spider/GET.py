import urllib
import urllib2

values = {}
values["username"] = "15327700930m0@sina.cn"
values["password"] = "xx19960922"

data = urllib.urlencode(values)

url = "http://passport.csdn.net/account/login"

geturl = url + "?" + data

request = urllib2.Request(geturl)

response = urllib2.urlopen(request)

print response.read()