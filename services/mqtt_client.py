"""This module exposes a class that handles all MQTT interactions"""
import logging
import datetime
import json
import paho.mqtt.client as paho
import settings as Config
from common.msg import Msg

# pylint: disable=too-few-public-methods


class MqttClient:
    """A facade api to  MQTT client"""

    def __init__(self):
        self.mqttc = paho.Client()
        self.mqttc.on_message = self.on_message
        self.registered_callbacks = {
            Config.MQTT_MOTOR_MOVE_TOPIC_NAME: None,
            Config.MQTT_SPEAK_TOPIC_NAME: None,
            Config.MQTT_CAM_TOPIC_NAME: None,
        }
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
        self.mqttc.subscribe(Config.MQTT_MOTOR_MOVE_TOPIC_NAME)
        self.mqttc.subscribe(Config.MQTT_SPEAK_TOPIC_NAME)
        self.mqttc.subscribe(Config.MQTT_CAM_TOPIC_NAME)

    def startListen(self):
        self.mqttc.loop_forever()

    def reg(self, topic, onMsgCallback):
        """register a callback method to delegate when topic updated"""
        self.registered_callbacks[topic] = onMsgCallback

    def publish(self, topic: str, message: Msg):
        """Publishes a new message to a topic"""
        return self.mqttc.publish(topic, json.dumps(message.__dict__))

    # pylint: disable=unused-argument
    def on_message(self, client, userdata, message):
        """callback"""
        # self.callback("Got Message! " + datetime.datetime.now().strftime())
        topic = message.topic
        if self.registered_callbacks[topic]:
            self.registered_callbacks[topic](
                json.loads(message.payload.decode("utf-8")))
        # self.callback(json.loads(message.payload.decode("utf-8")))
        logging.info("got message!" + str(message) + str(userdata))
