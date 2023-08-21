# Wego Scout MiniK Lidar Navigation

## 목표
- Lidar를 이용해서 맵핑이 된 맵내에서 목적지를 설정하면 자동으로 로봇이 경로를 계산해서 움직이게 하는 Navigating 주행 구현

## How to Launch?

1. Morai 실행
2. sensor (Lidar - Ros frame_id = lidar) 연결 
3. source devel/setup.bash -> 없으면 catkin_make
4. roslaunch rosbridge_server rosbridge_websokect.launch
5. roslaunch kw_tf tf_setting.launch
6. roslaunch point_cloud_to_laserscan sample_node.launch
7. roslaunch kw_tf navigation.launch
   
이렇게 까지 하면 rviz가 켜지고 목적지 설정하면 로봇이 자동으로 경로를 계획하고 이동함
---

## 주요 알고리즘 및 프로그램
   1. AMCL(Adaptive Monte Carlo Localization)
      - 로봇의 위치를 추정하고 보정하기 위해서 만든 알고리즘
      - Lidar로부터 받은 데이터에 Paticle 필터를 이용해서 로봇의 위치를 확률적으로 계산
   2. DWA(Dynamic Window Approach)
      - 로봇의 속도 탐색 영역에서 로봇과 충돌 가능한 장애물을 회피 하면서, 목표점까지 빠르게 도달할 수 있는 속도를 선택
   4. Odometry(ROS Open Source, 주행기록계) - 로봇의 처음위치는 모르나, 이동한 거리,이동한 좌표, 각각의 모터에 걸린 속도 등을 저장한다. 
   5. costmap (ROS Open Source, 충돌방지 및 경로 최적화) - 아래 사진을 보면 빨간부분은 실제로 장애물을 뜯하고, 파란 부분은 충돌를 방지하고자 장애물 주변으로 설정해놓는 금지구역이다. 이 파란 영역을 얼마나 넓게 설정하거나 좁게 설정하는것에 따라 로봇의 경로 계획이 달라지며, 그에 따른 최단거리 및 최단시간이 변화한다.
   <img src="./image/costmap.png" title="costmap img" width="300px" height="200px" align="left">

# Gmapping 

<img src="./image/gmapping.gif" title="Gmapping Start" alt="GMS">
- Gmap 세이브

---

<img src="./image/gmapping_navi.gif" title="Gmapping Navi Start" alt="GMSN">
- Gmap 네비게이션

# WayPoint Move(ros action 사용)

8. (kw_slam_ws)에 있다고 가정 cd src/kw_tf/scripts/
9. python application.py -> 지정된 Waypoint로 이동
<img src="./image/application.png" width="600px" height="400px" title="Application Code Img" alt="Code">

### 만약에 경로가 생기고 안움직이면 Morai Drive Info에서 Automode로 변경
### Lidar 맵이 생기지 않는다 -> sudo apt install ros-slam-gmapping 설치
Ros_Point Move Demo

<img src="./image/point_navigator.gif" title="point_navi" alt="Navi">
[Demo](https://drive.google.com/file/d/1g06gLS2Wv0s3-Mejqg12iqbUHV-qZH5K/view?usp=sharing)
