"""This module exposes a class that handles all MQTT interactions"""
import datetime
import json
import logging
import sys

import paho.mqtt.client as paho
from pyee import EventEmitter

import settings as Config
from common.msg import Msg

# pylint: disable=too-few-public-methods


class MqttClient:
    """A facade api to  MQTT client"""

    def __init__(self, topics_list, event_emitter=EventEmitter()):
        self.mqttc = paho.Client()
        self.mqttc.on_message = self._on_message
        self.emitter = event_emitter
        self.mqttc.username_pw_set(Config.MQTT_USER, Config.MQTT_PWD)
        self.callback = None

        logging.warning('Trying to establish connection to ' +
                        Config.MQTT_HOST)
        try:
            self.mqttc.connect(Config.MQTT_HOST, Config.MQTT_PORT)
        except ValueError:
            logging.critical(
                "Oops!  connection to '%s' couldn't be established",
                Config.MQTT_HOST)

        for topic in topics_list:
            self.mqttc.subscribe(topic)

    def start_listen(self):
        """starts the loop"""
        self.mqttc.loop_forever()

    def publish(self, topic: str, message: Msg):
        """Publishes a new message to a topic"""
        return self.mqttc.publish(topic, json.dumps(message.__dict__))

    # pylint: disable=unused-argument
    def _on_message(self, client, userdata, message):
        """callback"""
        topic = message.topic
        try:
            decoded_msg = json.loads(message.payload.decode("utf-8"))
            self.emitter.emit(topic, decoded_msg)
            logging.info("Handled message!" + str(decoded_msg) + str(userdata))
        except:  # pylint: disable-msg=W0702
            err = sys.exc_info()[0]
            logging.critical("unable to handle message: " + str(
                message.payload.decode("utf-8")) + " userdata: " +
                             str(userdata) + " exception:\n" + str(err))
