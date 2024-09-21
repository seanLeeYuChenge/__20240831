from machine import Pin
from time import sleep
led = Pin("LED", Pin.OUT)
status = False
while True:
     led.on()
     if status == False:
         led.on()
         status = True
     else:
         led.off()
         status = False
     sleep(1)