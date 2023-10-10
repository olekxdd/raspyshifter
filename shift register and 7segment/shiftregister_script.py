from gpiozero import DigitalOutputDevice, DigitalInputDevice
from gpiozero import LED, output_devices
from time import sleep

ds_data = 24
shcp_inst_shifter = 23
stcp_outputter = 4

data_pin = DigitalOutputDevice(ds_data)
shcp_pin = DigitalOutputDevice(shcp_inst_shifter)
stcp_pin = DigitalOutputDevice(stcp_outputter)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_byte = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000",
                "10000000", "10010000"]
numbers_dict = {0: "11000000", 1: "11111001", 2: "10100100", 3: "10110000", 4: "10011001", 5: "10010010", 6: "10000010",
                7: "11111000", 8: "10000000", 9: "10010000"}

sleep_length = 0.1


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
            for i in range(0, len(costum_data_segmented)):
                sleep(sleep_length)
                if costum_data_segmented[i] == "1":
                    high_bit(sleep_length)
                else:
                    low_bit(sleep_length)

        else:
            print("your input hast to be 8 objects long e.g: '10101010' ")


def wave_led():
    x = 0
    while x < 200:
        high_bit(sleep_length)
        low_bit(sleep_length)
        x += 1



# data_processor_led7_segment(data_segmented, sleep_length)
# costum_led_pattern()
wave_led()
