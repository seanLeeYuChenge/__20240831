from machine import Timer,ADC,Pin,PWM,RTC

import utime


#import tools
adc_light = ADC(Pin(28))
#tools.connect()
adc = ADC(4)
pwm = PWM(Pin(15),freq=50)
conversion_factor = 3.3 / (65535)
rtc = RTC()

def do_thing(t):
    year,month,day,weekly,hours,minuse,seconds,info = rtc.datetime()
    datetime_str = f"{year}-{month}-{day} {hours}:{minuse}:{seconds}"
    print(datetime_str)
    
    
def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    
    print(f'可變電阻:{round(duty/65535*10)}')
def do_thing2(t):
    '''
    :param t:Timer的實體
    負責偵測溫度和光線
    每2秒執行1次
    '''
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721  
    print(f'溫度:{temperature}')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')
    
def main():
    t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
    t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)
    t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing2)

if __name__ == '__main__':
    adc = ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光敏電阻
    pwm = PWM(Pin(15),freq=50) #pwm led
    main()