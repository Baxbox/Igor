from gpiozero import PWMLED
from time import sleep

#Core library of basic controllers and animations.

class Igor:

    class Eyes:

        def __init__(self,lid='',rid=''):
            self.lled = PWMLED(lid)
            self.rled = PWMLED(rid)
            self.brightnessSteps = 20
            self.brightnessInc = 1 / self.brightnessSteps

        def open(self,rate=0):
            #Go from off to on at rate
            brightness = 0 #Default brightness
            count = 0

            while count <= self.brightnessSteps:
                self.lled.value = brightness
                self.rled.value = brightness             
                sleep(rate)
                count = count + 1
                brightness = brightness + self.brightnessInc
                if brightness >= 1:
                    brightness = 1 #gpiozero does not like 1.0

        def close(self,rate=0):
            #Go from on to off at rate
            brightness = 1 #Default brightness
            count = 0

            while count <= self.brightnessSteps:
                self.lled.value = brightness
                self.rled.value = brightness             
                sleep(rate)
                count = count + 1
                brightness = brightness - self.brightnessInc
                if brightness <= 0:
                    brightness = 0 #gpiozero does not like < 0

        def blink(self,rate=0):
            #Go from open to close to open at rate
            self.open(rate)
            sleep(.3)
            self.close(rate)
            sleep(.3)
            self.open(rate)

