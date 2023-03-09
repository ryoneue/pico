from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
# from machine import Pin
from time import sleep_us
import utime


class pio_timer:
    def __init__(self, sm, freq, pin):
#         self.sm = StateMachine(sm, self.calc_time, freq=freq, set_base=Pin(pin))
        self.sm = StateMachine(sm)
        self.sm.init(self.calc_time_high, freq=freq, set_base=Pin(pin), out_base=Pin(pin))
        self.freq = freq
        
    def active(self):
        self.sm.active(1)
    
    def put(self, msec):
        value = int((msec / self.freq) * 1000000)
        self.sm.put(msec)
    
    # 決まった時間後にpushする関数
    @asm_pio(set_init=PIO.OUT_LOW)
    def calc_time():
        wrap_target()
        pull()
        mov(x,osr)
        label("loop")
        jmp(x_dec, "loop")
        set(x,1)

        mov(isr, x)
#         set(isr, 0) # 終了シグナル用の0を代入
#         push()         # 終了シグナルを送信

        wrap()

    
    @asm_pio(set_init=PIO.OUT_LOW, out_init=PIO.OUT_LOW)
    def calc_time_switch():
        mov(y, 1)
        wrap_target()
        pull()
        
        mov(x,osr)
        label("loop")

        
        jmp(x_dec, "loop")
        mov(pins, y)
#         mov(isr, x)
        mov(y, invert(y))

        wrap()

    @asm_pio(set_init=PIO.OUT_LOW, out_init=PIO.OUT_LOW)
    def calc_time_high():
        
        wrap_target()
        pull()
        set(pins, 1)
        mov(x,osr)
        label("loop")
        jmp(x_dec, "loop")
        set(pins, 0)
        
        wrap()

if __name__ == '__main__':
    timer = pio_timer(sm=1,freq=10000, pin=25)
#     timer2 = pio_timer(sm=2,freq=10000, pin=1)
    pin1 = Pin(1)
#     pin2 = Pin(1)

    # timer.active()
    # sm.put(20000)
    ms = 10000 # カウントしたい秒数を代入
#     ms = 5000
    timer.active()
    timer.put(ms)
    
#     timer2.active()
#     timer2.put(ms*2)
    start = utime.ticks_ms()
    count = 0
    count2 = 0
    value=0
    while True:
        
        check = pin1.value()!=value
        value = pin1.value()
        if check: count = 0

        if check and count==0:
            print("pin1: ", pin1.value())
            print((utime.ticks_ms()-start)/1000)
            utime.sleep(0.01)
            count = 1
            timer.put(ms)
        elif pin1.value()==1:
            pass

            
#         if pin2.value()==1 and count2==0:
#             print("pin2: ", pin2.value())
#             count2 = 1
#             timer2.put(ms*2)
#         else: count2 = 0   
        
        tmp = [i for i in range(1,100)]
        