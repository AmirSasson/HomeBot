"""Navigation Service Module"""
import logging
from gpiozero import DistanceSensor
from pyee import EventEmitter
from time import sleep, time
import threading
import math
MIN_DIST_CM = 10
import RPi.GPIO as GPIO


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


TRIG = 23
ECHO = 24


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

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)
        sleep(2)

        # self.sensor = DistanceSensor(
        #     echo=24,
        #     trigger=23,
        #     max_distance=1,
        #     threshold_distance=0.05,
        #     queue_len=5)
        set_interval(self._dist_check, 1)
        # self.sensor.when_activated = self._dist_check
        # self.sensor.when_out_of_range = self._dist_check
        # self._dist_check()
        # self.sensor.when_changed = self._dist_check

    def _dist_check(self):
        # sensor.Measurement(23, 24) dist_sensor.raw_distance()
        dist_cm = self._get_dist()
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

    def _get_dist2(self):
        dist_sensor = sensor.Measurement(TRIG, ECHO)
        dist = dist_sensor.raw_distance()
        GPIO.cleanup()
        return dist

    def _get_dist(self):

        GPIO.output(TRIG, True)
        sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        #GPIO.cleanup()
        return distance


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
