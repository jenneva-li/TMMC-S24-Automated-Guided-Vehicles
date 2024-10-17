# TMMC-S24-Automated-Guided-Vehicles

<p align="center">
  <img src = https://github.com/Jenneva-Li/TMMC-S24-Automated-Guided-Vehicles/assets/164729882/3073d63b-bb8b-4f06-9154-10cced951ddf width="700px">
</p>



## Introduction[![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#introduction)

The Toyota Motor Manufacturing Canada (TMMC) Engineering project team aims to implement a reliable solution for utilizing Automated Guided Vehicles (AGVs) to efficiently transport vehicle components to designated stations within a manufacturing environment. The AGVs must navigate from pickup to delivery points while avoiding collisions with static fixtures and other AGVs, and obeying traffic signals, such as stop signs. The primary objective is to minimize the time required for each delivery, ensuring a streamlined and efficient workflow.


https://github.com/user-attachments/assets/9f1b7ade-96e1-41d2-84a2-8c7f49eb4185

## Project Overview[![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#overview)

* **Collision Avoidance:** This was the first phase of the project. The robot was programmed to navigate an obstacle course while avoiding collisions with obstacles. Utilizing its LiDAR sensor, the robot successfully detected obstacles in real-time and adjusted its path accordingly. It was also programmed to halt and reverse when it encountered an obstacle.
* **Stop Sign Recognition: **For the second phase, the built in camera system in the TurtleBot was used to identify stop signs placed throughout the obstacle course. The robot was trained using YOLO machine learning model to recognize the stop signs and come to a complete stop. This feature is crucial for enhancing safety and compliance in autonomous navigation.
* **Autonomous Navigation: **The next goal was then to create a fully autonomous loop around the obstacle course. The team successfully simulated the robot's path using a pre-scanned map obtained from the LiDAR sensor, allowing it to plan an efficient route to the designated destination.
---
## Challenges and Solutions[![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#challenges)
One of the biggest challenges was implementing AprilTags into the system, which was essential for guiding the robot's movements around the partial test course. The Turtlebot's LiDAR camera was capable of recognizing AprilTags and capturing images of them; however, the Turtlebot failed to respond to all AprilTags. Each tag was intended to trigger a specific movement function. For instance, upon detecting an AprilTag, the robot was supposed to turn and move a designated distance around the partial test course. This problem was later resolved by refining the code to assign a unique key to each scanned AprilTag image. 
---

https://github.com/user-attachments/assets/5d4cc9f6-c880-45b5-8eff-aba5789585ab



---
<div align="right">[ <a href="#introduction">↑ Back to top ↑</a> ]</div>
