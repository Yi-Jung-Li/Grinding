from tf.transformations import euler_from_quaternion
import numpy as np

pose = np.loadtxt("test_eefV_v01_2/pose.csv", delimiter=' ')
pose_euler = np.array([])
print("Shape of pose: ", pose.shape)

for i in range(len(pose)):
    ori = euler_from_quaternion(pose[i][3:])

    temp_pose = np.concatenate(([pose[i][:3]], [ori]), axis=1)
    # print(temp_pose.shape)
    pose_euler = temp_pose if pose_euler.shape[0]==0 else np.append(pose_euler, temp_pose, axis=0)

print("Shape of pose_euler: ", pose_euler.shape)
np.savetxt("test_eefV_v01_2/pose_euler.csv", pose_euler, delimiter=',')