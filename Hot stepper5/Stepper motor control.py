from gpiozero import OutputDevice, DigitalOutputDevice, DigitalInputDevice, LED, output_devices
from time import sleep
import numpy as np
import random

#delay = 0.015625
delay = 0.001
steps_amount = 1000
# stepping modes (w1, w2, w3, w4) w1 = coil one

fullsteps = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
fullsteps_reverse = ((0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0))
fullsteps2 = ((1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1))

halfsteps = (
    (0, 1, 0, 0), (0, 1, 0, 1), (0, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 0), (1, 0, 1, 0), (0, 0, 1, 0), (0, 1, 1, 0))

halfsteps2 = (
    (1, 0, 0, 1), (1, 0, 0, 0), (1, 1, 0, 0), (0, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 0), (0, 0, 1, 1), (0, 0, 0, 1))

# declaring pins

# coil_a1_pin = 18  # color
# coil_a2_pin = 4  # color
# coil_b1_pin = 15  # color
# coil_b2_pin = 14  # color

coil_a1_pin = 27  # color
coil_a2_pin = 22  # color

coil_a1_pin = 5  # color
coil_a2_pin = 6  # color
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


# defining the accel and decell ramp with a sigmoid curve
ramp_start_step = 0
ramp_end_step = 50

a = 0.001
b = 0.01
c = 1


def accel_func(x, a, b, c):
    z = np.exp(-c * x)
    sig = 1 / ((a * 1) + b * z)

    return sig


for i in range(ramp_start_step, ramp_end_step):
    accel_func(i, a, b, c)


# controls the duration of the sequence and feeds the pattern into the function

def motor_run_time(ramp_start_step, ramp_end_step, stepmode):
    for i in range(ramp_start_step, ramp_end_step):
        for pattern in stepmode:
            step_sequence(*pattern)
            sleep((1000 / (accel_func(i, a, b, c) * 1000)))
            print((1000 / (accel_func(i, a, b, c) * 1000)))

btn_cw.when_pressedd =
btn_ccw

def motor_run_time_btn_ctrl(btn_cw, btn_ccw, stepmode):
    while btn_ccw.value(1) = 1 or btn_cw.value(1 = 1
        for pattern in stepmode:
            step_sequence(*pattern)
            sleep((1000 / (accel_func(i, a, b, c) * 1000)))
            print((1000 / (accel_func(i, a, b, c) * 1000)))
# def motor_run_time(ramp_start_step, ramp_end_step, stepmode):
#     for i in range(ramp_start_step, ramp_end_step):
#         for pattern in stepmode:
#             step_sequence(*pattern)
#             sleep(delay)


motor_run_time(ramp_start_step, ramp_end_step, fullsteps_reverse)
motor_run_time(ramp_start_step, ramp_end_step, fullsteps)
motor_run_time(ramp_start_step, ramp_end_step, fullsteps_reverse)
motor_run_time(ramp_start_step, ramp_end_step, fullsteps)
