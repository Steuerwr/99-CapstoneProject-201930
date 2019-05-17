"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Morgan Brown.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Morgan Brown")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    arm_up_label = ttk.Button(frame, text='Arm Up')
    arm_up_label.grid()

    arm_up_Entry = ttk.Entry(frame)
    arm_up_Entry.insert(0,100)
    arm_up_Entry.grid()

    arm_calibrate_label = ttk.Button(frame, text='Arm Calibrate')
    arm_calibrate_label.grid()

    arm_calibrate_Entry = ttk.Entry(frame)
    arm_calibrate_Entry.insert(0, 100)
    arm_calibrate_Entry.grid()

    arm_to_label = ttk.Button(frame, text='Arm to')
    arm_to_label.grid()

    arm_to_Entry = ttk.Entry(frame)
    arm_to_Entry.insert(0, 100)
    arm_to_Entry.grid()

    arm_down_label = ttk.Button(frame, text='Arm Down')
    arm_down_label.grid()

    arm_down_Entry = ttk.Entry(frame)
    arm_down_Entry.insert(0, 100)
    arm_down_Entry.grid()

    colors_label = ttk.Button(frame, text='Colors')
    colors_label.grid()

    colors_Entry = ttk.Entry(frame)
    colors_Entry.grid()

    arm_up_label["command"] = lambda: handle_arm_up(arm_up_Entry, mqtt_sender)
    arm_calibrate_label["command"] = lambda: calibration(arm_up_Entry, mqtt_sender)
    arm_to_label["command"] = lambda: arms_motor_position(arm_up_Entry, arm_to_Entry, mqtt_sender)
    arm_down_label["command"] = lambda: arms_to_zero(arm_down_Entry, mqtt_sender)
    colors_label["command"] = lambda: move_to_color(colors_Entry, mqtt_sender)

    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
def handle_arm_up(arm_up_Entry, mqtt_sender):
    speed = int(arm_up_Entry.get())
    print('arm up message:', speed)
    mqtt_sender.send_message('arm_up', [speed])

def calibration(arm_up_Entry, mqtt_sender):
    speed = int(arm_up_Entry.get())
    print('arm_calibrate message:', speed)
    mqtt_sender.send_message('arm_calibrated', [speed])

def arms_motor_position(arm_up_Entry, arm_to_Entry, mqtt_sender):
    position = int(arm_to_Entry.get())
    speed = int(arm_up_Entry.get())
    print('arm_position message:', position)
    mqtt_sender.send_message('arm_position', [speed, position])

def arms_to_zero(arm_up_Entry, mqtt_sender):
    speed = int(arm_up_Entry.get())
    print('arm_down message:', arm_up_Entry)
    mqtt_sender.send_message('arm_down', [speed])

def move_to_color(color_Entry, mqtt_sender):
    color = color_Entry.get()
    print('go to color message:', color)
    mqtt_sender.send_message('go_to_color', [color])