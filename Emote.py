from Igor import *
from time import sleep
from notify import *

#High level emotion expressions.

class IgorEmote:

    def __init__(self):
        self.igor = Igor()
        self.notify = Notify()
        pass

    #wake_up: LED control that appears to be waking up with blinking.
    def wakeup(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).blink()
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.notify.output('Eyes are...\nAwake!',['all'])

    def glare(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.notify.output('Eyes are...\nGlaring!!',['all'])

    def angry(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).blink()
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.notify.output('Eyes are...\nAngry!!',['all'])

    def surprised(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.notify.output('Eyes are...\nSurprised!!',['all'])


    def sleepy(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        pass

    def shy(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).blink()
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        pass

    def sad(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).blink()
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).blink()
        self.igor.Eyes(lid,rid,maxbrightness,rate).close()
        pass

    def happy(self,lid,rid,maxbrightness,rate=0):
        pass

    def fear(self,lid,rid,maxbrightness,rate=0):
        pass

    def love(self,lid,rid,maxbrightness,rate=0):
        pass

    def content(self,lid,rid,maxbrightness,rate=0):
        pass

    def bored(self,lid,rid,maxbrightness,rate=0):
        pass

    def nervous(self,lid,rid,maxbrightness,rate=0):
        pass

    def confused(self,lid,rid,maxbrightness,rate=0):
        pass

    def gotosleep(self,lid,rid,maxbrightness,rate=0):
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).open()
        self.igor.Eyes(lid,rid,maxbrightness,rate).close()
        self.notify.output('Eyes are...\nAsleep!!',['all'])

    def walk(self,gpio1,gpio2,gpio3,gpio4,rate=2):
        self.igor.Legs(gpio1,gpio2,gpio3,gpio4,rate).walk()

if __name__ == '__main__':
    emote = IgorEmote()
    #Set the left and right GPIO ID, 
    #max brightness 0-1 and the rate 0-< 
    #at which the animation should run
    emote.wakeup(17,18,1,.02)
    emote.glare(17,18,.2,1)
    emote.angry(17,18,1,.02)
    #emote.sad(17,18,.2,1)
    #emote.shy(17,18,.5,.05)
    #emote.sleepy(17,18,.05,.02)
    emote.surprised(17,18,1,.5)
    emote.gotosleep(17,18,0,.25)