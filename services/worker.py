"""Worker that register to post topic """
from services.motor_ctrl_service import MotorCtrlService


# pylint: disable=too-few-public-methods
class Worker(object):
    """Service Worker"""

    def __init__(self, mqtt):
        self.mqtt = mqtt
        self.motor = MotorCtrlService()
        self.mqtt.reg(self.motor_move)

    def motor_move(self, msg):
        """facebook page post api"""
        self.motor.act(msg)
