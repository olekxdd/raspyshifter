import gpiozero
from gpiozero import LED, output_devices
from time import sleep

# Outputs:
# VCC 5V(pin2)
# GND (Pin6)
# DS (gpio4)
# SHCP (gpio23)
# STCP (gpio24)
# OE into GND

# if SHCP is high, a low is safed in the buffer
# A high is safed in the buffer when SHCP is high WHILE DS is high
# to transfer the signal STCP must be high (under the cicumstance that OE is grounded to begin with)

ds_data = gpiozero.GPIODevice(4, pin_factory=None)
shcp_inst_shifter = gpiozero.GPIODevice(23, pin_factory=None)
stcp_outputter = gpiozero.GPIODevice(24, pin_factory=None)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]


def segmenter():
    num = int(input("input a number between 0-9: "))
    if num == numbers[num]:
        numbers[num] = int(numbers_byte[num])
        print(numbers[num])
    else:
        print("number must be between 0-9")


def data_processor(data=(segmenter()), single_byte=None):
    for i in data:
        data[i] = single_byte
        for j in single_byte:
            if single_byte[j] == 1:
                ds_data.value(1)
                shcp_inst_shifter.value(1)
                shcp_inst_shifter.value(0)
                ds_data.value(0)
                stcp_outputter.value(1)
                stcp_outputter.value(0)
                print("null")
                sleep(0.5)
            else:
                shcp_inst_shifter.value(1)
                shcp_inst_shifter.value(0)
                stcp_outputter.value(1)
                stcp_outputter.value(0)
                print("null")
