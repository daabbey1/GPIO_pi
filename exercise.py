from gpiozero import LED
from time import sleep

led = LED(17)
led2 = LED(3)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

    
while True:
    led2.on()
    sleep(1)
    led2.off()
    sleep(1)
