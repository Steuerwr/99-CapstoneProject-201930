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
import math

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
    # : Put your GUI onto your frame (using sub-frames if you wish).
    #forward_distance_button = ttk.Button(frame, text="Forward Distance")
    #forward_distance_button.grid()
    #forward_distance_button["command"] = lambda: MyLaptopDelegate.handle_forward_distance(
     #   speed_entry, distance_entry, mqtt_sender)

    #distance_entry = ttk.Entry(frame)
    #distance_entry.insert(0, "100")
    #distance_entry.grid()

    #speed_button = ttk.Button(frame, text="Speed")
    #speed_button.grid()
    #speed_entry = ttk.Entry(frame)
    #speed_entry.insert(0, "100")
    #speed_entry.grid()

    direction_label = ttk.Label(frame, text="Choose a direction: ")
    direction_label.grid()

    forwards_button = ttk.Button(frame, text="Forwards")
    forwards_button.grid(row=2, column=0)

    backwards_button = ttk.Button(frame, text="Backwards")
    backwards_button.grid(row=2, column=1)

    speed_label = ttk.Label(frame, text='Enter speed')
    speed_label.grid()
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid()

    distance_label = ttk.Label(frame, text='Enter distance')
    distance_label.grid()
    distance_box = ttk.Entry(frame, width=8)
    distance_box.grid()

    function_label = ttk.Label(frame, text='Move until...')
    function_button = ttk.Button(frame, text='Move')
    frame_label.grid()
    function_label.grid()
    function_button.grid()

    forwards_button["command"] = lambda: MyLaptopDelegate.forward(speed_entry, distance_box, mqtt_sender)
    backwards_button["command"] = lambda: MyLaptopDelegate.backward(speed_entry, distance_box, mqtt_sender)
    function_button["command"] = lambda: MyLaptopDelegate.move_until(speed_entry, distance_box, mqtt_sender)

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

    def forward(speed_entry, distance_box, mqtt_sender):
        speed = speed_entry.get()
        distance = distance_box.get()
        mqtt_sender.send_message("move_forward", [speed, distance])

    def backward(speed_entry, distance_box, mqtt_sender):
        speed = speed_entry.get()
        distance = distance_box.get()
        mqtt_sender.send_message("move_backward", [speed, distance])

    def move_until(speed_entry, distance_box, mqtt_sender):
        speed = speed_entry.get()
        distance = distance_box.get()
        mqtt_sender.send_message("move_until", [speed, distance])
    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
