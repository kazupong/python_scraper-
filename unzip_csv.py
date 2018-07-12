'''

python3

特定のフォルダにあるzipファイルをを解凍し展開する

https://docs.python.jp/3.6/library/zipfile.html
https://note.nkmk.me/python-zipfile/

'''
import os
import zipfile as zf

# open chrome folder  

#chrome_outフォルダ内にあるfileをリストに保存
chrome_out = os.listdir('chrome_out')

for ele in chrome_out:
   
   # 接続子が.zipのfileだけをターゲットにする
   if os.path.splitext(ele)[1] == '.zip':
		
	      path = os.path.join('chrome_out', ele)
	      with zf.ZipFile(path) as unzip:
	           
               for file in unzip.namelist():
               	   if os.path.splitext(file)[1] == '.csv':

                       unzip.extract(file, 'chrome_out')
                       

