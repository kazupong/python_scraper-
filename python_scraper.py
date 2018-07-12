#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 23:44:39 2018

@author: kazoo

  国税庁のウェブサイトから各都道府県別になっている企業データ（CSV形式 ・Unicode）を
  スクレイピングしてダウンロードする。

  ファイルの保存先：同じ階層のフォルダ内にchrome_outという名のフォルダを自動に作り、
                 そこにファイルを保存する

"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from urllib.parse import urlparse



#国税庁のウェブサイト
url = 'https://www.houjin-bangou.nta.go.jp/kensaku-kekka.html'

# Chromeドライバにダウンロード先の指定

chromeOptions = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'chrome_out'}
chromeOptions.add_experimental_option('prefs', prefs)


# SeleniumにChromeのドライバを設定
driver = webdriver.Chrome(chrome_options = chromeOptions)
# 国税庁のurlを設定
driver.get(url)

# cvsファイルのダウンロード画面までnavigate
driver.find_element_by_link_text("基本３情報ダウンロード").click()
driver.implicitly_wait(10)
driver.find_element_by_class_name("alignC").click()

# cvs形式・Shift_JIS のテーブル内の、各都道府県分のzip ファイルをする
# table[0]: 
table = driver.find_elements_by_class_name("tbl02")
cvs_jis = table[0].find_elements_by_tag_name('a')

# navigate先のテーブル内から各都道府県の企業データを取得・保存
print("downloading files...")
for ele in cvs_jis:
    ele.click()
print("process has finished!")
