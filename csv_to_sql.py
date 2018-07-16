'''

@author Kazuyuki Nakatsu

chrome_outに書き出されたcvsファイルから
必要な情報を抽出し、それらをmySQLに保存する

'''
import os
import csv
import mysql.connector


temp_path = os.path.join('chrome_out')

#このファイルと同じhierarchyに出力される'chrome_out'フォルダの内の
#.cvsファイルのpathをlistに保存
chrome_out = os.listdir(temp_path)
csv_files = []
for ele in chrome_out :
	if os.path.splitext(ele)[1] == '.csv':
		csv_files.append(ele)


#----- test ---------------------------
#csv_file = [csv_files[0]]
#テストが終われば下記のfor loop を　~... in csv_files: に戻す　<-----------  <------------ <--------     test 中
#--------------------------------------


# mySQLのlogin情報をコネクタに設定
conn = mysql.connector.connect(user = 'user1', password = 'user1_Password', 
	                           host = '127.0.0.1' , database = 'sampledb', 
	                           auth_plugin='mysql_native_password')

#カーソルの宣言
cur = conn.cursor()

#データベースへ挿入する型の宣言
add_company_info = ("INSERT INTO companyList" "(id, name, pref, city, address, full_address)" " VALUES (%s, %s, %s, %s, %s, %s)")

sum_file = len(csv_files)
print()
print("writing out to database...")


count = 0
#以下でcsvファイルから企業情報を取得、そしてSQLサーバーに送信
for ele in csv_files: 
	 
	 print(ele, end ='')
	 print(' is being processed...')

	 #csv_fileというリストからFile PATHを成型
	 PATH = os.path.join('chrome_out',ele)

	 #PATHを元にCSVfileを開き、
	 try: 
	 	  with open(PATH,'r', encoding='SHIFT_JIS') as csvfile:

	 	       reader = csv.reader(csvfile)

	 	       for row in reader:
				   
				   #----- １列ごとにmySQLの処理をする ---------

	 		       row_id   = row[1]
	 		       row_name = row[6]
	 		       row_pref = row[9]
	 		       row_city = row[10]
	 		       row_address = row[11]
	 		       row_full_address = row[9] + row[10] + row[11]

	 		       data_company_info = (row_id,row_name,row_pref,row_city,row_address,row_full_address)
	 		       cur.execute(add_company_info,data_company_info)
	 		       conn.commit()
	 	       
	 except Exception as a:
	 	raise a
	 	print(" Debug場所： ファイルを開く際 or mySQLの操作時の try/except ") 
	 print('%i / %i files has completed...'%(count,sum_file))
	 count += 1






