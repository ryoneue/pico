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
def toggle():
    set(x, 0)
    nop()
    # .sideset(0)
    # set(pins, abs(int(pins)-1))    [31]

# Instantiate a state machine with the blink program, at 2000Hz, with set bound to Pin(25) (LED on the rp2 board)
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(25))
sm2 = rp2.StateMachine(1, toggle, freq=2000, set_base=Pin(25), sideset_base=Pin(25))

# Run the state machine for 3 seconds.  The LED should blink.
sm.active(1)
time.sleep(3)
sm.active(0)

sm2.active(1)
# time.sleep(3)
sm2.active(0)