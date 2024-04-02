import matplotlib.pyplot as plt
from day06_graph.daoStock import DaoStock
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ds = DaoStock()
names = []
for i in ds.nameList():
    names.append(i['s_name'])

prices = []
# for i in names:
#     prices.append(ds.selectArr(i))
    
for i in range(len(names)):
    prices.append(ds.selectArr(names[i]))

# prices.append(ds.selectArr('LG'))
# prices.append(ds.selectArr('삼성전자'))
# prices.append(ds.selectArr('SK'))
# prices.append(ds.selectArr('마니커'))
# prices.append(ds.selectArr('서울식품'))
    cnt_t = len(prices[i])
    xs = np.ones(cnt_t)
    ys = list(range(cnt_t))

# for i in range(len(names)):
    ax.plot(xs*i, ys, prices[i],"")

# ax.plot(xs*0, ys, prices[0], '')
# ax.plot(xs*1, ys, prices[1], '')
# ax.plot(xs*2, ys, prices[2], '')
# ax.plot(xs*3, ys, prices[3], '')
# ax.plot(xs*4, ys, prices[4], '')

plt.show()