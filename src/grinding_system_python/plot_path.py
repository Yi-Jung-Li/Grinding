import matplotlib.pyplot as plt
import numpy as np

fileName = 'path/grinding/plate_grinding_1018.csv'
path = np.loadtxt(fileName, delimiter=',', usecols=(2,3,4))
print(len(path))
z = path[:,-1]

# fig, ax = plt.subplots()
# ax.plot(z)
# # plt.axhline(y=-5, color='r')
# ax.set_title('pose_z')
# # ax.legend(['original', 'filtered'])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_title('tool_position')
ax.plot(path[:,0], path[:,1], path[:,2], 'o-b')

plt.show()