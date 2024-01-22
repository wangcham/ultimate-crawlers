from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# 设置代理服务器
PROXY = "127.0.0.1:7890" 

# 创建一个ChromeOptions实例
options = webdriver.ChromeOptions()

# 忽略证书错误
options.add_argument('--ignore-certificate-errors')
# 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed. 错误
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 忽略 DevTools listening on ws://127.0.0.1... 提示
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# 添加参数来设置代理服务器
options.add_argument('--proxy-server=%s' % PROXY)

# 创建一个Service实例
service = Service(executable_path=r'D:\playground\ultimate\venv\Scripts\chromedriver.exe')

# 创建一个WebDriver实例
chrome = webdriver.Chrome(service=service, options=options)
# 李健传奇
chordurl = 'http://tabs.ultimate-guitar.com/tab/2005369'
chrome.get(chordurl)
elements = chrome.find_element(by=By.CSS_SELECTOR,value='body > div.js-page.js-global-wrapper.ug-page > div.fbcII > main > div.BDmSP > article.o2tA_.JJ8_m > div:nth-child(1) > section:nth-child(2) > article > section.P8ReX > div > section > code')

page = elements.get_attribute('innerHTML')

soup = BeautifulSoup(page,'html.parser')

spans = soup.find_all('span',class_='y68er')

for span in spans:
    print(span.text)
