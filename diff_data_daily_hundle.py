'''
@author Kazuyuki Nakatsu 


----< 差分データの更新 >-----


国税庁のウェブサイトに毎日更新される企業データの差分データをスクレイピング・
ダウンロードし、同じ階層に'diff_out'というfolderを出力する。
そこでzipファイルを解凍、そしてその中からCSVファイルを取り出し、
データベースにある既存の企業情報と照らし合わせ、

・レコードの新規挿入
・レコードの更新
・レコードの削除
・レコードの検索

などを行う。

（処理内容）
CSVファイルの差分データ内３列目のセルは、処理内容コードが記載されている。
______________________________
|code |       処理内容         |
------------------------------
|  1  |  新規に登記            |
------------------------------
| 11  |  商号または名称の変更   | 
------------------------------
| 12  |  国内所在地の変更.      |
------------------------------
| 13  |  国外所在地の変更.      |
------------------------------
| 21  |  登記記録の閉鎖         |
------------------------------
| 71  |  吸収合併              |
------------------------------
| 81  |  商号登記の抹消         |
------------------------------
| 99  |  削除                 |   
------------------------------

参照：
国税庁のサンプルデータ
https://www.houjin-bangou.nta.go.jp/documents/k-sample-explain-h3001.pdf

上記の内容に基づき、データベースも同様の処理をする。

'''

import os 
import csv
import mysql.connector 
from selenium import webdriver


#国税庁のウェブサイト
url = 'https://www.houjin-bangou.nta.go.jp/kensaku-kekka.html'

# mySQLのlogin情報をコネクタに設定
conn = mysql.connector.connect(user = 'user1', password = 'user1_Password', 
	                           host = '127.0.0.1' , database = 'sampledb', 
	                           auth_plugin='mysql_native_password')

#カーソルの宣言
cur = conn.cursor(buffered=True)


#データベースへ挿入する型の宣言
insert_company   = ("INSERT INTO companyList" "(id, name, pref, city, address, full_address)" " VALUES (%s, %s, %s, %s, %s, %s)")
updata_name      = ("UPDATE companyList SET name = '%s' where id = '%s'")
updata_address   = ("UPDATE companyList SET address = '%s' where id = '%s'")
delete_company_by_id   = ("DELETE FROM companyList where id = '%s'")
select_company_by_id   = ("SELECT * FROM companyList where id = '%s'")

cur_id = ('9700150079227')
#cur.execute(select_company_by_id, cur_id)

cur.execute('select * from companyList where id =' + cur_id)
a = cur.fetchall()
print(a)
#connect.commit()













'''

# ---------- WEB SCRAPING PART --------------------------

# Chromeドライバにダウンロード先の指定
chromeOptions = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'diff_out'}
chromeOptions.add_experimental_option('prefs', prefs)

# SeleniumにChromeのドライバを設定
driver = webdriver.Chrome(chrome_options = chromeOptions)
# 国税庁のurlを設定
driver.get(url)
# 差分データをダウンロードするページまでナビゲート
driver.find_element_by_link_text("基本３情報ダウンロード").click()
driver.implicitly_wait(10)
driver.find_element_by_link_text("差分ダウンロード").click()


'''



# 昨日の差分データを確認するロジック-------------------------------------





# ------------- UNZIPPING PART  ---------------------------------
'''
try:
    diff_out = os.listdir('diff_out')
except Exception as a:
	#print("Error: diff_outフォルダが開けない、もしくは存在していない")
else:
   for ele in diff_out:
   
        # 接続子が.zipのfileだけをターゲットにする
        if os.path.splitext(ele)[1] == '.zip':
		
	         path = os.path.join('diff_out', ele)
	         with zf.ZipFile(path) as unzip:
	           		
                  for file in unzip.namelist():
               	       if os.path.splitext(file)[1] == '.csv':
               	       	   unzip.extract(file, 'diff_out')
'''                     


# -------------- mySQL PART ------------------------------------









