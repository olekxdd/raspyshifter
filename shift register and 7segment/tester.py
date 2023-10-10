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


# def segmenter():
#     num = int(input("Input a number between 0-9: "))
#     if num in numbers:
#         data = int(numbers_byte[num], 2)
#         print(numbers_byte[num])
#         return data
#     else:
#         count = 0
#         while count < 5:
#             numbers[num] = 1
#             sleep(0.5)
#             numbers[num] = 0
#             sleep(0.5)
#             count += 1
#             print("number must be between 0-9")
#     return numbers[num]
#
#
# data = segmenter()
#
#
# def data_processor(data, single_byte=None):
#     for i in data:
#         data[i] = single_byte
#         for j in single_byte:
#             if single_byte[j] == 1:
#                 data_pin.on()
#                 shcp_pin.on()
#                 shcp_pin.off()
#                 data_pin.off()
#                 stcp_pin.on()
#                 stcp_pin.off()
#                 print(str(data))
#             else:
#                 shcp_pin.off()
#                 data_pin.off()
#                 stcp_pin.on()
#                 stcp_pin.off()
#                 stcp_pin.toggle()
#                 print("null")
#
#
# data_processor(data)


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


def data_processor(data_segmented):
    for i in range(0, len(data_segmented)):
        sleep_length = 0.5
        sleep(sleep_length)
        if data_segmented[i] == "1":
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
        else:
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


data_processor(data_segmented)






