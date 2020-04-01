import smbus2
import time


class ArduinoIO:

    def __init__(self, channel, addr):
        self.addr = addr
        self.bus = smbus2.SMBus(channel)

    def get(self, port):
        self.bus.write_byte(self.addr, port)
        return self.bus.read_byte(self.addr)

    def send(self, port):
        print(port)
        self.bus.write_byte(self.addr, port)
