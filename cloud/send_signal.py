from threading import Thread

from .cloud_engine import CloudClient


class SignalTransmission:
	"""
	This class sends signals to cloud via MQTT protocol.
	get message >> encrypt >> send
	"""
	def __init__(self):
		self.client = CloudClient("send_msg", "SEND")

	def send_signal(self, raw_signal):
		'''encrypt'''
		# log Preparing to send signal
		from helper import HideAndSeek
		print(raw_signal)
		encrypted_msg = HideAndSeek().encrypt(raw_signal)
		print(encrypted_msg)
		# log message encrypted
		self.client.transmit(encrypted_msg)
