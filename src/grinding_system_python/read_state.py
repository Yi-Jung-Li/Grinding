import os
import json
from turtle import pos
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import yaml
from yaml.loader import SafeLoader
from scipy import signal

def read_plan(fname):
  with open(fname, 'r') as f:
    plan = list(yaml.load_all(f, Loader=SafeLoader))
  
  trajectory_times = []
  # print(plan[2]['joint_trajectory']['points'][1]['time_from_start']['nsecs'])
  for _, p in enumerate(plan):
    nsec = p['joint_trajectory']['points'][-1]['time_from_start']['nsecs']
    sec = p['joint_trajectory']['points'][-1]['time_from_start']['secs']
    time = round(sec + nsec*10**-9,3)
    trajectory_times.append(time)
  return trajectory_times
  
def read_json(fname, T=False, Speed=False):
    with open(fname) as jsonfile:
        feedback = json.load(jsonfile)

    # print(len(feedback))

    tool_poses = []
    tcp_forces = []
    joint_tors = []
    if T:
        times = []
        time0 = feedback[0]["time"]
    if Speed:
        tcp_speed = []
    for _, f in enumerate(feedback):
        if T:
            time = f["time"] - time0
            times.append(time)
        speed = f['tcp_speed']
        pose = f['tool_pose']
        force = f['tcp_force']
        tor = f['joint_tor']
        tool_poses.append(pose)
        tcp_forces.append(force)
        joint_tors.append(tor)
        if Speed:
            tcp_speed.append(speed)

    tool_poses = np.array(tool_poses)
    tcp_forces = np.array(tcp_forces)
    joint_tors = np.array(joint_tors)
    if Speed:
        tcp_speed = np.array(tcp_speed)

    if T:
        times = np.array(times)
        if Speed:
            return tool_poses, tcp_forces, joint_tors, times, tcp_speed
        return tool_poses, tcp_forces, joint_tors, times
    else:
        return tool_poses, tcp_forces, joint_tors

def read_csv(fname):
    force_data = np.loadtxt(fname, delimiter=',', usecols=(5,6,7,11,12,13), skiprows=1)
    force_sensor = force_data[:,:3]
    force_sensor_filter = force_data[:,3:]
    # force_x = force_data[:,0]
    # force_y = force_data[:,1]
    # force_z = force_data[:,2]
    # force_x_filter = force_data[:,3]
    # force_y_filter = force_data[:,4]
    # force_z_filter = force_data[:,5]
    # return force_x, force_y, force_z, force_x_filter, force_y_filter, force_z_filter
    return force_sensor, force_sensor_filter

def plot_data(data, title="", poseZ=None, legend=None):
    num_data = len(data)
    color = ['-b', '-r', '-o']
    ####　plot tcp_force
    if poseZ:
        fig, axs = plt.subplots(4, 1, sharex=True)
    else:
        fig, axs = plt.subplots(3, 1, sharex=True)
    # fig.subplots_adjust(hspace=0) # Remove vertical space between axes
    axs[0].set_title(title)
    for i in range(num_data):
        axs[0].plot(data[i][:,0], color[i], linewidth=1.0)
        axs[1].plot(data[i][:,1], color[i], linewidth=1.0)
        axs[2].plot(data[i][:,2], color[i], linewidth=1.0)
    if legend:
        axs[0].legend(legend)
    if poseZ:
        for i in range(len(poseZ)):
            axs[3].plot(poseZ[i], color[i])
        # axs[3].set_title("pose_z")
    # if pose:
    #     #### plot tool_pose
    #     fig = plt.figure()
    #     ax = fig.add_subplot(projection='3d')
    #     ax.set_title('tool_position')
    #     ax.scatter(tool_poses[:,0], tool_poses[:,1], tool_poses[:,2])

def seperate_trajectory(poses, times, seperate_t, speed=None):
    SPEED =  speed.any()
    if len(seperate_t)%2 != 0:
        print('len(seperate_t) is not even !!!')
        return 
    print(len(seperate_t))
    trajectory_all = []
    if SPEED:
        tcp_speed_all = []
        tcp_speed_tmp = []
    i = 0
    traj_tmp = []
    traj_i = 0 # 紀錄軌跡數量
    while i < len(poses) and traj_i<len(seperate_t)/2:
        while times[i] > seperate_t[traj_i*2]: # 當時間大於開始時間，將接下來的軌跡紀錄，直到超過結束時間
            traj_tmp.append(poses[i,:])
            if SPEED:
                tcp_speed_tmp.append(speed[i,:])
            if times[i] > seperate_t[traj_i*2+1] or i == len(poses)-1:
                trajectory_all.append(traj_tmp)
                traj_tmp = []
                traj_i += 1
                if SPEED:
                    tcp_speed_all.append(tcp_speed_tmp)
                    tcp_speed_tmp = []
                # print(traj_i)
                break
            i+=1
        i+=1

    if SPEED:
        return trajectory_all, tcp_speed_all
    else:
        return trajectory_all

