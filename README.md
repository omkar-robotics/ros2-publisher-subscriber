# ros2-publisher-subscriber
A beginner ROS2 project implementing publisher–subscriber communication using Python (rclpy).

This project demonstrates a simple Publisher and Subscriber communication using ROS2 and Python.

## Technologies Used
- ROS2 Humble
- Python
- rclpy
- std_msgs

## Project Description
A ROS2 node publishes a string message "Hello ROS2" on a topic named `chatter`.  
Another node subscribes to this topic and prints the received message in the terminal.

## Publisher Node
Publishes messages every 1 second.

Topic:
chatter

Message Type:
std_msgs/String

## Subscriber Node
Subscribes to the same topic and prints the received messages.

## How to Run

### 1. Build the workspace
colcon build

### 2. Source the workspace
source install/setup.bash

### 3. Run Publisher Node
ros2 run my_pubsub_pkg publisher

### 4. Run Subscriber Node
ros2 run my_pubsub_pkg subscriber

## Output Example

[INFO] Hello ROS2  
[INFO] Hello ROS2  
[INFO] Hello ROS2

## Author
Omkar Honrao  
Robotics & Automation Enthusiast

### Build workspace
