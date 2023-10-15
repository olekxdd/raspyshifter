from gpiozero import DigitalOutputDevice, DigitalInputDevice
from gpiozero import LED, output_devices
from time import sleep
import random

ds_data = 18
oe_output_control = 4
stcp_outputter = 15
shcp_inst_shifter = 14

data_pin = DigitalOutputDevice(ds_data)
oe_pin = DigitalOutputDevice(oe_output_control)
shcp_pin = DigitalOutputDevice(shcp_inst_shifter)
stcp_pin = DigitalOutputDevice(stcp_outputter)

# modes = ["costum_led_pattern", "wave_led", "laser_led", "random_led_shifter", "random_led_static", "newton_pendle", "wave_drop"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]

numbers_dict = {0: "11000000", 1: "11111001", 2: "10100100", 3: "10110000", 4: "10011001", 5: "10010010", 6: "10000010",
                7: "11111000", 8: "10000000", 9: "10010000"}

wave_drop_8bit = ["00011000", "00100100", "01000010", "10000001", "01000010", "00100100", "00011000", "00000000",
                  "10000000", "10010000"]

newton_pendle_16bit = ["0000000110000000", "0000001001000000", "0000010000100000", "0000100000010000",
                       "0001000000001000", "0010000000000100", "0100000000000010", "1000000000000001",
                       "0100000000000010", "0010000000000100", "0001000000001000", "0000100000010000",
                       "0000010000100000", "0000001001000000"]

wave_drop_16bit = ["0000000110000000", "0000011001100000", "0001100110011000", "1001100110011001", "0001100110011000",
                   "0000011001100000"]

sleep_length = float(input("input the sleep length: "))  # add this line to every function and give recommendation


def high_bit():
    data_pin.on()
    shcp_pin.on()
    shcp_pin.off()
    data_pin.off()
    stcp_pin.on()
    stcp_pin.off()


def low_bit():
    shcp_pin.on()
    shcp_pin.off()
    stcp_pin.on()
    stcp_pin.off()


# modes = {1: costum_led_pattern, 2: wave_led, 3: laser_led, 4: random_led_shifter, 5: random_led_static,
#         6: newton_pendle, 7: wave_drop}

# def segmenter():
#     num = int(input("Input a number between 0-9: "))
#     if num in numbers:
#         data = int(numbers_byte[num])
#         return data
#     else:
#         count = 0
#         while count < 5:
#             numbers[num] = 1
#             sleep(0.5)
#             numbers[num] = 0
#             sleep(0.5)
#             count += 1
#             print("Number must be between 0-9")
#         return numbers[num]
#
#
# data_segmented = str(segmenter())
#
#
# def data_processor_led7_segment(data_segmented, sleep_length):
#     for i in range(0, len(data_segmented)):
#         sleep(sleep_length)
#         if data_segmented[i] == "1":
#             high_bit(sleep_length)
#         else:
#             low_bit(sleep_length)

def costum_led_pattern():
    while True:
        costum_data_segmented = input("type in a series of bits (1 and 0) which represent the leds(only 8 entries): ")
        if len(costum_data_segmented) == 8:
            oe_pin.on()
            for i in range(0, len(costum_data_segmented)):
                sleep(sleep_length)
                if costum_data_segmented[i] == "1":
                    high_bit()
                else:
                    low_bit()
            oe_pin.off()
        else:
            print("your input hast to be 8 objects long e.g: '10101010' ")


def wave_led():
    x = 0
    while x < 200:
        high_bit()
        low_bit()
        x += 1


def laser_led():
    x = 0
    while x < 200:
        high_bit()
        high_bit()
        high_bit()
        low_bit()
        low_bit()
        low_bit()
        x += 1


def random_led_shifter():
    x = 0
    while x < 200:
        n = random.randint(0, 1)
        print(n)
        if n == 1:
            high_bit()
            x += 1
        else:
            low_bit()
            x += 1


def random_led_static():
    stop_timer = 1
    x = 0
    byte_amt = 0
    sleep_length = 0.0001
    while x < 1000:
        oe_pin.on()
        n = random.randint(0, 1)
        if byte_amt == 16:
            sleep(stop_timer)
            byte_amt = 0
        if n == 1:
            high_bit()
            x += 1
            byte_amt += 1
        else:
            low_bit()
            x += 1
            byte_amt += 1
        oe_pin.off()


def newton_pendle(newton_pendle_16bit):
    sleep_length = 0.0001
    while True:
        for i in newton_pendle_16bit:
            sleep(0.1)
            oe_pin.on()
            for digit in i:
                if digit == "1":
                    high_bit()
                else:
                    low_bit()
            oe_pin.off()


def wave_drop(wave_drop_16bit):
    sleep_length = 0.001
    while True:
        for i in wave_drop_16bit:
            oe_pin.on()
            sleep(0.5)
            for digit in i:
                if digit == "1":
                    high_bit()
                else:
                    low_bit()
            oe_pin.off()


def led_modes(modes_dict, modes_arguments):
    x = 1
    for i in modes_dict:
        print(f"{str(x)}: {str(modes_dict[x])}")
        x += 1
    choice = int(input("which led mode do you want?: "))
    int(choice)
    while True:
        if choice in modes_dict:
            if modes_dict[choice] in modes_arguments:
                if modes_arguments is not None:
                    modes_dict[choice](modes_arguments[modes_dict[choice]])

        else:
            print("wrong numba idiot, pick one from the list....")


modes_dict = {1: costum_led_pattern, 2: wave_led, 3: laser_led, 4: random_led_shifter, 5: random_led_static,
              6: newton_pendle, 7: wave_drop}

modes_arguments = {costum_led_pattern: None, wave_led: None, laser_led: None, random_led_shifter: None,
                   random_led_static: None,
                   newton_pendle: newton_pendle_16bit, wave_drop: wave_drop_16bit}

led_modes(modes_dict, modes_arguments)
