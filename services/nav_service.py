"""Navigation Service Module"""
import logging
from gpiozero import DistanceSensor
from pyee import EventEmitter
from time import sleep
MIN_DIST_CM = 5


# pylint: disable=too-few-public-methods
class NavService(object):
    """NavService"""

    def __init__(self, motor_topic, event_emitter=EventEmitter()):
        # self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)
        logging.debug("initializing Speak Service!")
        self.event_emitter = event_emitter
        # https://www.bluetin.io/sensors/python-library-ultrasonic-hc-sr04/
        self.topic_motor = motor_topic

        self.sensor = DistanceSensor(
            echo=24, trigger=23, queue_len=2, threshold_distance=0.01)
        self.sensor.when_activated = self._dist_check
        self.sensor.when_out_of_range = self._dist_check

    def _dist_check(self):
        dist_cm = self.sensor.distance * 100,
        logging.info('Distance: %(dist_cm)f cm')
        print('Distance: ' + str(dist_cm) + ' cm')
        if int(dist_cm[0]) <= MIN_DIST_CM:
            logging.info('Distance Sensor Stopping motor!!')
            stop_msg = {'speed_left': 0, 'speed_right': 0}
            self.event_emitter.emit(self.topic_motor, stop_msg)


if __name__ == '__main__':
    print("initializing sonar sensor service!")
    NavService('bot-move')
    while True:
        sleep(1)
