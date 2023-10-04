import gpiozero
from gpiozero import LED, output_devices
from time import sleep
# led = LED(23)
# x = 0
# while x < 5:
#
#     led.on()
#     time.sleep(1)
#     led.off()
#     x += 1
#     time.sleep(1)

#SN74HC595N light row and 7 segment

# Outputs:
# VCC 5V(pin2)
# GND (Pin6)
# DS (4)
# SHCP (23)
# STCP (24)
# OE into GND

# if SHCP is high, a low is safed in the buffer
# A high is safed in the buffer when SHCP is high WHILE DS is high
# to transfer the signal STCP must be high (under the cicumstance that OE is grounded to begin with)

data = [0,1,0,1,0,0,0,1]

ds_data = gpiozero.GPIODevice(4, pin_factory=None)
shcp_inst_shifter = gpiozero.GPIODevice(23, pin_factory=None)
stcp_outputter = gpiozero.GPIODevice(24, pin_factory=None)



numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = [11000000, 11111001, 10100100, 10110000, 10011001, 10010010, 10000010, 11111000, 10000000, 10010000]
num = int(input("input a number between 0-9"))


# def segmenter():
#     if num is in numbers:
#         for i in numbers:
#             numbers[i] = numbers_byte[i]
#             print(numbers[i])
#     else:
#         print("number must be between 0-9")
#

def segmenter1(num):
    while num == numbers[num]:
        for i in numbers:
            numbers[i] = numbers_byte[i]
            print(numbers[i])
    else:
        print("number must be between 0-9")

segmenter1()

def data_processor(data):
#    if len(data) > 6
    for i in data:
        if data[i] == 1:
            ds_data.value(1)
            shcp_inst_shifter.value(1)
            shcp_inst_shifter.value(0)
            ds_data.value(0)
            stcp_outputter.value(1)
            stcp_outputter.value(0)
            print("null")
        else:
            shcp_inst_shifter.value(1)
            shcp_inst_shifter.value(0)
            stcp_outputter.value(1)
            stcp_outputter.value(0)
            print("null")

hi