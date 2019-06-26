# import paho.mqtt.client as mqtt
import json
import time
import os

from helper import get_logger


class MqttClient:
	"""
	It deals with MQTT Broker directly.
	"""
	def __init__(self, client_mqtt):
		self.mqtt_client = client_mqtt
		self._connection_ok = False		
		self._pub_result = False
		self._sub_result = False
		self._sub_msgs = []
		self._qos = 0

		self.logger = get_logger(name=__name__, _type="mqtt")

	def on_connect(self, client, userdata, flags, rc):
		if rc != 0:
			raise RuntimeError("MQTT Broker connection failed.")
		else:
			self._connection_ok = True
			
	def on_disconnect(self, client, userdata, flags):
		self.mqtt_client.loop_stop()
		self._connection_ok = False

	def on_log(self, client, userdata, level, buf):		
		self.logger.debug("Client: %s -- %s" % client, buf)

	def on_publish(self, client, userdata, mid):
		self._pub_result = True
	
	def on_subscribe(self, client, userdata, mid, granted_qos):
		self._sub_result = True
		self.logger("Ready to receive Signal")

	def on_message(self, client, userdata, message):
		logger = get_logger(_type="cloud_rx", name=__name__)
		time.sleep(0.1)
		logger.info("Signal Received........")
		self._sub_msgs.append(str(message.payload))
		logger.info("Signal Processed Successfully")

	def get_connection_details(self):
		try:
			path = "/opt/app/arduino_app/CutiePi/"
			with open(os.path.join(path, 'config/mqtt_config.json'), "r") as config_file:
				connection = json.load(config_file)
				self._qos = int(connection["qos"])
				return connection
		except Exception as e:
			self.logger.exception("Error in getting Broker details")
			raise RuntimeError("Could not get Broker details.")		
			
	def connect_target(self):
		"""
		Connects to MQTT broker and returns a MQTT Client object.
		"""

		connection_details = self.get_connection_details()

		self.mqtt_client.username_pw_set(connection_details['USERNAME'], connection_details['PASSWORD'])

		self.mqtt_client.on_connect = self.on_connect
		self.mqtt_client.on_disconnect = self.on_disconnect
		self.mqtt_client.on_publish = self.on_publish
		self.mqtt_client.on_subscribe = self.on_subscribe
		self.mqtt_client.on_message = self.on_message
		self.mqtt_client.on_log = self.on_log
		
		try:
			self.mqtt_client.connect(
				connection_details['HOST'],
				connection_details['PORT'],
				connection_details['keepalive'])
		except Exception as e:		
			# del self.mqtt_client
			self.logger.exception("Error in connection...!!!")
			raise RuntimeError("MQTT Broker connection failed.")
		
		time.sleep(0.2)

	def transmit_signal(self, topic, message):
		self.connect_target()
		
		self.mqtt_client.loop_start()
		time.sleep(0.5)
		self.mqtt_client.publish(topic=topic, payload=str(message), qos=self._qos)
		time.sleep(0.1)
		self.logger.info("Signal transmitted successfully.")
		
		if self._connection_ok or self._pub_result:
			self.disconnect_from_broker()

	def receive_signal(self, channel):
		self.connect_target()
		try:
			self.mqtt_client.subscribe(channel, qos=self._qos)
		except:
			self.logger.exception("Error in Recieving Signal")
			raise RuntimeError("Unable to receive from channel: ", channel)

		self.mqtt_client.loop_forever()

	def disconnect_from_broker(self):
		self.mqtt_client.disconnect()
		time.sleep(0.1)
