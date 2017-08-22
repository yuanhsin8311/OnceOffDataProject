#! /usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import os, csv, json
from py2neo import Graph, authenticate

url = "http://bniamerica.com/en-us/memberlist.php?keywords=wealth+management&countryIds=10&submit=Search"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')

tbl = soup.findAll('table')[0].tbody.findAll('tr')
times = len(tbl)

temp = {}
temp['name'] = [i.findAll('td')[1].get_text().strip('u') for i in tbl]
temp['city'] = [i.findAll('td')[3].text.strip('u') for i in tbl]
temp['specialty'] = [i.findAll('td')[5].text.strip('u') for i in tbl]
temp['company'] = [i.findAll('td')[6].text.strip('u') for i in tbl]


table = {}
for i in range(times):
	table['name'] = table.setdefault('person', []).append(temp['name'][i])
	table['city'] = table.setdefault('person', []).append(temp['city'][i])
	table['specialty'] = table.setdefault('person', []).append(temp['specialty'][i])
	table['company'] = table.setdefault('person', []).append(temp['company'][i])


with open('results.json', 'w') as f:
    json.dump(table , f)	


# replace 'foobar' with your password
authenticate("localhost:7474", "neo4j", "abcd0101")
graph = Graph()
 
with open('results.json') as data_file:
    json = json.load(data_file)

query = """
WITH {json} as document
UNWIND document.name as name
RETURN name
"""
 
# Send Cypher query.
print graph.cypher.execute(query, json = json)













