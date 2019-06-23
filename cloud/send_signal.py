from threading import Thread

from .cloud_engine import CloudClient
from helper import get_logger


class SignalTransmission:
	"""
	This class sends signals to cloud via MQTT protocol.
	get message >> encrypt >> send
	"""
	def __init__(self):
		self.client = CloudClient("send_msg", "SEND")
		self.logger = get_logger(_type="cloud", name=__name__)

	def send_signal(self, raw_signal):		
		from helper import HideAndSeek
		encrypted_msg = HideAndSeek().encrypt(raw_signal)
		
		self.logger.info("Signal Encrypted.")		
		self.client.transmit(encrypted_msg)
