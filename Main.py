import gpiozero
import Ports
from Fill_Sensor import FillSensor
import time

ports = Ports.RPiPorts()

start_btn = gpiozero.Button(ports.START_BUTTON)
stop_btn = gpiozero.Button(ports.STOP_BUTTON)
e_stop_btn = gpiozero.Button(ports.E_STOP_BUTTON)

hard_stop1 = gpiozero.DigitalOutputDevice(ports.HARD_STOP_SOL_1, True, False, None)
hard_stop2 = gpiozero.DigitalOutputDevice(ports.HARD_STOP_SOL_2, True, False, None)

ram = gpiozero.DigitalOutputDevice(ports.FILL_RAM, True, False, None)

filler1 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_1, True, False, None) # port, high is true, default val
filler2 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_2, True, False, None)
filler3 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_3, True, False, None)
filler4 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_4, True, False, None)
filler5 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_5, True, False, None)
filler6 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_6, True, False, None)
filler7 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_7, True, False, None)
filler8 = gpiozero.DigitalOutputDevice(ports.FILL_SOL_8, True, False, None)

fill_sensor1 = FillSensor(ports.FILL_SENSOR_1)
fill_sensor2 = FillSensor(ports.FILL_SENSOR_2)
fill_sensor3 = FillSensor(ports.FILL_SENSOR_3)
fill_sensor4 = FillSensor(ports.FILL_SENSOR_4)
fill_sensor5 = FillSensor(ports.FILL_SENSOR_5)
fill_sensor6 = FillSensor(ports.FILL_SENSOR_6)
fill_sensor7 = FillSensor(ports.FILL_SENSOR_7)
fill_sensor8 = FillSensor(ports.FILL_SENSOR_8)

ir_sensor1 = gpiozero.DigitalInputDevice(ports.IR_SENSOR_1)
ir_sensor2 = gpiozero.DigitalInputDevice(ports.IR_SENSOR_2)

output_to_arduino = gpiozero.DigitalOutputDevice(99, True, False, None)

is_ram_down = None #Filler staton
# started = False

while True:
    # while start button pressed
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
            # filler 1
            if not fill_sensor1.get_bool():
                filler1.on()
            else:
                filler1.off()
            # filler 2
            if not fill_sensor2.get_bool():
                filler2.on()
            else:
                filler2.off()
            # filler 3
            if not fill_sensor3.get_bool():
                filler3.on()
            else:
                filler3.off()
            # filler 4
            if not fill_sensor4.get_bool():
                filler4.on()
            else:
                filler4.off()
            # filler 5
            if not fill_sensor5.get_bool():
                filler5.on()
            else:
                filler5.off()
            # filler 6
            if not fill_sensor6.get_bool():
                filler6.on()
            else:
                filler6.off()
            # filler 7
            if not fill_sensor7.get_bool():
                filler7.on()
            else:
                filler7.off()
            # filler 8
            if not fill_sensor8.get_bool():
                filler8.on()
            else:
                filler8.off()

            if fill_sensor1.get_bool() and fill_sensor2.get_bool() and fill_sensor3.get_bool() and fill_sensor4.get_bool() and fill_sensor5.get_bool() and fill_sensor6.get_bool() and fill_sensor7.get_bool() and fill_sensor8.get_bool():
                ram.off()
                is_ram_down = False
                hard_stop1.on()
                hard_stop2.off()

        if ir_sensor2.value == 1:
            hard_stop2.on()
            hard_stop2.off()

    elif stop_btn.is_pressed() or e_stop_btn.is_pressed():
        print('Stopped!')
        output_to_arduino.off()
