"""FB Service Module"""
import logging
import settings as Config
# from gpiozero import Motor
import time
import math
import subprocess


# pylint: disable=too-few-public-methods
class CameraService(object):
    """SpeakService"""

    def __init__(self):
        # self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)
        logging.debug("initializing video Service!")
        self.stream_url = ''
        self.proc = None

    def act(self, msg):
        """perform speaj"""
        request_stream_url = msg["stream_url"]
        logging.debug("acting CAM VID !!! -> " + str(request_stream_url))
        params = "sudo ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 -f mpegts -codec:v mpeg1video -s 640x480 -b:v 1000k -bf 0 %(request_stream_url)s" % locals(
        )

        if (not self.stream_url == request_stream_url) and self.proc:
            self.proc.terminate()
            self.proc = None

        if not (self.stream_url == request_stream_url and self.proc):
            self.stream_url = request_stream_url
            logging.debug("running ffmpeg " + params)
            self.proc = subprocess.Popen(
                [params],
                shell=False,
                stdin=None,
                stdout=None,
                stderr=None,
                close_fds=True)
            # ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 -f mpegts -codec:v mpeg1video -s 640x480 -b:v 1000k -bf 0 http://SOME-STREAM-SERVER/YOUR-SECRET
