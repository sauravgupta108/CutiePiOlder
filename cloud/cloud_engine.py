import threading
import json 
import time
from paho.mqtt import client as mqtt

from libraries.mqtt_engine import Mqtt_Client


class CloudClient(threading.Thread):
	'''This class runs MQTT Clients as Threads.'''
	def __init__(self, name, client_type):
		threading.Thread.__init__(self)
		self._CLOUD_CLIENT = Mqtt_Client(mqtt.Client(client_id = name))

		if client_type not in ('SEND', 'RECEIVE'):
			raise ValueError("Invalid Client Type")
		else:
			self._client_type = client_type

	def set_channel():
		with open('/opt/app/arduino_app/CutiePi/secret/security.json') as scrt:
			content = json.loads(scrt.read())
			if self._client_type == 'SEND':
				self._channel = content['tranmission_channel']
			else:
				self._channel = content['reception_channel']

	def transmit(self, signal = ""):
		self.set_channel()
		
		if not signal:
			raise ValueError("Empty Signal....!!!!")
		else:
			self._signal = signal

		threading.Thread.start(self)

	def recieve(self):
		self.set_channel()
		threading.Thread.start(self)

	def run(self):
		if self._client_type == 'SEND':
			'''This part runs the mqtt client (Thread) as Publisher.'''
			self._CLOUD_CLIENT.transmit_signal(self._channel, self._signal)
			
		else:
			'''This part runs the mqtt client (Thread) as Subscriber.'''
			self._CLOUD_CLIENT.receive_signal(self._channel)

	def is_published(self):
		return self._CLOUD_CLIENT._pub_result

	def get_subscribed_messages(self):
		return self._CLOUD_CLIENT._sub_msgs

	def disconnect(self):  # Use it only for subscriber, not for publisher.
		self._CLOUD_CLIENT.disconnect_from_broker()
