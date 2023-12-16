from gpiozero import DigitalOutputDevice, DigitalInputDevice
from gpiozero import LED, output_devices
from time import sleep
import random

ds_data = 18
oe_outputcontrol = 4
stcp_outputter = 15
shcp_inst_shifter = 14



data_pin = DigitalOutputDevice(ds_data)
oe_pin = DigitalOutputDevice(oe_outputcontrol)
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


sleep_length = float(input("input the sleep length: ")) # add this line to every function and give recommendation

def high_bit():
    data_pin.on()
    shcp_pin.on()
    shcp_pin.off()
    data_pin.off()
    stcp_pin.on()
    stcp_pin.off()


data_pin.on()
sleep(1)
data_pin.off()

def low_bit():
    shcp_pin.on()
    shcp_pin.off()
    stcp_pin.on()
    stcp_pin.off()




