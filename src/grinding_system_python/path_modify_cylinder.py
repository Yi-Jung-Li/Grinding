import numpy as np

path_file = 'path/polishing/new/cylinder/cylinder_d30_quater'
original_path = np.genfromtxt(path_file+'.csv', delimiter=',')
num_path = len(original_path)

print(original_path)
### for d40
# for i in range(num_path//18): # 18 for d40
#     p = original_path[i*18+9: i*18+18]
#     p_modify = p[np.ix_([8,7,6,5,4,3,2,1,0])] #for d40
#     original_path[i*18+9: i*18+18] = p_modify

### for d30
for i in range(num_path//24):
    p = original_path[i*24+12: i*24+24]
    p_modify = p[np.ix_([11,10,9,8,7,6,5,4,3,2,1,0])]
    original_path[i*24+12: i*24+24] = p_modify

### the lift point is too high, make them lower
lift_point = [0,11,12,23,24,35]
for i in lift_point:
    original_path[i,4] = original_path[i,4] - 150

# np.savetxt('path/polishing/10degree_3traj.csv', original_path, fmt='%s', delimiter=',')

np.savetxt(path_file+'_modify.csv', original_path, delimiter=',', fmt='%f')