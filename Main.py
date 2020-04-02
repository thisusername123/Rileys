import gpiozero
import Ports
import States
from ArduinoIO import ArduinoIO
import time

# PI
start_btn = gpiozero.Button(Ports.START_BUTTON)
stop_btn = gpiozero.Button(Ports.STOP_BUTTON)
e_stop_btn = gpiozero.Button(Ports.E_STOP_BUTTON)

hard_stop1 = gpiozero.DigitalOutputDevice(Ports.HARD_STOP_SOL_1, True, False, None)
hard_stop2 = gpiozero.DigitalOutputDevice(Ports.HARD_STOP_SOL_2, True, False, None)

filler_pistons = gpiozero.DigitalOutputDevice(Ports.FILL_RAM, True, False, None)

fillers = [gpiozero.DigitalOutputDevice(Ports.FILL_SOL_0, True, False, None),
           gpiozero.DigitalOutputDevice(Ports.FILL_SOL_1, True, False, None),
           gpiozero.DigitalOutputDevice(Ports.FILL_SOL_2, True, False, None),
           gpiozero.DigitalOutputDevice(Ports.FILL_SOL_3, True, False, None),
           gpiozero.DigitalOutputDevice(Ports.FILL_SOL_4, True, False, None),
           gpiozero.DigitalOutputDevice(Ports.FILL_SOL_5, True, False, None),
           gpiozero.DigitalOutputDevice(Ports.FILL_SOL_6, True, False, None),
           gpiozero.DigitalOutputDevice(Ports.FILL_SOL_7, True, False, None)]

#Arduino
arduino = ArduinoIO(Ports.I2C_CHAN, Ports.ARDUINO_I2C_ADDR)

beginning_banner = gpiozero.DigitalInputDevice(Ports.BEGINNING_BANNER_SENSOR)
end_banner = gpiozero.DigitalInputDevice(Ports.END_BANNER_SENSOR)

is_filler_extended = False

machine_state = States.OFF

def main():
    global machine_state
    while True:
        if start_btn.value:
            for f in fillers:
                f.on()
        else:
            for f in fillers:
                f.off()
        continue

        if machine_state == States.OFF:
            kill()

        elif machine_state == States.LOADING:
            arduino.send(Ports.CONVEYOR_ON)
            if not end_banner:
                hard_stop1.off()
                hard_stop2.on()
            elif end_banner and beginning_banner:
                hard_stop1.on()
                hard_stop2.on()
                machine_state = States.FILLING

        elif machine_state == States.FILLING:
            arduino.send(Ports.CONVEYOR_ON)
            if not filler_pistons.value == 1:
                filler_pistons.on()
                time.sleep(2)  # Wait for filler to fully extend out
            for f in fillers:
                f.on()
            time.sleep(6)
            for f in fillers:
                f.off()
            #fill()
            #all_fills_done = True
            #for i in Ports.FILL_SENSORS:
            #    all_fills_done = all_fills_done and arduino.get(i)

            #if all_fills_done:
            machine_state = States.RETRACT_FILLER

        elif machine_state == States.RETRACT_FILLER:
            arduino.send(Ports.CONVEYOR_ON)
            if not filler_pistons.value == 0:
                filler_pistons.off()
                time.sleep(2)
            machine_state = States.BUFFERRING

        elif machine_state == States.BUFFERRING:
            arduino.send(Ports.CONVEYOR_ON)
            hard_stop2.off()
            time.sleep(1)
            machine_state = States.LOADING
        else:
            print('State Undefined')


def fill():
    for i in Ports.FILL_SENSORS:
        if arduino.get(i):
            fillers[i].off()
        else:
            fillers[i].on()


def kill():
    for i in range(0, 8):
        fillers[i].off()
    arduino.send(Ports.CONVEYOR_OFF)


if __name__ == "__main__":
    main()
