from selenium import webdriver
r=webdriver.Chrome("C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
r.get('http://www.taobao.com')
print(r.page_source)
