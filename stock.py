import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options = chrome_options)  # Optional argument, if not specified will search path.
driver.get('http://stockboard.sbsc.com.vn/apps/StockBoard/SBSC/HOSE.html');
time.sleep(10) # Let the user actually see something!
boardData = driver.find_element_by_id('boardData')
items = boardData.find_elements_by_tag_name('tr')
print(len(items))
for item in items:
    name = item.find_element_by_tag_name('span').text
    tds = item.find_elements_by_tag_name('td')
    for td in tds:
        name += "\t" + td.text.strip()
    print(name)

driver.quit()
