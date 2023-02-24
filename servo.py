from machine import PWM, Pin
import time
from sound import sound_sensor

class Servo():
    def __init__(self, pin, freq, pos=6700, neg=6000):
        self.servo = PWM(Pin(pin))
        self.servo.freq(freq)
        self.pos = pos
        self.neg = neg
        
    def turn_pos(self):
        self.servo.duty_u16(self.pos)

    def turn_neg(self):
        self.servo.duty_u16(self.neg)

    def stop(self):
        self.servo.duty_u16(0)
        
    def value(self, value):
        self.servo.duty_u16(value)
