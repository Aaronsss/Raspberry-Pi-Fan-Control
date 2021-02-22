import os
import re
from time import sleep
import RPi.GPIO as GPIO

pin = 4  # The pin ID, edit here to change it
maxTMP = 40  # The maximum temperature in Celsius after which we trigger the fan
stopTMP = maxTMP - 1 # The temperature to deactivate the fan


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    fan_off()
    return ()


def get_cpu_temperature():
    res = os.popen("vcgencmd measure_temp").readline()
    temp = re.findall("\d+\.\d+", res)[0]
    #print("temp is {0}".format(temp))  # Uncomment here for testing
    return temp


def fan_on():
    GPIO.output(pin, True)
    return ()


def fan_off():
    GPIO.output(pin, False)
    return ()


def get_temp():
    cpu_temp = float(get_cpu_temperature())
    if cpu_temp > maxTMP:
        fan_on()
    elif cpu_temp < stopTMP:
        fan_off()
    return ()

try:
    setup()
    while True:
        get_temp()
        sleep(2)  # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt:  
        fan_on()
