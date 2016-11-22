#!/usr/bin/env python

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""



soup = BeautifulSoup(
							   html_doc,
							   'html.parser',
							   from_encoding = 'utf-8'
							   )
							   

							   
# find links include 'a'
print '-find links include "a"'
links = soup.find_all('a')
for link in links:
	print link.name, link['href'], link.get_text()
	
# find links include href as 'http://example.com/elsie'
print '-find links include "a" with href as "http://example.com/elsie"'
links = soup.find_all('a', href = "http://example.com/elsie")
for link in links:
	print link.name, link['href'], link.get_text()
	
# find links include "a" with href like 'elsie'
print '-using RE'
links = soup.find_all('a', href = re.compile(r'elsie'))
for link in links:
	print link.name, link['href'], link.get_text()
	
# find links include 'p' class as 'title'
print '-find links with title as "p", class as "title"'
links = soup.find_all('p', class_ = 'title')
for link in links:
	print link.name, link.get_text()