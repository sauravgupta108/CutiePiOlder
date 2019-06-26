import os

from helper import get_logger


class ArduinoSignal:
	
	def __init__(self):
		self.logger = get_logger(_type="", name=__name__)

	def generate_signal(self, msg):
		assert isinstance(msg, str)
		self.logger.info("Generating Signal for Arduino.")
		# TODO: Generate signal for Arduino
		self.logger.info("Signal Generated for Arduino")

	def decode_signal_from_arduino(self, msg):
		assert isinstance(msg, str)
		self.logger.info("Started Signal interpretation from Arduino.")
		# TODO: Decode signal received from Arduino
		self.logger.info("Signal form Arduino decoded and sent for further processing.")
		# TODO: Send signal for further processing.
