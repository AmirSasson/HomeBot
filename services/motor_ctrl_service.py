"""FB Service Module"""
import logging
import settings as Config
from gpiozero import Motor
import time
import math


# pylint: disable=too-few-public-methods
class MotorCtrlService(object):
    """FB Service"""

    def __init__(self):
        # self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)
        logging.debug("initializing motor control!")
        self.motor_right = Motor(17, 18)
        self.motor_left = Motor(6, 12)
        self.start()

    def start(self):
        self.full_spin()

    def full_spin(self):
        logging.debug("full spin maneuver!")
        self.stop()
        self.motor_left.forward(1)
        self.motor_left.backward(1)
        # time.sleep(2)
        # self.stop()

    def forward(self, speed=1):
        self.move()

    def backward(self, speed=1):
        self.move(-1, -1)

    def move(self, speed_right=1, speed_left=1):
        logging.debug(f"Moving motor: {speed_right} | {speed_left}")
        self.stop()
        if speed_right > 0:
            self.motor_right.forward(speed_right)
            pass
        elif speed_right < 0:
            self.motor_right.backward(math.fabs(speed_right))
        else:
            self.motor_right.stop()

        if speed_left > 0:
            self.motor_left.forward(speed_left)
        elif speed_left < 0:
            self.motor_left.backward(math.fabs(speed_left))
        else:
            self.motor_left.stop()

    def stop(self):
        self.motor_right.stop()
        self.motor_left.stop()

    def act(self, msg):
        """perform motor move"""
        logging.debug("acting !!! -> " + str(msg) + " left:" +
                      str(msg.speed_left))
        self.move(
            speed_left=float(msg.speed_left),
            speed_right=float(msg.speed_right))
