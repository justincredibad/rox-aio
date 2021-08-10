import pyautogui
from pyautogui import *
import ppadb
from ppadb.client import Client
from PIL import Image
import numpy
import time
from mss import mss

adb = Client(host='127.0.0.1', port=5037) 
devices = adb.devices()


if len(devices) == 0:
    print("No device found")
    quit()

device = devices[0]

#device.shell('input tap 500 500')

class Fishing:
    def __init__(self, max_fishing):
        self.max_fishing = max_fishing
        self.position = 0
        self.amount = 0

    def throw(self):
        throw_position = pyautogui.locateCenterOnScreen('image/cast.png', confidence=.8, region=(1000, 500, 200, 200))
        if throw_position != None:
            device.shell('input tap 1083 576')
            #pyautogui.click(throw_position)
            print("Casting bait")
            print("Waiting") 
            self.position = 1

    def pull(self):
        pull_position = pyautogui.locateCenterOnScreen('image/reel.png', confidence=.9, region=(1000, 500, 200, 200))
        if pull_position != None:
            device.shell('input tap 1060 548')
            #pyautogui.click(pull_position)
            print("Reel")
            self.amount += 1
            print("Caught ", self.amount)
            self.position = 0

    def fishing(self):
        while True:
            if self.amount >= self.max_fishing:
                break
            elif self.position == 0:
                self.throw()
            elif self.position == 1:
                self.pull()

if __name__ == "__main__":
    print("Start Fishing")
    
    max_fishing = 1
    
    letsgo = Fishing(max_fishing)
    letsgo.fishing()
