import machine
from machine import Pin, I2C
import time


class sound_sensor:
    def __init__(self, adc_pin, limit, pio=False, out_pin=25, freq=10000):
        self.pin = machine.ADC(adc_pin)
        self.count = 0
        self.limit = limit
        self.value_list = []
        self.max_value = 0
        if pio:
            from pio_timer import pio_timer
            self.freq = freq
            self.timer = pio_timer(sm=1, freq=self.freq, pin=25)
            self.out_pin = Pin(out_pin)
            self.timer.active()
        
    def check_loudness_limit(self):
        value = self.pin.read_u16()
        self.value_list.append(value)
        self.count += 1
        max_value = 0
        if self.count > self.limit:
            max_value = max(self.value_list)
#             print("loudness:{}".format(max_value))
            self.count = 0
            self.value_list = []
        return max_value        

    # pio_timer()による正確な時間計測版
    def check_loudness_time(self, msec):
#         frame = int((msec / self.freq) * 100000)
        self.timer.put(msec)
        tmp = self.limit
        self.limit = 1000
        while True:
#             print("stop")
            if self.out_pin.value()==1:
                break    
#         print("start")            
        
        while True:
#             print(Pin(25).value())
#             continue
        
#             value = self.pin.read_u16()
            value = self.check_loudness_limit()
            self.value_list.append(value)
            self.count += 1
            max_value = 0           
#             print(self.out_pin.value())
            if self.out_pin.value()==0:
                max_value = max(self.value_list)
                print("loudness:{}".format(self.value_list))
                self.count = 0
                self.value_list = []
                self.limit = tmp
                return max_value
    
    def check_loudness(self):
        return self.pin.read_u16()

    def detect_loud(self, thresh):
        check = False
        max_value = self.check_loudness_limit()
        self.max_value = max_value
        if max_value > thresh:
            check = True
        
        
        return check
    
    
if __name__ == '__main__':
    
    # Raspberry Pi Picoの26ピン=ADC0
    pin26 = machine.ADC(0)
    pin25 = machine.Pin(25, Pin.OUT)
    pin1 = machine.Pin(25, Pin.OUT)

    # def setpin(pin1,pin25):
        
    # value = 0
    # value_add = 0
    # value_list = []
    # count = 0
    sound = sound_sensor(adc_pin=0, limit=10000, pio=True, out_pin=25)
#     pin25.value(1)
    while True:
        if sound.detect_loud(thresh=5000) or True:
            pin25.off()
            
#             print(Pin(25).value())
            sound.check_loudness_time(msec=10000)
#             pin25.value(0)
            print(Pin(25).value())
#             time.sleep(1)
#             pin1.value(1)
#             time.sleep(1)
        else:
#             pin25.value(0)
            pass
        

            
            

