import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(5, gpio.OUT)
gpio.setup(26, gpio.OUT)


for x in range(1,15):
    gpio.output(5, gpio.HIGH)
    time.sleep(0.3)
    gpio.output(5, gpio.LOW)
    time.sleep(0.1)
    gpio.output(26, gpio.HIGH)
    time.sleep(0.3)
    gpio.output(26, gpio.LOW)
    time.sleep(0.1)
    gpio.output(5, gpio.HIGH)
    time.sleep(0.3)
    gpio.output(5, gpio.LOW)
    time.sleep(0.1)
    gpio.output(26, gpio.HIGH)
    time.sleep(0.3)
    gpio.output(26, gpio.LOW)
    time.sleep(0.1)    
    gpio.output(26, gpio.HIGH)
    time.sleep(0.3)
    gpio.output(26, gpio.LOW)
    time.sleep(0.1)
    
gpio.cleanup()
