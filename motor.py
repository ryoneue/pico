from machine import PWM, Pin
import time
from sound import sound_sensor

# pin26 = machine.ADC(0)
servo1 = PWM(Pin(22))
servo1.freq(50)

sound = sound_sensor(adc_pin=0, limit=10000)

max_duty = 65025
dig_0 = 0.0725    #0°
dig_90 = 0.12     #90°

while True:
#     loudness = pin26.read_u16()
#     print(sound.detect_loud(thresh=20000))
    if sound.detect_loud(thresh=20000):
        print("ok")
        servo1.duty_u16(int(max_duty*dig_0))
        time.sleep(1)
        servo1.duty_u16(int(max_duty*dig_90))
        time.sleep(1)

    else:
        servo1.duty_u16(0)