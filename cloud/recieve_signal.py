from helper import HideAndSeek
from helper import get_logger


class SignalReception:
	"""
	This class recieves signals to cloud via MQTT protocol.
	"""
	def __init__(self):
		self.logger = get_logger(_type="cloud_rx", name=__name__)

	def decode_signal(self, signal):
		decrypted_msg = HideAndSeek().decrypt(signal)
		self.logger.info("Signal Decrypted.")
		# Send to Codesma for further processing
