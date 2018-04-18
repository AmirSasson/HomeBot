"""Navigation Service Module"""
import logging
from gpiozero import DistanceSensor
from pyee import EventEmitter
from time import sleep
import threading
import math
from hcsr04sensor import sensor
MIN_DIST_CM = 10


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


# pylint: disable=too-few-public-methods
class NavService(object):
    """NavService"""

    def __init__(self, motor_topic, event_emitter=EventEmitter()):
        # self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)
        logging.debug("initializing Speak Service!")
        self.event_emitter = event_emitter
        # https://www.bluetin.io/sensors/python-library-ultrasonic-hc-sr04/
        self.topic_motor = motor_topic
        self.last_known_distance_cm = 0.0

        # self.sensor = DistanceSensor(
        #     echo=24,
        #     trigger=23,
        #     max_distance=1,
        #     threshold_distance=0.05,
        #     queue_len=5)

        self.sensor = sensor.Measurement(23, 24)
        set_interval(self._dist_check, 1)
        # self.sensor.when_activated = self._dist_check
        # self.sensor.when_out_of_range = self._dist_check
        # self._dist_check()
        # self.sensor.when_changed = self._dist_check

    def _dist_check(self):
        dist_cm = self.sensor.raw_distance()
        print('Distance: %(dist_cm)s cm' % locals())
        if math.fabs(self.last_known_distance_cm - dist_cm) > 3.0:
            logging.info('Distance: %(dist_cm)s cm' % locals())
        if (dist_cm <
                self.last_known_distance_cm  # obsetacale getting closer...
            ) and int(dist_cm) <= MIN_DIST_CM:
            logging.info('Distance Sensor Stopping motor!!')
            stop_msg = {'speed_left': 0, 'speed_right': 0}
            self.event_emitter.emit(self.topic_motor, stop_msg)
        self.last_known_distance_cm = dist_cm


if __name__ == '__main__':
    print("initializing sonar sensor service!")
    # sensor1 = DistanceSensor(
    #     echo=24,
    #     trigger=23,
    #     threshold_distance=0.001,
    #     partial=True,
    #     queue_len=30)
    # sleep(2)
    NavService("")
    while True:
        #    print('Distance: ', sensor1.distance * 100)
        sleep(1)
    # NavService('bot-move')
    # while True:
    #     sleep(10)
