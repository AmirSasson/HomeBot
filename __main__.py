"""Main entry point"""

import logging

from pyee import EventEmitter

import settings as Config
from services.motor_ctrl_service import MotorCtrlService
from services.cam_service import CameraService
from services.speak_service import SpeakService
from services.mqtt_client import MqttClient
from services.nav_service import NavService

logging.basicConfig(level=logging.DEBUG)
EE = EventEmitter()

MQTTC = MqttClient([
    Config.MQTT_MOTOR_MOVE_TOPIC_NAME, Config.MQTT_SPEAK_TOPIC_NAME,
    Config.MQTT_CAM_TOPIC_NAME
], EE)

MotorCtrlService(Config.MQTT_MOTOR_MOVE_TOPIC_NAME, EE)
SpeakService(Config.MQTT_SPEAK_TOPIC_NAME, EE)
CameraService(Config.MQTT_CAM_TOPIC_NAME, EE)
NavService(Config.MQTT_MOTOR_MOVE_TOPIC_NAME, EE)

MQTTC.start_listen()
