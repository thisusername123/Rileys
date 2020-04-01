import gpiozero
import smbus
import time


class FillSensor:
    bus = smbus.SMBus(1)
    arduino_i2c_adress = 0x04

    def __init__(self, port_number):
        self.port_number = port_number
        self.fill_sensor = gpiozero.DigitalInputDevice(port_number)

    def get_val(self):
        return self.fill_sensor.value

    def get_bool(self):  # true if sensing
        return self.fill_sensor.value > .5

    def writeNumber(self):
        self.bus.write_byte(self.arduino_i2c_adress, 1)
        # return -1

    def readNumber(self):
        number = self.bus.read_byte_data(self.arduino_i2c_adress, 1)
        return number