from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
# from machine import Pin
from time import sleep_us
import utime


class pio_timer:
    def __init__(self, sm, freq, pin):
#         self.sm = StateMachine(sm, self.calc_time, freq=freq, set_base=Pin(pin))
        self.sm = StateMachine(sm)
        self.sm.init(self.calc_time, freq=freq, set_base=Pin(pin))
        self.freq = freq
        
    def active(self):
        self.sm.active(1)
    
    def put(self, msec):
        value = msec * self.freq / 1000
        self.sm.put(msec)
    
    @asm_pio(set_init=PIO.OUT_HIGH)
    def calc_time():
        wrap_target()
        pull()
        mov(x,osr)
        label("loop")

        jmp(x_dec, "loop")

        mov(isr,x_dec)
#         set(isr, 1) # 終了シグナル用の0を代入
        push()         # 終了シグナルを送信

        wrap()

@asm_pio(set_init=PIO.OUT_HIGH)
def piotime():
    wrap_target()
    pull()
    mov(x,osr) # x に必要時間を代入
    label("loop") # ｘ時間分ループ処理で待機
    jmp(x_dec, "loop")

#     mov(isr,x)
    set(isr, 1) # 終了シグナル用の0を代入

    push()         # 終了シグナルを送信

    wrap()


if __name__ == '__main__':
    timer = pio_timer(sm=1,freq=10000, pin=3)
    # timer.active()
    # sm.put(20000)
    ms = 20000 # カウントしたい秒数を代入
    timer.active()
    timer.put(ms)
    start = utime.ticks_ms()
    while True:
        
    #     sm.put(1)
    #     start_time = sm.get()
        
    #     end_time = sm.get()
    #     print(start_time, end_time)
        
    #     utime.sleep(1)
    #     print("aa")
    #     r = sm.get()
        r2 = timer.sm.get()
    #     utime.sleep(1)
    #     print(r2)
        if r2 == 0: # r2が0になるときにタイマーがリセットされる
            time = utime.ticks_ms() - start
            print(r2, time/1000)
            timer.put(ms)
        
