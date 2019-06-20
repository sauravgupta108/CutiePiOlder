from threading import Thread

from .cloud_engine import CloudClient


class SignalTransmission:
	"""
	This class sends signals to cloud via MQTT protocol.
	get message >> encrypt >> send
	"""
	def __init__(self):
		client = CloudClient("send_msg", "SEND")

	def send_signal(self, raw_signal):
		'''encrypt'''
		# log Preparing to send signal
		from ..helper import endrypt
		encrypted_msg = endrypt.HideAndSeek().encrypt(raw_signal)
		# log message encrypted
		client.transmit(encrypted_msg)
