# Ros_Wego_nav


1. Morai 실행
2. sensor (Lidar - Ros frame_id = lidar)
3. roslaunch rosbridge_server rosbridge_websokect.launch
4. roslaunch kw_tf tf_setting.launch
5. roslaunch point_cloud_to_laserscan sample_node.launch
6. roslaunch kw_tf navigation.launch
   
이렇게 까지 하면 rviz가 켜지고 목적지 설정하면 로봇이 자동으로 경로를 계획하고 이동함
---

WayPoint Move(ros action 사용)

7. (kw_slam_ws)에 있다고 가정 cd src/kw_tf/scripts/
8. python application.py -> 지정된 Waypoint로 이동


### 만약에 경로가 생기고 안움직이면 Morai -에서 Automode로 변경
### Lidar 맵이 생기지 않는다 -> sudo apt install ros-slam-gmapping 설치
