from gpiozero import PWMLED
from time import sleep

#Core library of basic controllers and animations.

class Igor:

    class Eyes:

        def __init__(self,lid='',rid='',maxBrightness=1,rate=0):
            self.lled = PWMLED(lid)
            self.rled = PWMLED(rid)
            self.rate = rate
            self.brightnessSteps = 20
            self.brightnessInc = maxBrightness / self.brightnessSteps

        def open(self):
            #Go from off to on at rate
            brightness = 0 #Default brightness
            count = 0

            while count <= self.brightnessSteps:
                self.lled.value = brightness
                self.rled.value = brightness             
                sleep(self.rate)
                count = count + 1
                brightness = brightness + self.brightnessInc
                if brightness >= 1:
                    brightness = 1 #gpiozero does not like 1.0

        def close(self):
            #Go from on to off at rate
            brightness = 1 #Default brightness
            count = 0

            while count <= self.brightnessSteps:
                self.lled.value = brightness
                self.rled.value = brightness             
                sleep(self.rate)
                count = count + 1
                brightness = brightness - self.brightnessInc
                if brightness <= 0:
                    brightness = 0 #gpiozero does not like < 0

        def blink(self):
            #Go from open to close to open at rate
            self.open()
            sleep(.3)
            self.close()
            sleep(.3)
            self.open()

    class Legs:

            def __init__(self,gpio=''):
                self.gpio = gpio
                pass

            def rotate(degrees=30):
                #todo
                pass

    class Arms:

            def __init__(self,gpio=''):
                self.gpio = gpio
                pass

            def rotate(degrees=30):
                #todo
                pass

