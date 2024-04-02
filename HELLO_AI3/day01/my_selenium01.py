from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


str  = "가나다라마바사아자차"
arr_wf = [
        {'w':100,'f':0},
        {'w':100,'f':1},
        {'w':100,'f':2},
        {'w':100,'f':3},
        {'w':100,'f':4},
        {'w':100,'f':5},
        {'w':100,'f':6},
        {'w':100,'f':7},
        
        {'w':600,'f':0},
        {'w':600,'f':1},
        {'w':600,'f':2},
        {'w':600,'f':3},
        {'w':600,'f':4},
        {'w':600,'f':5},
        {'w':600,'f':6},
        {'w':600,'f':7}
    ]
driver = webdriver.Firefox()
for i in range(10):
    index = 1
    myChar = str[i:i+1]
    for j in range(len(arr_wf)):
        driver.get(f"http://localhost:5000/ganadaSem?char={myChar}&w={arr_wf[j]['w']}&f={arr_wf[j]['f']}")
        driver.implicitly_wait(10)
        obj_span = driver.find_elements(By.CSS_SELECTOR,'span')
        nameIndex = (f"{index}").zfill(2)
        obj_span[0].screenshot(f"images/{myChar}{nameIndex}.png")
        index +=1



