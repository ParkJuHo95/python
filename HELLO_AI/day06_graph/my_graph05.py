import matplotlib.pyplot as plt
from day06_graph.daoStock import DaoStock
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ds = DaoStock()

s_names = ["LG","삼성전자","SK","마니커","서울식품"]


prices = []

# prices.append(ds.selectArr(s_names[0]))
# prices.append(ds.selectArr(s_names[1]))
# prices.append(ds.selectArr(s_names[2]))
# prices.append(ds.selectArr(s_names[3]))
# prices.append(ds.selectArr(s_names[4]))

for i in s_names:
    prices.append(ds.selectArrN(i))
    

cnt_t = len(prices[0])

xs = np.ones((cnt_t),dtype=np.int8)
ys = list(range(cnt_t))

for idx,s in enumerate(s_names):
    tp = (prices[idx]/prices[idx][0])*100
    ax.plot(xs*idx, ys, tp,"")

# ax.plot(xs*0, ys, prices[0], '')
# ax.plot(xs*1, ys, prices[1], '')
# ax.plot(xs*2, ys, prices[2], '')
# ax.plot(xs*3, ys, prices[3], '')
# ax.plot(xs*4, ys, prices[4], '')

plt.show()