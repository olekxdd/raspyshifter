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
from gpiozero import DigitalOutputDevice
from gpiozero import LED, output_devices
from time import sleep

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]

numbers_dict = {0: "11000000", 1: "11111001", 2: "10100100", 3: "10110000", 4: "10011001", 5: "10010010", 6: "10000010",
                7: "11111000", 8: "10000000", 9: "10010000"}
# work with the dict, you can make the segmenter easier

ds_data = 4
shcp_inst_shifter = 23
stcp_outputter = 24

data_pin = DigitalOutputDevice(ds_data)
shcp_pin = DigitalOutputDevice(shcp_inst_shifter)
stcp_pin = DigitalOutputDevice(stcp_outputter)


# GPIO.setup(ds_data, GPIO.OUT)
# GPIO.setup(shcp_inst_shifter, GPIO.OUT)
# GPIO.setup(stcp_outputter, GPIO.OUT)


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


data = segmenter()


def data_processor(data, single_byte=None):
    for i in data:
        data[i] = single_byte
        for j in single_byte:
            if single_byte[j] == 1:
                data_pin.on()
                shcp_pin.on()
                shcp_pin.off()
                data_pin.off()
                stcp_pin.on()
                stcp_pin.off()
                print(str(data))
            else:
                shcp_pin.off()
                data_pin.off()
                stcp_pin.on()
                stcp_pin.off()
                stcp_pin.toggle()
                print("null")


data_processor(data)

ChatGPT
There are several issues in your code that need to be addressed:

In the segmenter function, you're trying to compare num with numbers[num] to check if it's a valid number. However, numbers is a list, and you should compare num with elements of the list using in to check if it's a valid index. Replace the condition if num == numbers[num]: with if num in numbers:.

In the same function, you are trying to convert numbers_byte[num] to an integer. However, numbers_byte is a list of strings containing binary representations of numbers. You should use int(numbers_byte[num], 2) to convert the binary string to an integer.

In the data_processor function, you are using a for loop to iterate over the elements of data, but you are also trying to use i as an index for data, which is incorrect. Instead, you can directly iterate over the dictionary items using for i, single_byte in data.items():.

In the data_processor function, you have a nested loop where you iterate over each character in single_byte using for j in single_byte:. However, single_byte is a string, and this loop will iterate over individual characters as strings, not as integers. You should compare each character to the string "1" rather than the integer 1. Change the condition if single_byte[j] == 1: to if j == "1":.

Inside the data_processor function, you are using data_pin, shcp_pin, and stcp_pin as variables, but you have not declared them as global variables. You should declare these variables as global at the beginning of the function to access them within the function scope.

Here's the corrected code:

python
Copy code
import time
from gpiozero import DigitalOutputDevice

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]

numbers_dict = {0: "11000000", 1: "11111001", 2: "10100100", 3: "10110000", 4: "10011001", 5: "10010010", 6: "10000010",
                7: "11111000", 8: "10000000", 9: "10010000"}

ds_data = 4
shcp_inst_shifter = 23
stcp_outputter = 24

data_pin = DigitalOutputDevice(ds_data)
shcp_pin = DigitalOutputDevice(shcp_inst_shifter)
stcp_pin = DigitalOutputDevice(stcp_outputter)

def segmenter():
    num = int(input("Input a number between 0-9: "))
    if num in numbers:
        data = int(numbers_byte[num], 2)

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


def data_processor(data_segmented):
    for i in data_segmented:
        if i == "1":
            data_pin.on()
            shcp_pin.on()
            shcp_pin.off()
            data_pin.off()
            stcp_pin.on()
            stcp_pin.off()
            print(str(data))
        else:
            shcp_pin.off()
            data_pin.off()
            stcp_pin.on()
            stcp_pin.off()
            stcp_pin.toggle()
            print("null")


data_processor(data_segmented)








