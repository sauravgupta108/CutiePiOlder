import threading
import json
from paho.mqtt import client as mqtt
import os


from libraries.mqtt_engine import Mqtt_Client
from helper import get_logger


class CloudClient(threading.Thread):
	"""This class runs MQTT Clients as Threads."""
	def __init__(self, name, client_type):
		threading.Thread.__init__(self)
		self._CLOUD_CLIENT = Mqtt_Client(mqtt.Client(client_id=name))
		self._signal = None
		self._channel = None

		if client_type not in ('SEND', 'RECEIVE'):
			raise ValueError("Invalid Client Type")
		else:
			self._client_type = client_type

		self.logger = get_logger(name=__name__, _type="cloud")

	def set_channel(self):
		with open(os.environ["CUTIE_SECRET"]) as scrt:
			content = json.loads(scrt.read())
			if self._client_type == 'SEND':
				self._channel = content['transmission_channel']
			else:
				self._channel = content['reception_channel']
			self.logger.debug("Cloud Channel set.")

	def transmit(self, signal=""):
		self.logger.debug("Signal ready to transmit")
		self.set_channel()
		
		if not signal:
			raise ValueError("Empty Signal....!!!!")
		else:
			self._signal = signal
		
		threading.Thread.start(self)

	def recieve(self):
		self.logger.debug("Ready to recieve signals")
		self.set_channel()

		threading.Thread.start(self)

	def run(self):
		if self._client_type == 'SEND':
			'''This part runs the mqtt client (Thread) as Publisher.'''
			self._CLOUD_CLIENT.transmit_signal(self._channel, self._signal)
			self.logger("Signal Transmitted Successfully.")
			
		else:
			'''This part runs the mqtt client (Thread) as Subscriber.'''
			self._CLOUD_CLIENT.receive_signal(self._channel)

	def is_published(self):
		# return self._CLOUD_CLIENT._pub_result
		pass

	def get_subscribed_messages(self):
		# return self._CLOUD_CLIENT._sub_msgs
		pass

	def disconnect(self):  # Use it only for subscriber, not for publisher.
		self._CLOUD_CLIENT.disconnect_from_broker()
