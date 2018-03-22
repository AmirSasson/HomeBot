"""FB Service Module"""
import logging
import settings as Config


# pylint: disable=too-few-public-methods
class MotorCtrlService(object):
    """FB Service"""

    def __init__(self):
        # self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)
        logging.debug("initializing motor control!")

    def act(self, msg):
        """perform motor move"""
        logging.debug("acting !!! -> " + str(msg))
