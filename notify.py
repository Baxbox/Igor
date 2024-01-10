
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import logging
from datetime import datetime

class Notify:

    def __init__(self):
        self.now = datetime.utcnow().strftime("%Y-%m-%d")
        self.logfilename = "logs/" + self.now + ".notify.log"
        logging.basicConfig(filename=self.logfilename,level=logging.DEBUG)

    def lcd_setup(self):
        self.mcp = PCF8574_GPIO(0x3F)
        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=self.mcp)
        self.mcp.output(3,1)     # turn on LCD backlight
        self.lcd.begin(16,2)     # set number of LCD lines and columns
        self.lcd.setCursor(0,0)  # set cursor position

    def print_lcd(self):
        self.lcd_setup()
        self.destroy()
        self.lcd.message(self.msg)

    def log_it(self):
        self.now_seconds = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
        logging.debug(self.now_seconds + "\t" + self.msg.strip().replace("\n",'<NEWLINE>'))

    def output(self,msg,type):
        self.msg = msg
        if 'all' in type or 'print' in type:
            print(msg)

        if 'all' in type or 'lcd' in type:
            self.print_lcd()

        if 'all' in type or 'log' in type:
            self.log_it()

    def destroy(self):
        self.lcd.clear()
    

