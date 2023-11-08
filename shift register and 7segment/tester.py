from gpiozero import DigitalOutputDevice, DigitalInputDevice, LED, output_devices
from time import sleep
import random
from signal import pause


ds_data = 26


# Creating physical Pins with the GPIOZero Libary
x = 0.1
data_pin = DigitalOutputDevice(ds_data)

data_pin.value = 1
sleep(x)
data_pin.value = 0
sleep(x)
data_pin.value = 1
sleep(x)
data_pin.value = 0
sleep(x)
data_pin.value = 1
sleep(x)
data_pin.value = 0
sleep(x)