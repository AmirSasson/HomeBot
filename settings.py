"""Application Config"""
from pconf import Pconf
import json

Pconf.defaults({'bot-move-topic-name': 'bot-move'})
Pconf.file('dev.json', encoding='json')
Pconf.env()

CONFIG = Pconf.get()

MQTT_HOST = CONFIG.get("mqtt-host", '')
MQTT_USER = CONFIG.get("mqtt-user", '')
MQTT_PWD = CONFIG.get("mqtt-pwd", '')
MQTT_PORT = int(CONFIG.get("mqtt-port", -1))
MQTT_MOTOR_MOVE_TOPIC_NAME = CONFIG.get("bot-move-topic-name", '')
WEB_PORT = int(CONFIG.get("PORT", 5000))
