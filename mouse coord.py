import pyautogui
from pyautogui import *
import ppadb
from ppadb.client import Client
from PIL import Image
import numpy
import time
from mss import mss
from pynput.mouse import Controller,Button,Listener

def on_click(x,y,button,pressed):
    if pressed:
        print('Mouse Clicked at ({0},{1})'.format(x,y))

with Listener(on_click=on_click) as listener:
    listener.join()
