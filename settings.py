"""Application Config"""
import os
from pconf import Pconf
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

Pconf.defaults({
    'bot-move-topic-name': 'bot-move',
    "bot-speak-topic-name": 'bot-speak',
    "bot-cam-topic-name": 'cam-command'
})
localpath = os.path.join(DIR_PATH, 'dev.json').format()
Pconf.file(localpath, encoding='json')
Pconf.env()

CONFIG = Pconf.get()

MQTT_HOST = CONFIG.get("mqtt-host", '')
MQTT_USER = CONFIG.get("mqtt-user", '')
MQTT_PWD = CONFIG.get("mqtt-pwd", '')
MQTT_PORT = int(CONFIG.get("mqtt-port", -1))
MQTT_MOTOR_MOVE_TOPIC_NAME = CONFIG.get("bot-move-topic-name", '')
MQTT_SPEAK_TOPIC_NAME = CONFIG.get("bot-speak-topic-name", '')
MQTT_CAM_TOPIC_NAME = CONFIG.get("bot-cam-topic-name", '')

WEB_PORT = int(CONFIG.get("PORT", 5000))
