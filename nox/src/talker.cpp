#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/Vector3.h>
#include <stdio.h>
#include <cmath>
#include <ros/time.h>
ros::Time current_time;
ros::Time speed_time(0.0);
double x = 1.0;
double y = 0.0;
double theta = 1.57;

char base_link[] = "/base_link";
char odom[] = "/odom";
int main(int argc, char **argv){
    ros::init(argc, argv, "talker");
    ros::NodeHandle  nh;
    geometry_msgs::TransformStamped t;
    tf::TransformBroadcaster broadcaster;
    while (ros::ok()){
        double dx = 0.2;
        double dtheta = 0.18;
        x += cos(theta)*dx*0.1;
        y += sin(theta)*dx*0.1;
        theta += dtheta*0.1;
        if(theta > 3.14){
         theta=-3.14;}
    
        // tf odom->base_link
        
        geometry_msgs::Quaternion empty_quat = tf::createQuaternionMsgFromYaw(0);
        geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(theta);
        t.header.frame_id = odom;
        t.child_frame_id = base_link; 
        t.transform.translation.x = x;
        t.transform.translation.y = y;
        t.transform.rotation = odom_quat;
        t.header.stamp = ros::Time::now();
        broadcaster.sendTransform(t);
        ros::spinOnce();
        usleep(100000);
    }
}