"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Will Steuerwald.
  Spring term, 2018-2019.
"""
# Done 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Will Steuerwald")
    frame_label.grid()
    # Done 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    forward_distance_button = ttk.Button(frame, text="Forward Distance")
    forward_distance_button.grid()
    forward_distance_button["command"] = lambda handle_forward_distance:(
        speed_entry, distance_entry, mqtt_sender)
    #forward_distance_button["command"] = lambda: handle_forward_distance(
    #    speed_entry, distance_entry, mqtt_sender)

    distance_entry = ttk.Entry(frame)
    distance_entry.insert(0, "100")
    distance_entry.grid()

    speed_button = ttk.Button(frame, text="Speed")
    speed_button.grid()
    speed_entry = ttk.Entry(frame)
    speed_entry.insert(0, "100")
    speed_entry.grid()


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

def go(mqtt_sender, direction, left_wheel_speed, right_wheel_speed):
    print()
    print("Sending a message to the robot to", direction)
    print("  using wheel motor speeds:", left_wheel_speed, right_wheel_speed)
    mqtt_sender.send_message("go", [left_wheel_speed, right_wheel_speed])

def handle_forward_distance(speed_entry_box, distance_entry_box, mqtt_sender):
    left = int(speed_entry_box.get())
    right = int(speed_entry_box.get())
    inches = int(distance_entry_box.get())
    go(mqtt_sender, "FORWARD", left, right)

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
