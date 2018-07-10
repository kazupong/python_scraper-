#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 23:44:39 2018

@author: kazoo
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib3

url = 'https://www.houjin-bangou.nta.go.jp/kensaku-kekka.html'

http = urllib3.PoolManager()
response = http.request('POST', url, fields = {'prefectureLst': "01"})

soup = BeautifulSoup(response.data,'html.parser')
#soup = BeautifulSoup(requests.get(url, verify = False).content,'html.parser')

temp = soup.find('div', class_= "paginate").find('li', class_="next")
print(temp.prettify())

next100 = 



'''
info = []


table = soup.table.tbody 
tr = table.find_all('tr')

for i in tr:
    
     th = i.find('th')
     print(th.get_text().strip())
     #temp_th = th.get_text().replace(" ","")
     
    
     
     td = i.find_all('td')
     count = 0
     for j in td:
         if count < 2:
             temp_td = j.get_text().strip()
             
             print(str(temp_td))
         count +=1       
     print("")
    

'''

       
       
             


