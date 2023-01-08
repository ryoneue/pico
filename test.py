import time
import rp2
from machine import Pin

# Define the blink program.  It has one GPIO to bind to on the set instruction, which is an output pin.
# Use lots of delays to make the blinking visible by eye.
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink2():
    wrap_target()
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()


    
# Instantiate a state machine with the blink program, at 2000Hz, with set bound to Pin(25) (LED on the rp2 board)
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(25))
sm2 = rp2.StateMachine(1, blink2, freq=10000, set_base=Pin(2))
sound = Pin(3, Pin.OUT)
sound.value(0)

# Run the state machine for 3 seconds.  The LED should blink.
# sound.toggle()
sm.active(1)
sm2.active(1)
time.sleep(8)
sm.active(0)
sm2.active(0)
# sound.toggle()

# sm.active(1)
# time.sleep(3)
# sm.active(0)

led = Pin(25, Pin.OUT)
led.value(0)
led2 = Pin(2, Pin.OUT)
led2.value(0)