def plot_force_data(data, path_time, exp_name):
    # 畫出2*3的subplot: 全部範圍和5道軌跡
    ## data: 力規的z方向力, path_time:

    sos = signal.butter(2, 10, fs=1000,output='sos')
    filtered_data = signal.sosfilt(sos, data)

    fig = plt.figure(tight_layout=True)
    gs = gridspec.GridSpec(2, 5)
    ax = fig.add_subplot(gs[0, :])
    ax.plot(data[int(path_time[0])*1000:int(path_time[-1]*1000)], label='original')
    ax.plot(filtered_data[int(path_time[0])*1000:int(path_time[-1]*1000)], label='filtered')
    # for i in range(1,len(path_time)):
    #     plt.axvline(x=(path_time[i]-path_time[0])*1000, color='g')
    ax.set_ylim(-13,2.5)
    plt.axhline(y=-5, color='r')
    ax.set_ylabel('Force (N)')
    ax.legend()

    path_time = path_time[np.array([1,2,5,6,9,10,13,14,17,18])]
    path_time = (np.rint(path_time*1000)).astype(int)
    for i in range(len(path_time)//2):
        ax = fig.add_subplot(gs[1, i])
        ax.plot(data[path_time[i*2]:path_time[i*2+1]+300])
        ax.plot(filtered_data[path_time[i*2]:path_time[i*2+1]+300])
        ax.set_ylim(-13,2.5)
        plt.axhline(y=-5, color='r')

    fig.suptitle(exp_name, fontsize=16)

if __name__ == '__main__':
    exp = 'state' 
    ROS_file = '.'
    feedback_fileName = f'{ROS_file}/feedback.json'
    grinding_times_fileName = f'{ROS_file}/grinding_times.csv'
    cmd_file = 'trajectory/grind_cmd_modify0.5_1115.csv'
    minirobot_file = f'學新數據/grinding/20221213/minirobot/{exp}.csv'

    ## 讀取手臂收回的feedback (pose, tcp_speed, time)
    tool_poses, _, _, times, tcp_speed = read_json(feedback_fileName, T=True, Speed=True)
    tool_poses = tool_poses*1000
    tcp_speed = tcp_speed*1000
    pose_x = tool_poses[:,0]
    pose_y = tool_poses[:,1]
    pose_z = tool_poses[:,2]

    ## 讀取五道研磨軌跡的開始與結束時間
    grinding_times = np.loadtxt(grinding_times_fileName, delimiter=',')
    # seperate_time = grinding_times[np.array([1,2,5,6,9,10])] # 四個時間為一組軌跡，每一組軌跡的研磨部分依序為：1和2, 5和6......
    seperate_time = grinding_times[np.array([1,2,5,6])]
    
    ## 讀取手臂command
    # grind_cmd = np.loadtxt(cmd_file, delimiter=',')
    # cmd_x = grind_cmd[:,2]
    # cmd_y = grind_cmd[:,3]
    # cmd_z = grind_cmd[:,4]

    ## 利用開始與結束時間，將 feedback 中的 pose 與速度分段 (目前是五段)
    trajectory_all, tcp_speed_all = seperate_trajectory(tool_poses, times, seperate_time, tcp_speed)
    print(len(tcp_speed_all))
    # print(trajectory_all[0])

    print(exp)
    ## 將分段後的速度對 x,y,z 方向做平均，最後算出總平均速度
    for i in range(len(tcp_speed_all)):
        tmp = np.array(tcp_speed_all[i])
        print(f'Trajectory {i}:')
        print('mean of speed_x: ', np.mean(tmp[20:,0]))
        print('mean of speed_y: ', np.mean(tmp[20:,1]))
        print('mean of speed_z: ', np.mean(tmp[20:,2]))
        print('mean of speed: ', np.mean(np.sqrt(np.square(tmp[20:,0])+np.square(tmp[20:,1])+np.square(tmp[20:,2]))))
        print('-----')
    fig, ax = plt.subplots()
    ax.set_title('tcp_speed')
    tcp_speed_tmp = np.array(tcp_speed_all[-2])
    tcp_speed_tmp = np.sqrt(np.square(tcp_speed_tmp[20:,0])+np.square(tcp_speed_tmp[20:,1])+np.square(tcp_speed_tmp[20:,2]))
    ax.plot(tcp_speed_tmp, '-o')
    # ax.plot(tcp_speed_tmp[:,0], '-o')

    fig, ax = plt.subplots()
    ax.set_title('pose')
    traj_tmp = np.array(trajectory_all[0])
    ax.scatter(traj_tmp[:,1], traj_tmp[:,2], s=1)

    ## 讀取研磨頭數據
    # force, _ = read_csv(minirobot_file)
    # force_z = force[:,2]
    # plot_force_data(force_z, grinding_times, exp_name=exp)

    # # 比較 cmd 與 feedback 的 pose (3d)
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # ax.set_title('tool_position')
    # # for i in range(len(trajectory_all)):
    # traj_tmp = np.array(trajectory_all[0])
    # ax.scatter(traj_tmp[:,0], traj_tmp[:,1], traj_tmp[:,2], s=1)
    # for i in range(1,11):
    #     ax.scatter(grind_cmd[i,2], grind_cmd[i,3], grind_cmd[i,4], s=10, c='r')

    # # 比較 cmd 與 feedback 的 pose (2d)
    # fig, ax = plt.subplots()
    # ax.set_title('tool_position')
    # # for i in range(len(trajectory_all)):
    # traj_tmp = np.array(trajectory_all[0])
    # ax.scatter(traj_tmp[:,1], traj_tmp[:,2], s=1)
    # for i in range(1,11):
    #     ax.scatter(grind_cmd[i,3], grind_cmd[i,4], s=10, c='r')

    # feedback_fileName = '學新數據/grinding/20221019/feedback/feedback-7.json'
    # tool_poses, _, _ = read_json(feedback_fileName)
    # tool_poses = tool_poses*1000
    # pose_x = tool_poses[:,0]
    # pose_y = tool_poses[:,1]
    # pose_z = tool_poses[:,2]
    # cmd_file = 'trajectory/grind_cmd_modify0.5_1115.csv'

    # fig, ax = plt.subplots()
    # ax.set_title('tool_position')
    # ax.scatter(pose_y[600:800], pose_z[600:800], s=1)
    # print(len(pose_z))


    # ax.scatter(cmd_x, cmd_y, cmd_z, s=10, c='r')
  # feedback_file = '學新數據/grinding/20221020/feedback_nogrinding-1.json'
  # feedback_file_grinding = '學新數據/grinding/20221019/feedback/feedback-7.json'

  # poses, forces, tors = read_json(feedback_file)
  # poses_grinding, forces_grinding, tors_grinding = read_json(feedback_file_grinding)
  # # plot_data([forces, forces_grinding], poseZ=[poses[:,2], poses_grinding[:,2]], legend=["nogrinding", "grinding"], title="tcp_force")
  # plot_data([forces_grinding-forces[:len(forces_grinding),:]], poseZ=[poses[:,2], poses_grinding[:,2]], legend=["nogrinding", "grinding"], title="tcp_force")

  # feedback_file_grinding_time = '學新數據/grinding/20221020/feedback_nogrinding_notime-1.json'
  # poses, forces, tors, times = read_json(feedback_file_grinding_time, T=True)
  # plot_data([forces], title="grinding_time")

  # force_sensor, force_sensor_filter = read_csv('學新數據/grinding/20221019/force_sensor/1019_7.csv')
  # # plot_data([force_sensor, force_sensor_filter], title="force_sensor", legend=["nofiltered","filtered"])
  # plot_data([force_sensor_filter], title="force_sensor", legend=["filtered"])
  # # #### plot joint_torque
  # # # x = [i for i in range(len(feedback))]
  # # # fig, ax = plt.subplots()
  # # # ax.set_title('joint_torque')
  # # # ax.scatter(x, joint_tors[:,0], linewidth=1.0)
  # # # ax.scatter(x, joint_tors[:,1], linewidth=1.0)
  # # # ax.scatter(x, joint_tors[:,2], linewidth=1.0)
  # # # ax.scatter(x, joint_tors[:,3], linewidth=1.0)
  # # # ax.scatter(x, joint_tors[:,4], linewidth=1.0)
  # # # ax.scatter(x, joint_tors[:,5], linewidth=1.0)
  # # # ax.legend(['j1','j2','j3','j4','j5','j6'])

    plt.show()

  # # print(tool_pose[0][0])