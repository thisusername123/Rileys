import gpiozero
import Ports
from Fill_Sensor import FillSensor
import time
import ArduinoDI

Ports = Ports.RPiPorts()

#PI
start_btn = gpiozero.Button(Ports.START_BUTTON)
stop_btn = gpiozero.Button(Ports.STOP_BUTTON)
e_stop_btn = gpiozero.Button(Ports.E_STOP_BUTTON)

hard_stop1 = gpiozero.DigitalOutputDevice(Ports.HARD_STOP_SOL_1, True, False, None)
hard_stop2 = gpiozero.DigitalOutputDevice(Ports.HARD_STOP_SOL_2, True, False, None)

ram = gpiozero.DigitalOutputDevice(Ports.FILL_RAM, True, False, None)

#filler1 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_1, True, False, None) # port, high is true, default val
#filler2 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_2, True, False, None)
#filler3 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_3, True, False, None)
#filler4 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_4, True, False, None)
#filler5 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_5, True, False, None)
#filler6 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_6, True, False, None)
#filler7 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_7, True, False, None)
#filler8 = gpiozero.DigitalOutputDevice(Ports.FILL_SOL_8, True, False, None)
# port, high is true, default val
fillers = [ gpiozero.DigitalOutputDevice(Ports.FILL_SOL_1, True, False, None), \
            gpiozero.DigitalOutputDevice(Ports.FILL_SOL_2, True, False, None), \
            gpiozero.DigitalOutputDevice(Ports.FILL_SOL_3, True, False, None), \
            gpiozero.DigitalOutputDevice(Ports.FILL_SOL_4, True, False, None), \
            gpiozero.DigitalOutputDevice(Ports.FILL_SOL_5, True, False, None), \
            gpiozero.DigitalOutputDevice(Ports.FILL_SOL_6, True, False, None), \
            gpiozero.DigitalOutputDevice(Ports.FILL_SOL_7, True, False, None), \
            gpiozero.DigitalOutputDevice(Ports.FILL_SOL_8, True, False, None) ]

#Arduino + Motor
#fill_sensor1 = FillSensor(Ports.FILL_SENSOR_1) 
#fill_sensor2 = FillSensor(Ports.FILL_SENSOR_2)
#fill_sensor3 = FillSensor(Ports.FILL_SENSOR_3)
#fill_sensor4 = FillSensor(Ports.FILL_SENSOR_4)
#fill_sensor5 = FillSensor(Ports.FILL_SENSOR_5)
#fill_sensor6 = FillSensor(Ports.FILL_SENSOR_6)
#fill_sensor7 = FillSensor(Ports.FILL_SENSOR_7)
#fill_sensor8 = FillSensor(Ports.FILL_SENSOR_8)
fill_sensors = [ ArduinoDI(Ports.FILL_SENSOR_1), \
                 ArduinoDI(Ports.FILL_SENSOR_2), \
                 ArduinoDI(Ports.FILL_SENSOR_3), \
                 ArduinoDI(Ports.FILL_SENSOR_4), \
                 ArduinoDI(Ports.FILL_SENSOR_5), \
                 ArduinoDI(Ports.FILL_SENSOR_6), \
                 ArduinoDI(Ports.FILL_SENSOR_7), \
                 ArduinoDI(Ports.FILL_SENSOR_8)  ]


mBeginningBanner = gpiozero.DigitalInputDevice(Ports.BEGINNING_BANNER_SENSOR)
mEndBanner = gpiozero.DigitalInputDevice(Ports.END_BANNER_SENSOR)

output_to_arduino = gpiozero.DigitalOutputDevice(99, True, False, None)

is_ram_down = None #Filler staton

def main():
    while True:
        if start_btn.is_pressed():
            print("Started!")

            # start conveyor motor
            output_to_arduino.on()

            # actuate hard stop 1
            # hard_stop1.actuate(True)

            if ir_sensor1.value == 1:
                # stop conveyor
                output_to_arduino.off()
                # bring down ram
                ram.on()
                is_ram_down = True

            time.sleep(1)

            if is_ram_down:
                # while sensor is false keep filling
                fill()

                all_fills_done = True

                for i in range(0, 8):
                    all_fills_done = all_fills_done and fill_sensors[i].get()

                if all_fills_done
                    ram.off()
                    is_ram_down = False
                    hard_stop1.on()
                    hard_stop2.off()

            if ir_sensor2.value == 1:
                hard_stop2.on()
                hard_stop2.off()

        elif stop_btn.is_pressed() or e_stop_btn.is_pressed():
            print('Stopped!')
            kill()

def fill():
    for i in range(0, 8):
        if fill_sensors[i].get():
            fillers[i].off()
        else
            fillers[i].on()

def kill():
    for i in range(0, 8):
        fillers[i].off()

if __name__ == "__main__":
    main()