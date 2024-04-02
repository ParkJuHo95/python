import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot([0,0,0], [0,2,4], [0,5,0], 'r')
ax.plot([1,1,1], [0,2,4], [0,-5,0], 'y')
ax.plot([2,2,2], [0,2,4], [0,0,0], '')

plt.show()