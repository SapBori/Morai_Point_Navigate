# Wego Scout Mini Inside Navigation


1. Morai 실행
2. sensor (Lidar - Ros frame_id = lidar) 연결 
3. source devel/setup.bash -> 없으면 catkin_make
4. roslaunch rosbridge_server rosbridge_websokect.launch
5. roslaunch kw_tf tf_setting.launch
6. roslaunch point_cloud_to_laserscan sample_node.launch
7. roslaunch kw_tf navigation.launch
   
이렇게 까지 하면 rviz가 켜지고 목적지 설정하면 로봇이 자동으로 경로를 계획하고 이동함
---

WayPoint Move(ros action 사용)

8. (kw_slam_ws)에 있다고 가정 cd src/kw_tf/scripts/
9. python application.py -> 지정된 Waypoint로 이동
<img src="./image/application.png" width="500px" height="500px" title="Application Code Img" alt="Code">

### 만약에 경로가 생기고 안움직이면 Morai -에서 Automode로 변경
### Lidar 맵이 생기지 않는다 -> sudo apt install ros-slam-gmapping 설치
Ros_Point Move Demo
[!Video](https://drive.google.com/file/d/1g06gLS2Wv0s3-Mejqg12iqbUHV-qZH5K/view?usp=sharing)
