import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

rospy.init_node('application',anonymous=True)
client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
client.wait_for_server()


goal= MoveBaseGoal()
goal.target_pose.header.frame_id='map'
goal.target_pose.header.stamp = rospy.Time.now()
x= [12.9,   -11.4,  -20.9, -19.3,  15.4,1.0]
y= [-42.1,  -42.1,  -18.2,  17.2,  20.8,-1.0]
yaw= [0.0,  1.2,    -0.5,   -2.1,   1.57,1.2]
i=0
while True:
    
    goal.target_pose.pose.position.x = x[i] 
    goal.target_pose.pose.position.y = y[i]
    goal.target_pose.pose.orientation.z = yaw[i]
    goal.target_pose.pose.orientation.w=-1.0
    print("Move to Point x={}, y={}".format(x[i],y[i]))
    client.send_goal(goal)
    wait = client.wait_for_result()
    i+=1
    if i==len(x):
        i=0