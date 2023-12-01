import numpy as np

def fit_trajectory(grind_cmd):
  interp_num = 10
#   grind_start = [1,5,9,13,17]
  grind_start = [1,5,9]
  rep = np.ones(len(grind_cmd), dtype=int)
  print(rep.shape)
  
  for _, idx in enumerate(grind_start):
    rep[idx] = interp_num
  grind_cmd_interp = np.repeat(grind_cmd, repeats=rep, axis=0)
  # print(grind_cmd_modify)
  # grind_traj_z = grind_cmd[[1,2,5,6,9,10,13,14,17,18]]
  for i, idx in enumerate(grind_start):
    grind_cmd_interp[idx+9*i:idx+9*i+10, 2:5] = np.linspace(grind_cmd[idx, 2:5], grind_cmd[idx+1, 2:5], num=interp_num, endpoint=False)
  # print(grind_cmd_modify)

  return grind_cmd_interp

path_file = 'path/polishing/new/testing/plate_8.56deg'
original_path = np.genfromtxt(path_file+'.csv', delimiter=',')
num_path = len(original_path)

print(original_path)
for i in range(12//8):
    p = original_path[i*8+4: i*8+8]
    p_modify = p[np.ix_([3,2,1,0])]
    original_path[i*8+4: i*8+8] = p_modify


# np.savetxt('path/polishing/10degree_3traj.csv', original_path, fmt='%s', delimiter=',')

grind_cmd_interp = fit_trajectory(original_path)
np.savetxt(path_file+'_interp.csv', grind_cmd_interp, delimiter=',', fmt='%f')

# inverse_path = original_path[np.ix_([16,17,18,19,12,13,14,15,8,9,10,11,4,5,6,7,0,1,2,3])]
# np.savetxt('path/grinding/mason/plate_grinding_1213_x+8_inverse.csv', inverse_path, fmt='%s', delimiter=',')