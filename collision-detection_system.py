import TMMC_Wrapper
import rclpy
import numpy as np
import math
from ultralytics import YOLO

if not rclpy.ok():
    rclpy.init()

TMMC_Wrapper.is_SIM = False
if not TMMC_Wrapper.is_SIM:
    TMMC_Wrapper.use_hardware()

    if "robot" not in globals():
        robot = TMMC_Wrapper.Robot()

        print("running main")

        robot.start_keyboard_control() 
        model = YOLO('yolov8n.pt')
        rclpy.spin_once(robot, timeout_sec=0.1)

        stop_sign_flag = False
        robot.send_cmd_vel(1.0, 0.0)

        scan = robot.checkScan()
        th1 = 45
        th2 = 90
        min_dist = 0.05

        try:
            print("Listening for keyboard events. Press keys to test, Ctrl+C to exit")
            while True:
                rclpy.spin_once(robot, timeout_sec=0.1)
                img = robot.rosImg_to_cv2()
                tags = robot.detect_april_tag_from_img(img)
                print(tags)

                result = robot.lidar_data_too_close(scan, th1, th2, min_dist)

                if result:
                    dist_obstacle = min(scan[th1:th2])

                    velocity_x = 0.0
                    velocity_phi = 0.0
                    duration = 2.0
                    robot.set_cmd_vel(velocity_x, velocity_phi, duration)

                    velocity_x = -0.5
                    velocity_phi = 0.0
                    duration = 5.0
                    robot.set_cmd_vel(velocity_x, velocity_phi, duration)

                if 7 in tags.keys():
                    robot.set_cmd_vel(0.0, 1, 0.5)
                    robot.send_cmd_vel(1, 0)
                    tags[7] = None

                if 3 in tags.keys():
                    robot.set_cmd_vel(0.0, 1, 0.5)
                    robot.send_cmd_vel(1, 0)

                if 6 in tags.keys():
                    robot.set_cmd_vel(0.0, 1, 0.5)
                    robot.send_cmd_vel(1, 0)
                    tags[6] = None

                img = robot.rosImg_to_cv2()
                stop_sign_detected, x1, y1, x2, y2 = robot.ML_predict_stop_sign(model, img)
                stop_dist = robot.lidar_data_too_close(robot.checkScan(), 45, 90, 0.3)

                if stop_sign_detected and stop_sign_flag and stop_dist <= 0.3:
                    robot.stop_keyboard_control()
                    print('stop sign')
                    robot.set_cmd_vel(0.0, 0.0, 2)
                    robot.start_keyboard_control()
                    stop_sign_flag = False
                if not stop_sign_detected:
                    stop_sign_flag = True

        except KeyboardInterrupt:
            print("Keyboard interrupt received. Stopping...")
        finally:
            # When exiting program, run the kill processes
            robot.stop_keyboard_control()
            robot.destroy_node()
            rclpy.shutdown()
