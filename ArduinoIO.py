import smbus2
import time


class ArduinoIO:

    def __init__(self, channel, addr):
        self.addr = addr
        self.bus = smbus2.SMBus(channel)

    def get(self, port):
        try:
            self.bus.write_byte(self.addr, port)
            return self.bus.read_byte(self.addr)
        except:
            print "Error communicating with ARduino - Check power and connection."

    def send(self, port):
        try:
            self.bus.write_byte(self.addr, port)
            print("Sending Arduino: " + port)
        except:
            print "Error communicating with Arduino - Check power and connection."