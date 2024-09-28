from machine import Timer, ADC  # 從 machine 模組導入 Timer 和 ADC 類

# 初始化 ADC，這裡指定使用 GPIO 4 來讀取模擬信號
adc = ADC(4)  
conversion_factor = 3.3 / (65535)  # 將 ADC 讀數轉換為電壓值的係數

def do_thing(t):
    # 這是定時器的回調函數，每次定時器觸發時會執行這個函數
    reading = adc.read_u16() * conversion_factor  # 讀取 ADC 的數值並轉換為電壓
    temperature = 27 - (reading - 0.706) / 0.001721  # 根據讀數計算溫度
    print(temperature)  # 輸出計算出的溫度值

def do_thing1(t):
    # 另一個定時器的回調函數
    print("do_thing1")  # 每次觸發時會輸出這個字符串

# 設置定時器 t1，每 2000 毫秒（2 秒）觸發一次 do_thing 函數
t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)

# 設置定時器 t2，每 500 毫秒觸發一次 do_thing1 函數
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)
