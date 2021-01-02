
#include <PID_v1.h>
#include <ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Vector3Stamped.h>
#include <geometry_msgs/Twist.h>
#include <ros/time.h>

ros::NodeHandle nh;
double kp1=20,ki1=15,kd1=0.01;
double input1 = 0, output1 = 0, setpoint1 = 0;
double kp2=20,ki2=15,kd2=0.01;
double input2 = 0, output2 = 0, setpoint2 = 0;
PID PID1(&input1, &output1, &setpoint1, kp1, ki1, kd1, DIRECT);
PID PID2(&input2, &output2, &setpoint2, kp2, ki2, kd2, DIRECT);
unsigned long currenmillis;
unsigned long previousmillis;
#define loopTime 100
#define encoderA1 2
#define encoderB1 3
#define encoderA2 18
#define encoderB2 19
#define enA 11
#define IN1 10
#define IN2 9
#define enB 6
#define IN3 7
#define IN4 8
volatile long pos1=0;
volatile long pos2=0;
volatile long posp1=0;
volatile long posp2=0;
float demand1,demand2,demandx,demandz;
float diff1,diff2;
float differror1,differror2;
float speed_left,speed_right;












void velcallback(const geometry_msgs::Twist& vel){
   demandx=vel.linear.x;
   demandz=vel.angular.z;
  demandx=constrain(demandx,-0.25,0.25);
  demandz=constrain(demandz,-1,1);
}
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel",velcallback);
geometry_msgs::Vector3Stamped speed_msg;
ros::Publisher speed_pub("speed", &speed_msg);


void setup(){
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(speed_pub);
  pinMode(enA,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(enB,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode (encoderA1,INPUT_PULLUP);
  pinMode (encoderA2,INPUT_PULLUP);
  pinMode (encoderB1,INPUT_PULLUP);
  pinMode (encoderB2,INPUT_PULLUP);
  attachInterrupt(0,encoder1A,CHANGE);
  attachInterrupt(1,encoder1B,CHANGE);
  attachInterrupt(4,encoder2A,CHANGE);
  attachInterrupt(5,encoder2B,CHANGE);
  PID1.SetMode(AUTOMATIC);
  PID1.SetSampleTime(100);
  PID1.SetOutputLimits(-255, 255);

  PID2.SetMode(AUTOMATIC);
  PID2.SetSampleTime(100);
  PID2.SetOutputLimits(-255, 255);

  //Serial.begin(57600);

}

void loop() {
  nh.spinOnce();
  currenmillis=millis();
  if (currenmillis -previousmillis >=loopTime){
    previousmillis - currenmillis;
   /* if(Serial.available()>0){
      char c = Serial.read();
     if (c=='w'){
        demandx=0.25;
        demandz=0;
      }else if (c=='x'){
        demandx=0;
        demandz=-0.3;
      }else if(c=='a'){
        demandx=0.25;
        demandz=0.3;
        
      }else if (c=='d'){
        demandx=0.25;
        demandz=-0.3;
      }else if (c=='s'){
        demandx=0;
        demandz=0;
      }}*/
      demand1=demandx-(demandz*0.41);
      demand2=demandx+(demandz*0.41);
    diff1=pos1 -posp1;
    diff2=pos2 - posp2;
    differror1=(demand1*32)-diff1;
    differror2=(demand2*32)-diff2;
    posp1=pos1;
    posp2=pos2;
    /*Serial.print(pos1);
    Serial.print(" , ");
    Serial.print(pos2);
    Serial.print(" , ");
    Serial.print(output1);
    Serial.print(", ");
    Serial.println(output2);*/
    
    setpoint1=demand1*32;
    input1=diff1;
    PID1.Compute();
    //pwm1(output1);
    setpoint2=demand2*32;
    input2=diff2;
    PID2.Compute();
   // pwm2(output2);

  if (output1 >0){
    digitalWrite(IN1,LOW);
    digitalWrite(IN2, HIGH);
    analogWrite(enA, abs(output1));
  }else if(output1<0){
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    analogWrite(enA, abs(output1));
  }else if (input1==0){
    digitalWrite(IN1,LOW);
    digitalWrite(IN2, LOW);
    analogWrite(enA, 0);
  }


  if (output2 >0){
    digitalWrite(IN3,LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(enB, abs(output2));
  }else if(output2<0){
    digitalWrite(IN3,HIGH);
    digitalWrite(IN4,LOW);
    analogWrite(enB, abs(output2));
  }else if (input2==0){
    digitalWrite(IN3,LOW);
    digitalWrite(IN4, LOW);
    analogWrite(enB, 0);
  }
  /*if (demand1==0 and demand2==0){
    output1=0;
    output2=0;
  }*/

    
    speed_left=diff1/32;
    speed_right=diff2/32;
    //Serial.println(speed_left);
    publishSpeed(loopTime);
  }
}

void publishSpeed(double time){
  speed_msg.header.stamp=nh.now();
  speed_msg.vector.x=speed_left;
  speed_msg.vector.y=speed_right;
  speed_msg.vector.z=time/1000;
  speed_pub.publish(&speed_msg);
  nh.spinOnce();
  nh.loginfo("publishing odometry giang dep trai");
}
void encoder1A(){
  if (digitalRead(encoderA1)==HIGH){
    if (digitalRead(encoderB1)==LOW){
       pos1=pos1+1;
    }else {
      pos1=pos1-1;
    }
  }else {
    if (digitalRead(encoderB1)==HIGH){
      pos1=pos1+1;
    }else {
      pos1=pos1-1;
    }
  }
}
void encoder1B(){
  if (digitalRead(encoderB1)==HIGH){
    if (digitalRead(encoderA1)==HIGH){
       pos1=pos1+1;
    }else {
      pos1=pos1-1;
    }
  }else {
    if (digitalRead(encoderA1)==LOW){
      pos1=pos1+1;
    }else {
      pos1=pos1-1;
    }
  }
}
void encoder2A(){
  if (digitalRead(encoderA2)==HIGH){
    if (digitalRead(encoderB2)==LOW){
       pos2=pos2-1;
    }else {
      pos2=pos2+1;
    }
  }else {
    if (digitalRead(encoderB2)==HIGH){
      pos2=pos2-1;
    }else {
      pos2=pos2+1;
    }
  }
}
void encoder2B(){
  if (digitalRead(encoderB2)==HIGH){
    if (digitalRead(encoderA2)==HIGH){
       pos2=pos2-1;
    }else {
      pos2=pos2+1;
    }
  }else {
    if (digitalRead(encoderA2)==LOW){
      pos2=pos2-1;
    }else {
      pos2=pos2+1;
    }
  }
}
