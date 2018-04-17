"""speaking Service Module"""
import logging
import settings as Config
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

    def act(self, msg):
        """perform speak"""
        logging.debug("acting speak!!! -> " + str(msg["msg"]))
        who = msg["by"]
        what = msg["msg"]
        text = "%(who)s says, %(what)s" % locals()
        subprocess.Popen(
            ["espeak", text],
            shell=True,
            stdin=None,
            stdout=None,
            stderr=None,
            close_fds=True)
