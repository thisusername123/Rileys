import gpiozero
import smbus
import time


class FillSensor:
    bus = smbus.SMBus(1)
    arduino_adress = 0x04

    def __init__(self, port_number):
        self.port_number = port_number
        self.fill_sensor = gpiozero.DigitalInputDevice(port_number)


    def get_val(self):
        return self.fill_sensor.value()

    def get_bool(self):  # true if sensing
        return self.fill_sensor.value() > .5

    def writeNumber(value):
        bus.write_byte(address, value)
        bus.write_byte(address_2, value)
        # bus.write_byte_data(address, 0, value)
        return -1

    def readNumber():
        # number = bus.read_byte(address)
        number = bus.read_byte_data(address, 1)
        return number