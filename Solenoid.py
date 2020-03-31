import gpiozero

# unused
class Solenoid:

    def __init__(self, port_number):
        self.port_number = port_number
        self.solenoid = gpiozero.DigitalOutputDevice(port_number, True, False, None)  # portnumber, if high is on, default value(off)

    def actuate(self, is_acutated):
        if is_acutated:
            self.solenoid.on()
        else:
            self.solenoid.off()
