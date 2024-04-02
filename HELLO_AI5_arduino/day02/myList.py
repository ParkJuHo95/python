import os

list = os.listdir("animal/")


for idx,name in enumerate(list):
    print(name, chr(65+idx))
