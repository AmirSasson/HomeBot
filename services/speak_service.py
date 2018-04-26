"""speaking Service Module"""
import logging
from time import sleep, time
import shlex

# from gpiozero import Motor
import time
import math
import subprocess
from pyee import EventEmitter


# pylint: disable=too-few-public-methods
class SpeakService(object):
    """SpeakService"""

    def __init__(self, topic, event_emitter=EventEmitter()):
        # self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)
        logging.debug("initializing Speak Service!")
        event_emitter.on(topic, self.act)
        self.last_speaker = None

    def act(self, msg):
        """perform speak"""
        logging.debug("acting speak!!! -> " + str(msg["msg"]))
        who = msg["by"]
        what = msg["msg"]
        greet = '%(who)s Says: ' % locals()
        if self.last_speaker == who:
            greet = ''
        elif self.last_speaker == 'bot':
            greet = 'Guys :'
        text = '%(greet)s %(what)s' % locals()
        self.last_speaker = who
        params = 'espeak -s 135 -a 100 -k 50 -p 30 "%(text)s"' % locals()
        subprocess.Popen(
            shlex.split(params),
            # shell=True,
            # stdin=None,
            # stdout=subprocess.PIPE,
            # stderr=subprocess.PIPE,
            # universal_newlines=True,
            # close_fds=True
            shell=False,
            stdin=None,
            stdout=None,
            stderr=None,
            close_fds=True)


if __name__ == '__main__':
    print("Testing espeak")
    # sensor1 = DistanceSensor(
    #     echo=24,
    #     trigger=23,
    #     threshold_distance=0.001,
    #     partial=True,
    #     queue_len=30)
    # sleep(2)
    ss = SpeakService("")
    sleep(2)

    while True:
        #    print('Distance: ', sensor1.distance * 100)
        ss.act({'msg': "hello", 'by': "Test user"})
        sleep(10)
