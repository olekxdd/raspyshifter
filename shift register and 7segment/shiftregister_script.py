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

# import RPi.GPIO as GPIO
import time
from gpiozero import DigitalOutputDevice, DigitalInputDevice
from gpiozero import LED, output_devices
from time import sleep

ds_data = 4
shcp_inst_shifter = 23
stcp_outputter = 24
oe_pullup = 26

oe_pin = DigitalInputDevice(oe_pullup)
data_pin = DigitalOutputDevice(ds_data)
shcp_pin = DigitalOutputDevice(shcp_inst_shifter)
stcp_pin = DigitalOutputDevice(stcp_outputter)

# oe_pin.pull_up()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]
numbers_dict = {0: "11000000", 1: "11111001", 2: "10100100", 3: "10110000", 4: "10011001", 5: "10010010", 6: "10000010",
                7: "11111000", 8: "10000000", 9: "10010000"}

sleep_length = 0.2


def high_bit(sleep_length):
    data_pin.on()
    sleep(sleep_length)
    shcp_pin.on()
    sleep(sleep_length)
    shcp_pin.off()
    sleep(sleep_length)
    data_pin.off()
    sleep(sleep_length)
    stcp_pin.on()
    sleep(sleep_length)
    stcp_pin.off()


def low_bit(sleep_length):
    data_pin.off()
    sleep(sleep_length)
    shcp_pin.off()
    sleep(sleep_length)
    shcp_pin.on()
    sleep(sleep_length)
    shcp_pin.off()
    sleep(sleep_length)
    stcp_pin.on()
    sleep(sleep_length)
    stcp_pin.off()


def segmenter():
    num = int(input("Input a number between 0-9: "))
    if num in numbers:
        data = int(numbers_byte[num])
        return data
    else:
        count = 0
        while count < 5:
            numbers[num] = 1
            sleep(0.5)
            numbers[num] = 0
            sleep(0.5)
            count += 1
            print("Number must be between 0-9")
        return numbers[num]


data_segmented = str(segmenter())


def data_processor_led7_segment(data_segmented, sleep_length):
    for i in range(0, len(data_segmented)):
        sleep(sleep_length)
        if data_segmented[i] == "1":
            high_bit(sleep_length)
        else:
            low_bit(sleep_length)


def costum_led_pattern():
    while True:
        costum_data_segmented = input("type in a series of bits (1 and 0) which represent the leds(only 8 entries): ")
        if len(costum_data_segmented) == 8:
            for i in range(0, len(costum_data_segmented)):
                sleep(sleep_length)
                if data_segmented[i] == "1":
                    high_bit(sleep_length)
                else:
                    low_bit(sleep_length)
                break
        else:
            print("your input hast to be 8 objects long e.g: '10101010' ")


data_processor_led7_segment(data_segmented, sleep_length)
#costum_led_pattern()