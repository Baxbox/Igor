from Igor import *
from time import sleep

#High level emotion expressions.

class IgorEmote:

    def __init__(self):
        self.igor = Igor()
        pass

    #wake_up: LED control that appears to be waking up with blinking.
    def wake_up(self,lid,rid,rate=0):
        self.igor.Eyes(lid,rid).open(rate)
        self.igor.Eyes(lid,rid).blink(rate)
        self.igor.Eyes(lid,rid).blink(rate)
        self.igor.Eyes(lid,rid).open(rate)

if __name__ == '__main__':
    emote = IgorEmote()
    #Set the left and right GPIO ID and the rate 0-1 
    #at which the animation should run
    emote.wake_up(17,18,.05)
