"""Main entry point"""

import logging
import settings as Config
from services.worker import Worker
from services.mqtt_client import MqttClient

logging.basicConfig(level=logging.DEBUG)

# pylint: disable=invalid-name
mqttc = MqttClient()
worker = Worker(mqttc)

mqttc.startListen()
