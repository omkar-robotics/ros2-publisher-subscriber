# 🤖 ROS2 Publisher–Subscriber Communication

🚀 A beginner **ROS2 project demonstrating Publisher–Subscriber communication using Python (rclpy)**.

This project explains the fundamental ROS2 concept where one node **publishes messages** to a topic and another node **subscribes to the same topic** to receive those messages.

---

# 📌 Project Overview

In ROS2, communication between nodes is commonly implemented using the **Publisher–Subscriber model**.

In this project:

* A **Publisher Node** sends a message `"Hello ROS2"` to a topic named **`chatter`**
* A **Subscriber Node** listens to the same topic
* The subscriber prints the received message in the terminal

This demonstrates the **basic communication mechanism between ROS2 nodes**.

---

# 🛠 Technologies Used

| Technology     | Description                   |
| -------------- | ----------------------------- |
| 🤖 ROS2 Humble | Robotics middleware framework |
| 🐍 Python      | Programming language          |
| 📡 rclpy       | ROS2 Python client library    |
| 📨 std_msgs    | Standard ROS2 message types   |

---

# ⚙️ Project Description

A ROS2 node publishes a string message **"Hello ROS2"** on a topic named:

```
chatter
```

Another node subscribes to the same topic and prints the received message in the terminal.

---

# 📂 Project Structure

```
ros2-publisher-subscriber
│
├── publisher.py
├── subscriber.py
└── README.md
```

---

# 📡 Publisher Node

The publisher node sends messages every **1 second**.

### Topic

```
chatter
```

### Message Type

```
std_msgs/String
```

The node publishes the message **"Hello ROS2"** continuously.

---

# 📥 Subscriber Node

The subscriber node listens to the **`chatter`** topic and prints the received message in the terminal.

Whenever a message is published, the subscriber immediately receives and displays it.

---

# ▶️ How to Run the Project

## 1️⃣ Build the Workspace

```
colcon build
```

---

## 2️⃣ Source the Workspace

```
source install/setup.bash
```

---

## 3️⃣ Run Publisher Node

```
ros2 run my_pubsub_pkg publisher
```

---

## 4️⃣ Run Subscriber Node

Open another terminal and run:

```
ros2 run my_pubsub_pkg subscriber
```

---

# 💻 Output Example

```
[INFO] Hello ROS2
[INFO] Hello ROS2
[INFO] Hello ROS2
```

The subscriber node continuously receives and prints messages published by the publisher node.

---

# 🎯 Learning Outcomes

This project helps understand:

* ROS2 node creation
* Publisher–Subscriber communication
* ROS2 topics
* Message passing between nodes
* Python-based ROS2 development using **rclpy**

---

# 👨‍💻 Author

**Omkar Honrao**
Robotics & Automation Enthusiast

---



