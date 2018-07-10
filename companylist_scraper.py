'''

a python web scraper that goes to 日本国税庁 and 
get all company list along with their business number, 
name and address.


author 
@Kazuyuki Nakatsu

'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


url = 'https://www.houjin-bangou.nta.go.jp/kensaku-kekka.html'



driver = webdriver.Chrome()
driver.get(url)

select = Select(driver.find_element_by_id('addr_pref'))
select.select_by_visible_text('北海道')

driver.find_element_by_class_name('submitBtn01').click()
driver.find_element_by_link_text("100件").click()


#let's pass html data to bs4 from selenium 
html = driver.page_source
soup = BeautifulSoup(html)

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
    

