import machine
from machine import Pin, I2C
import time

class sound_sensor:
    def __init__(self, adc_pin, limit):
        self.pin = machine.ADC(adc_pin)
        self.count = 0
        self.limit = limit
        self.value_list = []
        
    def check_loudness(self):
        value = self.pin.read_u16()
        self.value_list.append(value)
        self.count += 1
        max_value = 0
        if self.count > self.limit:
            max_value = max(self.value_list)
            print("loudness:{}".format(max_value))
            self.count = 0
            self.value_list = []
        return max_value        

    def detect_loud(self, thresh):
        check = False
        max_value = self.check_loudness()
        if max_value > thresh:
            check = True
        
        
        return check
    
    
if __name__ == '__main__':
    
    # Raspberry Pi Picoの26ピン=ADC0
    pin26 = machine.ADC(0)
    pin25 = machine.Pin(25, Pin.OUT)
    pin1 = machine.Pin(1, Pin.OUT)

    # def setpin(pin1,pin25):
        
    # value = 0
    # value_add = 0
    # value_list = []
    # count = 0
    sound = sound_sensor(adc_pin=0, limit=10000)

    while True:
        if sound.detect_loud(thresh=20000):
            pin1.value(1)
            time.sleep(1)
        else:
            pin1.value(0)
        

            
            

