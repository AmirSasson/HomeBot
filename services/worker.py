"""Worker that register to post topic """
from services.motor_ctrl_service import MotorCtrlService
from services.cam_service import CameraService
from services.speak_service import SpeakService

import settings as Config


# pylint: disable=too-few-public-methods
class Worker(object):
    """Service Worker"""

    def __init__(self, mqtt):
        self.mqtt = mqtt
        self.motor = MotorCtrlService()
        self.speakService = SpeakService()
        self.vid = CameraService()
        self.mqtt.reg(Config.MQTT_MOTOR_MOVE_TOPIC_NAME, self.motor_move)
        self.mqtt.reg(Config.MQTT_CAM_TOPIC_NAME, self.start_cam)
        self.mqtt.reg(Config.MQTT_SPEAK_TOPIC_NAME, self.speak)

    def motor_move(self, msg):
        """facebook page post api"""
        self.motor.act(msg)

    def start_cam(self, msg):
        """facebook page post api"""
        self.vid.act(msg)

    def speak(self, msg):
        """facebook page post api"""
        self.speakService.act(msg)
