"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Morgan Brown.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_robot_code as m1
import m2_robot_code as m2


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

    def arm_up(self, speed):
        print_message_received('arm_up', [speed])
        self.robot.arm_and_claw.motor.turn_on(speed)
        while True:
            if self.robot.arm_and_claw.touch_sensor.is_pressed():
                self.robot.arm_and_claw.motor.turn_off()
                break

    def arm_calibrated(self, speed):
        self.arm_up(speed)
        self.robot.arm_and_claw.motor.reset_position()
        self.robot.arm_and_claw.motor.turn_on(-speed)
        while True:
            if abs(self.robot.arm_and_claw.motor.get_position()) >= 14.2*360:
                self.robot.arm_and_claw.motor.turn_off()
                break
        self.robot.arm_and_claw.motor.reset_position()

    def arm_position(self, speed, position):
        if self.robot.arm_and_claw.motor.get_position() >= position:
            self.robot.arm_and_claw.motor.turn_on(-speed)
            while True:
                if self.robot.arm_and_claw.motor.get_position() <= position:
                    self.robot.arm_and_claw.motor.turn_off()
                    break
        else:
            self.robot.arm_and_claw.motor.turn_on(speed)
            while True:
                if abs(self.robot.arm_and_claw.motor.get_position()) >= position:
                    self.robot.arm_and_claw.motor.turn_off()
                    break

    def arm_down(self, speed):
        self.arm_position(speed, 0)

    def go_to_color(self, color):
        self.robot.drive_system.go(50,50)
        while True:
            if self.robot.sensor_system.color_sensor.get_color_as_name() == color:
                self.robot.drive_system.stop()
                break

    # TODO: Add methods here as needed.


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

