from machine import Pin, I2C
from micropython import const
from sound import sound_sensor

from utime import sleep
#AQM initialized
class LCD():
    def __init__(self, i2c, scl, sda):
        self.i2c = I2C(i2c, scl=scl, sda=sda)        
        #AQM function
        self._ST7032  = const(0x3e)
        self._SETTING = const(0x00)
        self._DISPLAY = const(0x40)
        self.command = {}
        self.command["init"] = b"\x38"
        self.command["set_init"] = b"\x39"
        self.command["set_freq"] = b"\x14"
        self.command["set_contrast"] = b"\x73"
        self.command["set_vcc"] = b"\x56"
        self.command["set_folower"] = b"\x6c"
        self.command["disp_on"] = b"\x0c"
        
        self.command["disp_clear"] = b"\x01"
        self.command["reset_cursor"] = b"\x02"
        self.command["disp_1st"] = 2
        self.command["disp_2nd"] = 0
    
        orders = [self.command["init"],self.command["set_init"],self.command["set_freq"],
                  self.command["set_contrast"],self.command["set_vcc"], self.command["set_folower"],
                  self.command["init"], self.command["disp_on"], self.command["disp_clear"]]
        sleep(0.04)
        for order in orders[:6]:
            self.i2c.writeto_mem(self._ST7032, self._SETTING, order)
            sleep(0.001)
        sleep(0.2)
        for order in orders[6:]:
            self.i2c.writeto_mem(self._ST7032, self._SETTING, order)
            sleep(0.001)
        
        self.i2c.writeto_mem(self._ST7032, self._SETTING, self.command["reset_cursor"])        
        sleep(0.001)
        
    def show(self, string, row=1, skip=0):
        self.i2c.writeto_mem(self._ST7032, self._SETTING, self.command["disp_clear"])
        sleep(0.001)
        self.i2c.writeto_mem(self._ST7032, self._SETTING, self.command["reset_cursor"])
        sleep(0.001)
        if row == 1:
#             print("disp_1st")

            self.i2c.writeto_mem(self._ST7032, self._SETTING, b"\x02")

            sleep(0.001)
        elif row == 2:
#             print("disp_2nd")

            disp = bytes.fromhex(("c" + str(skip)).encode())
            self.i2c.writeto_mem(self._ST7032, self._SETTING, b"\xc0")
#             self.i2c.writeto_mem(self._ST7032, self._SETTING, disp)
            sleep(0.001)             

        for i in string:
            self.i2c.writeto_mem(self._ST7032, self._DISPLAY, i.encode())


    def shift(self, num):
        for i in range(num):
            self.i2c.writeto_mem(self._ST7032, self._SETTING, b"\x1c")
        
        
    def clear(self):
        self.i2c.writeto_mem(self._ST7032, self._SETTING, self.command["reset_cursor"])
        sleep(0.0001)
        self.i2c.writeto_mem(self._ST7032, self._SETTING, self.command["disp_clear"])

lcd = LCD(i2c=0,scl=Pin(17),sda=Pin(16))
sleep(0.001)

sound = sound_sensor(adc_pin=0, limit=1000)
#display temp data
i = 0
while 1:
    lcd.clear()
    if sound.detect_loud(thresh=10000):
#         if i == 0:
        lcd.show("OK!oK!", row=1, skip=0)
        sleep(1)
#         lcd.shift(1)    
#         i2c.writeto_mem(0x3e, 0x00, b'\x18')
#         i = abs(i - 1)
#     sleep(1)
    
    
