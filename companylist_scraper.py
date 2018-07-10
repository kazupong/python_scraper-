'''

a python web scraper that goes to 日本国税庁 and 
get all company list along with their business number, 
name and address.


author 
@Kazuyuki Nakatsu


further improvement:
	time.sleep(3)のロジックではなく、loadが完了しデータが抽出され次第、ページ偏移する
    process = WebDriverWait(driver, bufferTime).until(EC.presence_of_element_located((By.NAME, 'next'))



'''
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
# 国税庁　全国企業基本情報の検索




url = 'https://www.houjin-bangou.nta.go.jp/kensaku-kekka.html'


# instantiate a selenium object and set the above url 
driver = webdriver.Chrome()
driver.get(url)

# select the prefecture attribute as follows...
select = Select(driver.find_element_by_id('addr_pref'))
select.select_by_visible_text('北海道')

# click on the 'show 100 companies at once' button
driver.find_element_by_class_name('submitBtn01').click()
driver.find_element_by_link_text("100件").click()

'''
#let's pass html data to bs4 from selenium 
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

#detecting table 
table = soup.table.tbody 
tr = table.find_all('tr')
'''

#detecting '次の100件' button
#next100 = driver.find_element_by_class_name('next').click()

isNext = True

while isNext:

	time.sleep(3)
	
	html = driver.page_source
	soup = BeautifulSoup(html,'html.parser')
	table = soup.table.tbody
	tr = table.find_all('tr')

	try:
		for i in tr:
			th = i.find_all('th')
			for j in th:

				# store data into SQL : company number
				print(j.get_text().strip())

			td = i.find_all('td')
			count = 0
			for k in td:
				if count >= 2:
					break
				# store data into SQL : company name and address 
				print(k.get_text().strip())
				count += 1
			print("")

		driver.find_element_by_link_text('次の100件').click()	
	
	except:
		isNext = False
		print("the process has finished")


