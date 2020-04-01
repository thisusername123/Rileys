import smbus2
import time


class ArduinoIO:

    def __init__(self, channel, addr):
        self.addr = addr
        self.bus = smbus2.SMBus(channel)

    def get(self, port):
        self.bus.write_byte(self.addr, port)
        return self.bus.read_byte(self.addr)

    def send(self, val):
        self.bus.write_byte(self.addr, val)
