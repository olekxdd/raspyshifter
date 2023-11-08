from gpiozero import DigitalOutputDevice, DigitalInputDevice, LED, output_devices, motor
from time import sleep
import random
from signal import pause

delay = 0.05
steps = 500

fullsteps = ((0,1,0,1), (0,1,1,0), (1,0,1,0), (1,0,0,1))

halfsteps = ((0,1,0,1), (0,1,0,0), (0,1,1,0), (0,0,1,0),
             (1,0,1,0), (1,0,0,0), (1,0,0,1), (0,0,0,1))

coil_a1_pin = 18 #color
coil_a2_pin = 4 #color
coil_b1_pin = 15 #color
coil_b2_pin = 14 #color

# Creating physical Pins with the GPIOZero Libary

coil_A1 = DigitalOutputDevice(coil_a1_pin)
coil_A2 = DigitalOutputDevice(coil_a2_pin)
coil_B1 = DigitalOutputDevice(coil_b1_pin)
coil_B2 = DigitalOutputDevice(coil_b2_pin)

def stepSequence(w1, w2, w3, w4):
    coil_A1.value = w1
    coil_A2.value = w2
    coil_B1.value = w3
    coil_B2.value = w4

for i in range(0, steps):
    for pattern in fullsteps:
        stepSequence(pattern)
        sleep(delay)

