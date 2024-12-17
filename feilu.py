from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
browser=webdriver.Chrome(service=service, options=options)
url = 'https://www.hongxiu.com/chapter/30096664207575309/80796541564023424'
browser.get(url)
print(browser.page_source)
browser.close()
