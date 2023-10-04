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

# SN74HC595N light row and 7 segment

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

data = [0, 1, 0, 1, 0, 0, 0, 1]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = [11000000, 11111001, 10100100, 10110000, 10011001, 10010010, 10000010, 11111000, 10000000, 10010000]
num = int(input("input a number between 1-9"))
# def segmenter():
#     for i in numbers:
#         numbers[i] = numbers_byte[i]
#         print(numbers[i])

def segmenter1(num):
    while num == numbers[num]:
        for i in numbers:
            numbers[i] = numbers_byte[i]
            print(numbers[i])
    else:
        print("number must be between 0-9")

segmenter1(num)


ds_data = 0
shcp_inst_shifter = 0
stcp_outputter = 0



# def data_processor(data):
# #    if len(data) > 6
#     for i in data:
#         if data[i] == 1:
#             ds_data = 1
#             shcp_inst_shifter = 1
#             shcp_inst_shifter = 0
#             ds_data = 0
#             stcp_outputter = 1
#             stcp_outputter = 0
#             print("eins")
#         else:
#             shcp_inst_shifter = 1
#             shcp_inst_shifter = 0
#             stcp_outputter = 1
#             stcp_outputter = 0
#             print("null")
#
# data_processor(data)
