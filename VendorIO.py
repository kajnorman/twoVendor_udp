from machine import Pin
from time import sleep
class Trigger_Pin:

    def __init__(self, pin):
        self.p = pin
        self.PreviousValue = False
        self.CurrentValue = False

    def Triggered(self):
        self.CurrentValue = self.p()
        if (self.PreviousValue == False and self.CurrentValue == True):
            self.PreviousValue = self. CurrentValue
            sleep(0.015)# undgå kontaktprell
            return True
        else:
            self.PreviousValue = self.CurrentValue
            sleep(0.015)# undgå kontaktprell
            sleep(0.015)# undgå kontaktprell
            return False




