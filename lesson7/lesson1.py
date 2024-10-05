from machine import Timer,ADC,Pin,PWM,RTC
from umqtt.simple import MQTTClient
import utime
import binascii

import tools

tools.connect()
rtc = RTC()

def do_thing(t):
    year,month,day,weekly,hours,minuse,seconds,info = rtc.datetime()
    datetime_str = f"{year}-{month}-{day} {hours}:{minuse}:{seconds}"
    print(datetime_str)
    mqtt.publish('SA-10/時間', f'datetime_str')
    
def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    light_level = round(duty/65535*10)
    print(f'可變電阻:{light_level}')
    mqtt.publish('SA-10/可變電阻', f'light_level')
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
    mqtt.publish('SA-10/溫度', f'temperature')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')
    mqtt.publish('SA-10/光線', f'dc_value')
    
def main():
    try:
        tools.connect()
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知名錯誤')
    else:
        
        t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
        t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)
        t3 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing2)
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect()

if __name__ == '__main__':
    adc = ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光敏電阻
    pwm = PWM(Pin(15),freq=50) #pwm led
    SERVER = "192.168.0.252"
    CLIENT_ID = binascii.hexlify(machine.unique_id())
    
    main()