# ZAGON IN UPORABA ROBOTA KUKA YOUBOT
## ZAGON
### ROBOT KUKA YOUBOT
Za zagon robota youbot in povezavo s ssh sledite naslednjim korakom:
1. S tipko na paltformi prižgite krmilnik (držite 1s)
2. S tipko na platformi zaženite motorje in računalnik (gumb držite, dokler se na zaslonu ne izpište **Motor On**, nato pa gumb spustite)
3. Manipulator postavite v začetno lego ( obratna smer urinega kazalca)
4. Manipulator prižgite z rdečo tipko na njegovi bazi
5. Po ~ 30 s se računalnik zažene. nanj se povežete z ukazom
``$ ssh youbot@192.168.65.59`` 
in geslom "youbot".
6. nastavite parametre:
    - ``$ export ROS_IP=192.168.65.59``
    - ``$ export ROS_HOSTNAME=192.168.65.59``
7. zaženite ROS driver:
``$ roslaunch youbot_driver_ros_interface youbot_driver.launch``

### STACIONARNI RAČUNALNIK
Za povezavo stacionarnega računalnika v ROS mrežo morate marediti naslednje korake (v vsakem reminalu ali .bashrc):
1. Nastavite parametre:
    - ``$ export ROS_IP=192.168.65.37`` (preverite ip z ukazom ``$ ip address``)
    - ``$ export ROS_HOSTNAME=192.168.65.37`` (preverite ip z ukazom ``$ ip address``)
    - ``$ export ROS_MASTER_URI=http://192.168.65.59:11311``
2. V terminal vključite svoj workspace ``$ source ~/VAJE/VR/pot_do_ws/devel/setup.bash``
    - **WS mora obvezno vsebovati paket brics_actuator**
3. Zaženite svoj node

## UPORABA KUKA YOUBOT GONILNIKOV
### VODENJE PLATFORME
Platrofmo lahko vodite hitrostno preko standardnega topica /cmd_vel:
``rostopic pub /cmd_vel geometry_msgs/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0" 
``
Lego platforme lahko dobite prek topica /tf 


### VODENJE MANIPULATORJA
Manipulator lahko vodite hitrostno, pozicijsko, ... Primer ukaza:
``rostopic pub /arm_1/arm_controller/velocity_command brics_actuator/JointVelocities "poisonStamp:
  originator: ''
  description: ''
  qos: 0.0
velocities:
- timeStamp:
    secs: 0
    nsecs: 0
  joint_uri: 'arm_joint_5'
  unit: 's^-1 rad'
  value: 0.0"``

sklepi:
- arm_joint_1
- arm_joint_2
- arm_joint_3
- arm_joint_4
- arm_joint_5

### VODENJE AKTUATORJA
Aktuator lahko vodite pozicijsko:
``rostopic pub /arm_1/gripper_controller/position_command brics_actuator/JointPositions "poisonStamp:
  originator: ''
  description: ''
  qos: 0.0
positions:
- timeStamp:
    secs: 0
    nsecs: 0
  joint_uri: 'gripper_joint_l'
  unit: 'm'
  value: 0.01" ``

sklepi:
- gripper_joint_l
- gripper_joint_r


## UGAŠANJE
### ROBOT KUKA YOUBOT
1. S kombinacijo tipk ctrl+C izklopite ROS driver
2. Ugasnite računalnik z ukazom ``$ sudo shutdown now``
3. Ugasnite manipulator z zelenim gumbom na manipulatorju (**manipulator se ob izklopu sesede, obvezno ga zadržite**)
4. Po ~ 30 s se računalnik ugasne. S črno tipko na platformi robota ugasnite (gumb držite, dokler se na zaslonu ne izpiše **System off**)
5. Preverite, da sta izklopljena baterija in napajalnik.