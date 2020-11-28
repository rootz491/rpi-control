# control the LED from here.

from gpiozero import LED
from time import sleep


def changeLedState(flag):
    led = LED(15)
    if flag:
        led.on()
    else:
        led.off()
        