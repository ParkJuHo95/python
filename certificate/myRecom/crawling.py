from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://namu.wiki/w/%EA%B5%AD%EA%B0%80%EA%B8%B0%EC%88%A0%EC%9E%90%EA%B2%A9#s-3")





divs = driver.find_elements(By.CLASS_NAME,'JOWKtQdm')

nowstart = False;

for div in divs:
    trs = div.find_elements(By.TAG_NAME, 'tr')
    for idx,tr in enumerate(trs):
        if idx == 0:
            td = tr.find_element(By.TAG_NAME,'td').text
            if td == "2. 경영/회계/사무":
                nowstart = True
            if nowstart == True:
                td = f"{td}"
                if not td.isspace():
                    print(td)
        
        if idx == 1:
            continue
        
        if nowstart == True:
            tds = tr.find_elements(By.TAG_NAME,'td')
            for td in tds:
                td = f"{td.text}"
                if td.isspace():
                    continue
                print(td)
        
        