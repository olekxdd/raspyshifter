from gpiozero import DigitalOutputDevice, DigitalInputDevice, LED, output_devices
from time import sleep
import random
from signal import pause

# assigning name/role to the pin (Broadcom (BCM) numbering)

ds_data = 18
oe_output_control = 4
stcp_outputter = 15
shcp_inst_shifter = 14

# Creating physical Pins with the GPIOZero Libary

data_pin = DigitalOutputDevice(ds_data)
oe_pin = DigitalOutputDevice(oe_output_control)
shcp_pin = DigitalOutputDevice(shcp_inst_shifter)
stcp_pin = DigitalOutputDevice(stcp_outputter)

# Lists and Dicts for bit/LED pattern

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]

numbers_dict_2nd = {0: "100000000000000", 1: "111100100000000", 2: "010010000000000", 3: "011000000000000", 4: "001100100000000", 5: "001001000000000", 6: "000001000000000",
                7: "111100000000000", 8: "000000000000000", 9: "001000000000000"}
numbers_dict = {0: "0111111", 1: "0000110", 2: "1011011", 3: "1001111", 4: "1100110", 5: "1101101", 6: "1111101",
                7: "0000111", 8: "1111111", 9: "1101111"}

wave_drop_8bit = ["00011000", "00100100", "01000010", "10000001", "01000010", "00100100", "00011000", "00000000",
                  "10000000", "10010000"]

newton_pendle_16bit = ["0000000110000000", "0000001001000000", "0000010000100000", "0000100000010000",
                       "0001000000001000", "0010000000000100", "0100000000000010", "1000000000000001",
                       "0100000000000010", "0010000000000100", "0001000000001000", "0000100000010000",
                       "0000010000100000", "0000001001000000"]

wave_drop_16bit = ["0000000110000000", "0000011001100000", "0001100110011000", "1001100110011001", "0110011001100110",
                   "0001100000011000"]


# Functions for Creating either a HIGH or LOW, its rather timing based and less Logic (improvements?)

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


# Functions segments a bit Pattern for the 7 segment IC (depends on the wiring)  and only allows the right range of
# segments

def data_processor_led7_segment(numbers_dict):
    sleep_length = float(input("input a length in seconds or decimals e.g: 0.1: "))
    choice = input("1: show specific number\n2: count down from 9 to 0 ")
    if choice == "1":
        num = int(input("Input a number between 0-9: "))
        data = numbers_dict.get(num)
        for i in data:
            sleep(sleep_length)
            if i == "1":
                high_bit()
            else:
                low_bit()
        pause()
    else:
        x = 0
        while x < 100:
            for j in range(0, len(numbers_dict)):
                data = numbers_dict.get(j)
                for bit in data:
                    if bit == "1":
                        high_bit()
                    else:
                        low_bit()
                sleep(1)
                x += 1
            pause()


def custom_led_pattern():
    while True:
        custom_data_segmented = input("type in a series of bits (1 and 0) which represent the leds(only 16 entries are shown): ")
        oe_pin.on()
        for i in range(0, len(custom_data_segmented)):
            if custom_data_segmented[i] == "1":
                high_bit()
            else:
                low_bit()
        oe_pin.off()


def wave_led():
    x = 0
    sleep_length = float(input("input a length in seconds or decimals e.g: 0.1: "))
    while x < 200:
        sleep(sleep_length)
        high_bit()
        sleep(sleep_length)
        low_bit()
        x += 1


def laser_led():
    x = 0
    sleep_length = float(input("input a length in seconds or decimals e.g: 0.1: "))
    while x < 200:
        high_bit()
        sleep(sleep_length)
        high_bit()
        sleep(sleep_length)
        high_bit()
        sleep(sleep_length)
        low_bit()
        sleep(sleep_length)
        low_bit()
        sleep(sleep_length)
        low_bit()
        sleep(sleep_length)
        x += 1


def random_led_shifter():
    x = 0
    sleep_length = float(input("input a length in seconds or decimals e.g: 0.1: "))
    while x < 200:
        n = random.randint(0, 1)
        sleep(sleep_length)
        print(n)
        if n == 1:
            high_bit()
            x += 1
        else:
            low_bit()
            x += 1


def random_led_static():
    stop_timer = 0.5
    x = 0
    byte_amt = 0
    sleep_length = 0.1
    while x < 1000:
        sleep(sleep_length)
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
            sleep(0.5)


def led_modes(modes_dict, modes_arguments):
    x = 1
    for i in modes_dict:
        print(f"{str(x)}: {str(modes_dict[x])}")
        x += 1
    choice = int(input("which led mode do you want?: "))
    if choice in modes_dict:
        selected_mode = modes_dict[choice]
        if selected_mode in modes_arguments:
            mode_argument = modes_arguments[selected_mode]
            if mode_argument  is not None:
                selected_mode(mode_argument)
            else:
                selected_mode()
        else:
            print("wrong numba idiot, pick one from the list....")


modes_dict = {1: custom_led_pattern, 2: wave_led, 3: laser_led, 4: random_led_shifter, 5: random_led_static,
              6: newton_pendle, 7: wave_drop, 8: data_processor_led7_segment}

modes_arguments = {custom_led_pattern: None, wave_led: None, laser_led: None, random_led_shifter: None,
                   random_led_static: None, data_processor_led7_segment: numbers_dict,
                   newton_pendle: newton_pendle_16bit, wave_drop: wave_drop_16bit}

led_modes(modes_dict, modes_arguments)
