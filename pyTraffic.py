# import GPIO
import RPi.GPIO as GPIO
import time.sleep as sleep


class PyTraffic():
    """Class to control traffic light demo for Raspberry Pi"""

    def setup(this):
        """Method to set up board functionality"""
        GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

        # set up light 1
        GPIO.setup(4, GPIO.OUT)     # set up pin 4 / green
        GPIO.setup(17, GPIO.OUT)    # set up pin 17 / yellow
        GPIO.setup(22, GPIO.OUT)    # set up pin 22 / red

        # set up light 2
        GPIO.setup(5, GPIO.OUT)     # set up pin 5 / green
        GPIO.setup(13, GPIO.OUT)    # set up pin 13 / yellow
        GPIO.setup(24, GPIO.OUT)    # set up pin 24 / red

    def light_test():
        """Method to turn on all lights"""
        GPIO.output(4, 1)
        GPIO.output(17, 1)
        GPIO.output(22, 1)
        GPIO.output(5, 1)
        GPIO.output(13, 1)
        GPIO.output(24, 1)
        sleep(5000)
        GPIO.output(4, 0)
        GPIO.output(17, 0)
        GPIO.output(22, 0)
        GPIO.output(5, 0)
        GPIO.output(13, 0)
        GPIO.output(24, 0)

    def demo_mode():
        """Method to run a disco light show"""
        pass

    def instersection():
        """Method to control an intersection"""
        pass

    def rail_crossing():
        """Method to control a rail crossing"""
        pass
