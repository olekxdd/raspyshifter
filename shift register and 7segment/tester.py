import gpiozero
from gpiozero import LED, output_devices
from time import sleep
#
# # led = LED(23)
# # x = 0
# # while x < 5:
# #
# #     led.on()
# #     time.sleep(1)
# #     led.off()
# #     x += 1
# #     time.sleep(1)
#
# # SN74HC595N light row and 7 segment
#
# # Outputs:
# # VCC 5V(pin2)
# # GND (Pin6)
# # DS (4)
# # SHCP (23)
# # STCP (24)
# # OE into GND
#
# # if SHCP is high, a low is safed in the buffer
# # A high is safed in the buffer when SHCP is high WHILE DS is high
# # to transfer the signal STCP must be high (under the cicumstance that OE is grounded to begin with)
#
# # data = [0, 1, 0, 1, 0, 0, 0, 1]
# #
# # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # numbers_byte = [11000000, 11111001, 10100100, 10110000, 10011001, 10010010, 10000010, 11111000, 10000000, 10010000]
# # num = int(input("input a number between 1-9"))
# # # def segmenter():
# # #     for i in numbers:
# # #         numbers[i] = numbers_byte[i]
# # #         print(numbers[i])
# #
# # def segmenter1(num):
# #     while num == numbers[num]:
# #         for i in numbers:
# #             numbers[i] = numbers_byte[i]
# #             print(numbers[i])
# #     else:
# #         print("number must be between 0-9")
# #
# # segmenter1(num)
# #
# #
# ds_data = 0
# shcp_inst_shifter = 0
# stcp_outputter = 0
# #
#
#
# # def data_processor(data):
# # #    if len(data) > 6
# #     for i in data:
# #         if data[i] == 1:
# #             ds_data = 1
# #             shcp_inst_shifter = 1
# #             shcp_inst_shifter = 0
# #             ds_data = 0
# #             stcp_outputter = 1
# #             stcp_outputter = 0
# #             print("eins")
# #         else:
# #             shcp_inst_shifter = 1
# #             shcp_inst_shifter = 0
# #             stcp_outputter = 1
# #             stcp_outputter = 0
# #             print("null")
# #
# # data_processor(data)
#
#
# list = [124124, 45845, 1767547]
# print(list[0][1])
#
#
#
# def data_processor(data=(segmenter1()), single_byte=None):
#     for i in data:
#         data[i] = single_byte
#         if single_byte[i] == 1:
#             ds_data.value(1)
#             shcp_inst_shifter.value(1)
#             shcp_inst_shifter.value(0)
#             ds_data.value(0)
#             stcp_outputter.value(1)
#             stcp_outputter.value(0)
#             print("null")
#         else:
#             shcp_inst_shifter.value(1)
#             shcp_inst_shifter.value(0)
#             stcp_outputter.value(1)
#             stcp_outputter.value(0)
#             print("null")
#
#
#
# # def segmenter1():
# #     num = int(input("input a number between 0-9: "))
# #     while num == numbers[num]:
# #         for i in numbers:
# #             numbers[i] = int(numbers_byte[i])
# #             print(numbers[i])
# #         break
# #     else:
# #         print("number must be between 0-9")

# ds_data = gpiozero.GPIODevice(4, pin_factory=None)
# shcp_inst_shifter = gpiozero.GPIODevice(26, pin_factory=None)
# stcp_outputter = gpiozero.GPIODevice(24, pin_factory=None)


# --------------------------------------------------------------

# import gpiozero
# from gpiozero import LED, output_devices
# from time import sleep
# from signal import pause
#
# # Outputs:
# # VCC 5V(pin2)
# # GND (Pin6)
# # DS (gpio4)
# # SHCP (gpio23)
# # STCP (gpio24)
# # OE into GND
#
# # if SHCP is high, a low is safed in the buffer
# # A high is safed in the buffer when SHCP is high WHILE DS is high
# # to transfer the signal STCP must be high (under the cicumstance that OE is grounded to begin with)
#
# ds_data = gpiozero.GPIODevice(4, pin_factory=None)
# shcp_inst_shifter = gpiozero.GPIODevice(23, pin_factory=None)
# stcp_outputter = gpiozero.GPIODevice(24, pin_factory=None)
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
#                 "10000000", "10010000"]
#
#
#
# def segmenter():
#     num = int(input("input a number between 0-9: "))
#     if num == numbers[num]:
#         numbers[num] = int(numbers_byte[num])
#         print(numbers[num])
#     else:
#         print("number must be between 0-9")
#
#
# def data_processor(data=(segmenter()), single_byte=None):
#     for i in data:
#         data[i] = single_byte
#         for j in single_byte:
#             if single_byte[j] == 1:
#                 ds_data.value(1)
#                 shcp_inst_shifter.value(1)
#                 shcp_inst_shifter.value(0)
#                 ds_data.value(0)
#                 stcp_outputter.value(1)
#                 stcp_outputter.value(0)
#                 print("null")
#             else:
#                 shcp_inst_shifter.value(1)
#                 shcp_inst_shifter.value(0)
#                 stcp_outputter.value(1)
#                 stcp_outputter.value(0)
#                 print("null")
from gpiozero import DigitalOutputDevice
import time
from gpiozero import DigitalOutputDevice
from gpiozero import LED, output_devices
from time import sleep

led = 26

# led_pin = DigitalOutputDevice(led)
#
# led_pin.on()
# sleep(1)
# led_pin.off()
# sleep(1)
#
# led_pin.on()
# sleep(1)
# led_pin.off()
# sleep(1)
# led_pin.on()
# sleep(1)
# led_pin.off()
# sleep(1)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]

numbers_dict = {0: "11000000", 1: "11111001", 2: "10100100", 3: "10110000", 4: "10011001", 5: "10010010", 6: "10000010",
                7: "11111000", 8: "10000000", 9: "10010000"}


# work with the dictinor, you can make the segmenter easier


# def segmenter(count=None):
#     num = int(input("input a number between 0-9: "))
#     if num == numbers[num]:
#         numbers[num] = int(numbers_byte[num])
#         data = numbers[num]
#         print(numbers[num])
#         return data
#     else:
#         while count <= 5:
#             numbers[num] = 1
#             sleep(0.5)
#             numbers[num] = 0
#             sleep(0.5)
#             count += 1
#             print("number must be between 0-9")
#     return numbers[num]
#
#
# data = str(segmenter())
#
# print(data)

def segmenter():
    num = int(input("Input a number between 0-9: "))
    if num in numbers:
        data = int(numbers_byte[num], 2)
        print(numbers_byte[num])
        return data
    else:
        count = 0
        while count < 5:
            numbers[num] = 1
            sleep(0.5)
            numbers[num] = 0
            sleep(0.5)
            count += 1
            print("number must be between 0-9")
    return numbers[num]

segmenter()