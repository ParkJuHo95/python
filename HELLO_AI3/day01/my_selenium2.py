from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox, FirefoxOptions
import os
import time


file_list = os.listdir("./static/examples/textures/hangul/")

arr_xy = [
        {'rx':-0.5,  'ry':-0.5},
        {'rx':0,    'ry':-0.5},
        {'rx':0.5,  'ry':-0.5},

        {'rx':-0.5, 'ry':0},
        {'rx':0,    'ry':0},
        {'rx':0.5,  'ry':0},

        {'rx':-0.5, 'ry':0.5},
        {'rx':0,    'ry':0.5},
        {'rx':0.5,  'ry':0.5}
    ]

# print(file_list[0][0:3])

opts = FirefoxOptions()
opts.add_argument("--width=600")
opts.add_argument("--height=600")
driver = webdriver.Firefox(options=opts)

index = 1
mine = None
for i in range(len(file_list)):
    if file_list[i][0:1] != mine:
        mine = file_list[i][0:1]
        index = 1
    for k in range(len(arr_xy)):
        nameIndex = (f"{index}").zfill(3)
        driver.get(f"http://localhost:5000/static/examples/ganadara?image={file_list[i][0:3]}&rx={arr_xy[k]['rx']}&ry={arr_xy[k]['ry']}")
        driver.implicitly_wait(10)
        # obj_span = driver.find_elements(By.CSS_SELECTOR,'span')
        time.sleep(0.01)
        driver.save_screenshot(f"static/examples/textures/ganada/{file_list[i][0:1]}{nameIndex}.png")
        # print(nameIndex)
        index +=1
        
        
        
        