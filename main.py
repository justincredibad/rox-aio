from pyautogui import *
import pyautogui

class Fishing:
    def __init__(self, max_fishing):
        self.max_fishing = max_fishing
        self.position = 0
        self.amount = 0

    def throw(self):
        throw_position = pyautogui.locateCenterOnScreen('image/cast.png', confidence=.8, region=(1000, 500, 200, 200))
        if throw_position != None:
            pyautogui.click(throw_position)
            print("Casting bait")
            print("Waiting")
            self.position = 1

    def pull(self):
        pull_position = pyautogui.locateCenterOnScreen('image/reel.png', confidence=.9, region=(1000, 500, 200, 200))
        if pull_position != None:
            pyautogui.click(pull_position)
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
