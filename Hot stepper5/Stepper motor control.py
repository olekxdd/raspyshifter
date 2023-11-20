from gpiozero import OutputDevice, DigitalOutputDevice, DigitalInputDevice, LED, output_devices
from time import sleep
import numpy as np
import random

delay = 0.015625
steps_amount = 500
ramp_up_steps = 100
# stepping modes (w1, w2, w3, w4) w1 = coil one

# fullsteps = ((0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 0, 0, 1))

fullsteps = (
(0, 1, 0, 0), (0, 1, 0, 1), (0, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 0), (1, 0, 1, 0), (0, 0, 1, 0), (0, 1, 1, 0))

halfsteps = ((0, 1, 0, 1), (0, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 0),
             (1, 0, 1, 0), (1, 0, 0, 0), (1, 0, 0, 1), (0, 0, 0, 1))



# declaring pins

# coil_a1_pin = 18  # color
# coil_a2_pin = 4  # color
# coil_b1_pin = 15  # color
# coil_b2_pin = 14  # color

coil_a1_pin = 5  # color
coil_a2_pin = 46  # color
coil_b1_pin = 13  # color
coil_b2_pin = 26  # color

# Creating physical Pins with the GPIOZero Libary

coil_A1 = DigitalOutputDevice(coil_a1_pin)
coil_A2 = DigitalOutputDevice(coil_a2_pin)
coil_B1 = DigitalOutputDevice(coil_b1_pin)
coil_B2 = DigitalOutputDevice(coil_b2_pin)


# function to control and apply the stepping sequence pattern
def step_sequence(w1, w2, w3, w4):
    coil_A1.value = w1
    coil_A2.value = w2
    coil_B1.value = w3
    coil_B2.value = w4


# def speed_control(ramp_up_steps, ):


# controls the duration of the sequence and feeds the pattern into the function
def motor_run_time(steps, stepmode):
    for i in range(0, steps):
        for pattern in stepmode:
            step_sequence(*pattern)
            sleep(delay)


motor_run_time(steps_amount, fullsteps)

max_steps_per_second = 1000  # 15,625 umdrehungen pro sekunde
max_speed = 1
initial_speed = 0

a = 0.001
b = 0.001
c = 0.01

rate_of_change = 1


def accel_func(x):
    z = np.exp(-c * x)
    sig = 1 / ((a * 1) + b * z)
    time_step = 1 / sig

    return time_step
