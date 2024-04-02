import matplotlib.pyplot as plt
from day06_graph.daoStock import DaoStock
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ds = DaoStock()

prices = []

prices.append(ds.selectArr('LG'))
prices.append(ds.selectArr('삼성전자'))
prices.append(ds.selectArr('SK'))
prices.append(ds.selectArr('마니커'))
prices.append(ds.selectArr('서울식품'))

xs = np.ones(len(ds.selectArr("LG")))


ax.plot(xs*0, [0,1,2,3,4], prices[0], '')
ax.plot(xs*1, [0,1,2,3,4], prices[1], '')
ax.plot(xs*2, [0,1,2,3,4], prices[2], '')
ax.plot(xs*3, [0,1,2,3,4], prices[3], '')
ax.plot(xs*4, [0,1,2,3,4], prices[4], '')

plt.show()