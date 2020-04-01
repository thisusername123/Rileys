import gpiozero
import smbus

class test_comms:

    # @vivek this is basic for reading one of the pins on the pi
    # its just according the gpiozero api
    # you prob know the i2c stuff
    bus = smbus.SMBus(1)
    adress = 0x04
    
    def writeNumber(value):
        return bus.write_byte(address, value)
        

    def readNumber():
        number = bus.read_byte(address)
        return number

    portNum = 69420
    something = gpiozero.DigitalInputDevice(portNum)

    def getVal(self):
        return self.something.value


    # while True:
    #     print(getVal)
     