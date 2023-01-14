import machine
import time
from machine import PWM

# GP16をPWMに使うための設定です
Led  = PWM(machine.Pin(25, machine.Pin.OUT))

# 周期を1秒間に10回(10Hz)に設定します
Led.freq(10)

# 1回の周期の内、8割ON(Duty比:80)になるように設定します
# Duty比は、0~65536の範囲なので、Duty比:80は「52429」です。
Led.duty_u16(1000)

# 上のコードでDuty比を設定するとLEDが点滅するので、2秒待機します
time.sleep(2)

# Duty比は変えずに、周期を1000Hzに変更します。
# この周期になると、人の目では点滅ではなく、点灯に見えます
Led.freq(1000)
time.sleep(2)

# Duty比を10にセットします
# 周期が早い状態でDutyを下げると、LEDは暗く見えます
Led.duty_u16(3277)
time.sleep(2)

# Duty比0にセットすると、LEDが消灯します
Led.duty_u16(0)
time.sleep(2)