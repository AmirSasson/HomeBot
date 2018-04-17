"""Camera stream Service Module"""
import logging
import os
import shlex
import signal
import subprocess
from pyee import EventEmitter


# pylint: disable=too-few-public-methods
class CameraService(object):
    """SpeakService"""

    def __init__(self, topic, event_emitter=EventEmitter()):
        # self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)
        logging.debug("initializing video Service!")
        event_emitter.on(topic, self.act)
        self.stream_url = ''
        self.proc = None

        logging.debug("creating cam file..")
        subprocess.Popen(
            shlex.split("modprobe bcm2835-v4l2"), stdout=subprocess.PIPE)

    def act(self, msg):
        """perform cam stream.."""
        logging.debug("CAM acting !!! -> " + str(msg))
        if msg["action"] == "stop":
            if not self.proc is None:
                logging.debug("stoping cam...")
                os.kill(self.proc.pid, signal.SIGINT)
                # self.proc.send_signal(signal.CTRL_BREAK_EVENT)
                self.proc = None
        else:  # assuming start...
            request_stream_url = msg["stream_url"]
            logging.debug("acting CAM VID !!! -> " + str(request_stream_url))
            #pylint: disable=unused-argument
            video_size = "300x255"
            params = "ffmpeg -f v4l2 -framerate 25 -video_size %(video_size)s -i /dev/video0 -f mpegts -codec:v mpeg1video -s %(video_size)s -b:v 1000k -bf 0 %(request_stream_url)s" % locals(
            )

            if (not self.stream_url == request_stream_url) and self.proc:
                self.proc.terminate()
                self.proc = None

            if not (self.stream_url == request_stream_url and self.proc):
                self.stream_url = request_stream_url
                logging.debug("running ffmpeg " + params)

                self.proc = subprocess.Popen(
                    shlex.split(params),
                    # shell=True,
                    # stdin=None,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    # universal_newlines=True,
                    # close_fds=True
                )
            #out, err = self.proc.communicate('rasberry\n')
