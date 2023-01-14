import machine
from machine import Pin, I2C
import time

# Raspberry Pi Picoの26ピン=ADC0
pin26 = machine.ADC(0)
pin25 = machine.Pin(25, Pin.OUT)
pin1 = machine.Pin(1, Pin.OUT)

# def setpin(pin1,pin25):
    

while True:
    value = pin26.read_u16()

    print("lightness:{}".format(value))
    time.sleep(1)
    
    if value < 8000:
        pin25.value(1)
        pin1.value(1)
    elif value < 15000:
        pin25.value(1)
        pin1.value(0)
    else:
        pin25.value(0)
        pin1.value(0)
    
        
        
