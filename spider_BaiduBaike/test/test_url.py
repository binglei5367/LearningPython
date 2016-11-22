#!/usr/bin/env python

import urllib2, cookielib

url = 'http://www.baidu.com'

#method 1
print '-Method 1'
response1 = urllib2.urlopen(url)
print response1.getcode()
cont1 = response1.read()
print len(cont1)

#method 2
print '-Method 2'
request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)
print response2.getcode()
cont2 = response2.read()
print len(cont2)

#method 3
print '-Method 3'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
cont3 = response3.read()
print len(cont3)
print cj