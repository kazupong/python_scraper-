# pythonとSeleniumとBeautifulSoup4で web scraper！

         Web Driver である　selenium と　BeautifulSoup4 を使った Python のウェブ　crawler と　scraper です。


## abstract  


        国税庁の公式ウェブサイトにある、日本の企業のデータ（基本情報：企業番号、名称、所在地）を抽出します. 
        上記の企業データはjavascriptで構成されたformに動的に配置されており、requests や　urllib3などのAPIではなく
        seleniumを使いました。
        
[国税庁]-https://www.houjin-bangou.nta.go.jp/kensaku-kekka.html
        
### remarks 

        Mac用（OSX）のChrome driverを使用しております.
        download後、そのファイルを/usr/bin に移動させるとコード内でPATHの指定をしなくて済むようになる。(以下url参照ください)
        
        
[chromium ダウンロード]-http://chromedriver.chromium.org/downloads.   
[ドライバの保存先　説明]-http://damien.co/resources/how-to-install-chromedriver-mac-os-x-selenium-python-7406


####  参考サイト

[chromium reference]-https://sites.google.com/a/chromium.org/chromedriver/getting-started
[selenium official documentation]-https://www.seleniumhq.org/docs/
