import time
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unicodedata

chrome_options = Options()
chrome_options.add_argument("--headless")
blue = "&#9650;"
red = "&#9660;"
yellow = "&#9632;"
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options = chrome_options)  # Optional argument, if not specified will search path.
driver.get('http://stockboard.sbsc.com.vn/apps/StockBoard/SBSC/HOSE.html')
time.sleep(10) # Let the user actually see something!
boardData = driver.find_element_by_id('boardData')
items = boardData.find_elements_by_tag_name('tr')
print(len(items))
print blue + red + yellow
for item in items:
    name = item.find_element_by_tag_name('span').text
    tds = item.find_elements_by_tag_name('td')
    for td in tds:
        #txt = unicodedata.normalize('NFKD', td.text.strip()).encode('ascii','ignore')
        txt = td.text.strip()
        if isinstance(txt, unicode):
            txt = txt.encode('ascii' , 'xmlcharrefreplace')
            if txt.startswith(red):
                txt = txt.replace(red, "-")
                txt = txt.replace("\n","")
                txt = txt.replace(" ", "")
            elif txt.startswith(yellow):
                txt = txt.replace(yellow, "")
                txt = txt.strip()
            elif txt.startswith(blue):
                txt = txt.replace(blue, "")
                txt = txt.strip()
            txt = txt.replace(",","")
            print float(txt)
        txt.strip()
        name += "\t" + txt
    print(name)

driver.quit()
