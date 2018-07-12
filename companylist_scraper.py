'''

国税庁ウェブサイト内にあるJavaScriptで構成されたテーブル内から、
日本に登記してある基本企業情報（企業番号,商号,所在地）をスクレイピング
を行い、mySQLを使ってSQLサーバーに書き出す


環境：　Python3, selenium, beautifulSoup4, mySQL -v 8.* 

注意点：　予めmySQLでサーバーを作成する必要がある
　　　　　属性 = (id text, name text, address text)

author 
@Kazuyuki Nakatsu

'''
import re
import time
import mysql.connector
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


# 国税庁　全国企業基本情報の検索
url = 'https://www.houjin-bangou.nta.go.jp/kensaku-kekka.html'

# 都道府県list
'''
pref = ['北海道', '青森','岩手','宮城','秋田','山形','福島','茨城','栃木',
　　　　　　'群馬','埼玉','千葉','東京','神奈川','新潟','富山','石川','福井',
　　　　　　'山梨','長野','岐阜','静岡','愛知','三重','滋賀','京都','大阪',
　　　　　　'兵庫','奈良','和歌山','鳥取','島根','岡山','広島','山口','徳島',
　　　　　　'香川','愛媛','高知','福岡','佐賀','長崎','熊本','大分','宮崎',
　　　　　　'鹿児島','沖縄','国外']
'''

# ------------< mySQL login information >---------------
# note: your user account has to be one that uses mysql_native-password 
#        and has all authority on the account.
#
# edit the following login information to 
user     = '****'
password = '****'
host     = '****'
database = '****'

# ------------------------------------------------------


# mySQLのコネクタを設定
conn = mysql.connector.connect(user= user,   password=password,
                               host= host,   database=database,
                               auth_plugin='mysql_native_password')
# コネクタのカーソルを宣言
cur=conn.cursor()

#  テーブルにPOSTするframeを成型
add_company_info = ("INSERT INTO companyList" "(id, name, adress)" " VALUES (%s, %s, %s)")



# Chromeのドライバーと上記URLをセット 
driver = webdriver.Chrome()
driver.get(url)

# スクレイプする都道府県をセット：　
# 全国分スクレイピングするのであれば、loop内で指定
select = Select(driver.find_element_by_id('addr_pref'))
select.select_by_visible_text('北海道')

# 都道府県を指定後、検索ボタンをクリックし、JavaScriptのformを更新
driver.find_element_by_class_name('submitBtn01').click()

# １００件づつ表示させるため、'１００件'というボタンをクリック
driver.find_element_by_link_text("100件").click()

# detecting '次の100件' button
# next100 = driver.find_element_by_class_name('next').click()

isNext = True

while isNext:

	#time.sleep(1)
	driver.implicitly_wait(10)
	
	# seleniumで得たhtmlデータをbs4に渡す
	html = driver.page_source
	soup = BeautifulSoup(html,'html.parser')
	
	# 必要なtable情報の部分にまでloop先を絞り込む
	table = soup.table.tbody
	info_table = table.find_all('tr')

	try:
		for ele in info_table:
			

			# ------------- < 企業番号の取得 >-------------
			
			# 企業番号がStringで返ってくる
			company_num = ele.find('th').get_text().strip()
			
			print(company_num)

			# -------------------------------------------
			

			# 企業情報（商号、所在地、url）が入ったlistが返り値  
			company_info = ele.find_all('td')
		
			# ------------- < 商号の取得 >-----------------
			
			temp = company_info[0].get_text()
			temp_fixed = re.sub('\n', '', temp)
			company_name = re.sub(' ', '', temp_fixed)
			company_name.replace('\r','').strip()
			print(company_name)
			# --------------------------------------------
			
			# ------------- < 所在地の取得 >----------------
			
			addr = company_info[1].get_text()
			addr_fixed = re.sub('\n', '', addr)
			company_address = re.sub(' ','',addr_fixed)
			company_address.replace('\r','').strip()
			print(company_address)
			# --------------------------------------------

			print("")

			# ------------- < mySQLへ書き出し> -------------
			
			data_company_info = (company_num, company_name, company_address)
			cur.execute(add_company_info,data_company_info)
			conn.commit()
            

		# 次の100件をクリックし、ページを更新
		driver.find_element_by_link_text('次の100件').click()	
	
	except BufferError:
		isNext = False
		print("the process has finished")


