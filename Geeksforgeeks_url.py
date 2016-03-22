#! /usr/bin/python

import httplib2
import socket
from bs4 import BeautifulSoup, SoupStrainer 

#http = httplib2.Http().....(IF NOT USING PROXY)
http = httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'proxy_address', port, proxy_user = 'username', proxy_pass = 'password') )

url = "http://www.geeksforgeeks.org/"
status, response = http.request(url)
soup = BeautifulSoup(response, parseOnlyThese=SoupStrainer('a'))
for link in soup.find_all('a'):
	val =str(link.get('href'))
	print(val)
	
