from gpiozero import DigitalOutputDevice, DigitalInputDevice, LED, output_devices
from time import sleep
import math
import random
from signal import pause


ds_data = 26

n = 1
# Creating physical Pins with the GPIOZero Libary

data_pin = DigitalOutputDevice(ds_data)
while True:

    y = math.sin(n)
    data_pin.value = 1
    sleep(y)
    data_pin.value = 0
    sleep(y)
    n += 1
