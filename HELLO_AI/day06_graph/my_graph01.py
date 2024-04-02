import matplotlib.pyplot as plt
from day06_graph.datas import Datas

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')




dt = Datas()


samsung = dt.points(0,"삼성전자")
x1 = samsung[0]
y1 = samsung[1]
z1 = samsung[2]
lg = dt.points(1,"LG")
x2 = lg[0]
y2 = lg[1]
z2 = lg[2]
sk = dt.points(2,"SK")
x3 = sk[0]
y3 = sk[1]
z3 = sk[2]
han = dt.points(3,"한화")
x4 = han[0]
y4 = han[1]
z4 = han[2]
pos = dt.points(4,"포스코퓨처엠")
x5 = pos[0]
y5 = pos[1]
z5 = pos[2]
# lg = dt.selectDatas("LG")
# sk = dt.selectDatas("SK")
# hanhwa = dt.selectDatas("한화")
# posco = dt.selectDatas("포스코퓨처엠")




ax.plot(x1, y1, z1, '')
ax.plot(x2, y2, z2, '')
ax.plot(x3, y3, z3, '')
ax.plot(x4, y4, z4, '')
ax.plot(x5, y5, z5, '')
#ax.plot([x1, x2, x3], [y1, y2, y3], [z1, z2, z3], '')

plt.show()