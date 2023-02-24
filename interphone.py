from machine import PWM, Pin
import time
from sound import sound_sensor
from servo import Servo
from lcd import LCD

def ready_message(lcd):

    lcd.show("Ready", row=1, skip=0)
    time.sleep(1)
    lcd.clear()

def off_message(lcd):
    lcd.show("PowerOff", row=1, skip=0)
    time.sleep(1)
    lcd.clear()
# def switch(pin_in=14, pin_out=15):
    
pin_in = Pin(14, Pin.IN, Pin.PULL_DOWN)

pin_out = Pin(15, Pin.OUT)
pin_out.value(1)

light = Pin(25, Pin.OUT)
light.value(0)

servo = Servo(pin=22, freq=50, pos=6700, neg=6000)
sound = sound_sensor(adc_pin=0, limit=10000)
lcd = LCD(i2c=0,scl=Pin(17),sda=Pin(16))
lcd.clear()
# lcd.show("stop", row=1, skip=0)
power = False

while True:
    
    if pin_in.value()==1:
        print(pin_in.value())
        if not power:
            ready_message(lcd)
            light.value(1)
            power = True
#             lcd.show("listening", row=1, skip=0)
        else:
            off_message(lcd)
            light.value(0)
            power = False

    if not power:
        continue


    if sound.detect_loud(thresh=20000):
#         print("run")
        lcd.show("running", row=1, skip=0)
        servo.turn_pos()
        time.sleep(0.05)
        
        servo.stop()
        time.sleep(1)
        
        servo.turn_neg()
        time.sleep(0.05)
        servo.stop()
        time.sleep(1)
        lcd.clear()
        lcd.show("stop", row=1, skip=0)

#     else:
# #         print("stop")
# #         lcd.show("stop", row=1, skip=0)
#         servo.stop()


