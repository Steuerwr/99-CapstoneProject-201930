"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Will Steuerwald.
  Spring term, 2018-2019.
"""
# Done 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_laptop_code as m1
import m2_robot_code as m2
import m3_robot_code as m3
import math

class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    def forward(self, speed, distance):
        self.robot.drive_system.right_motor.reset_position()
        self.go(int(speed), int(speed))
        while True:
            if self.robot.drive_system.right_motor.get_position() >= (88.149 * int(distance)):
                self.robot.drive_system.stop()
                break

    def backward(self, speed, distance):
        self.robot.drive_system.right_motor.reset_position()
        self.go(-int(speed), -int(speed))
        while True:
            if abs(self.robot.drive_system.right_motor.get_position()) >= (88.149 * int(distance)):
                self.robot.drive_system.stop()
                break

    def move_until(self, speed, distance):
        self.go(int(speed), int(speed))
        while True:
            dist = self.get_distance()
            print(dist)
            if dist < int(distance):
                self.robot.drive_system.right_motor.turn_off()
                self.robot.drive_system.left_motor.turn_off()
                break
                
    def get_distance(self):
        dist = []
        max = 0
        sum = 0
        for k in range(5):
            dist = dist + [self.robot.sensor_system.ir_proximity_sensor.get_distance()]
        for k in range(len(dist)):
            if dist[k] > max:
                max = dist[k]
        min = dist[0]
        for k in range(len(dist)):
            if dist[k] < min:
                min = dist[k]
        for k in range(len(dist)):
            sum = sum + dist[k]
        sum = (sum - (max + min)) / 3
        return sum
    # TODO: Add methods here as needed.


def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

