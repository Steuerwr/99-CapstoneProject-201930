"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
  Spring term, 2018-2019.
"""
# TODO 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Ram Thiru")
    frame_label.grid()
    # TODO 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    spin_right = ttk.Button(frame, text='Turn Right')
    spin_right.grid()
    spin_right_speed = ttk.Entry(frame)
    spin_right['command']= lambda: handle_spin_right(mqtt_sender, entry_box_turnright_speed,entry_box_turnright_dist)


    entry_box_turnright_speed = ttk.Entry(frame)
    entry_box_turnright_speed.grid()

    entry_box_turnright_dist = ttk.Entry(frame)
    entry_box_turnright_dist.grid()


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
    #def handle_spin_right(spin_right_speed, mqtt_sender):
     #   print('spin right speed:',spin_right_speed)
      #  mqtt_sender.send_message('spin_right',[spin_right_speed.get()])



# TODO: Add functions here as needed.
def handle_spin_right(self, mqtt_sender, degrees):
    self.reset_position()

