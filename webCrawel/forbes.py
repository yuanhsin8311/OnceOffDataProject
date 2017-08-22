#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pandas as pd 
import os, csv


from py2neo import Graph, Path

url = "http://bniamerica.com/en-us/memberlist.php?keywords=wealth+management&countryIds=10&submit=Search"
r = requests.get(url)


data = r.text
soup = BeautifulSoup(data,'html.parser')


tbl = soup.findAll('table')[0].tbody.findAll('tr')
times = len(soup.findAll('table')[0].tbody.findAll('tr'))


for i in range(times):
	#print str(i) 
	#name = tbl[i].findAll('td')[1].find('a').string
	try:
    		name = tbl[i].find('a',attrs={'class':'linkone'}).string
	except (AttributeError):
    		print "************   no attribute    ***********"
	#link = tbl[i].findAll('a')[0]['href']
	city = tbl[i].findAll('td')[3].text
	specialty = tbl[i].findAll('td')[5].text
	company = tbl[i].findAll('td')[6].text
	




	
	
		





