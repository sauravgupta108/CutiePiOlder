import os
import json

from helper import get_logger
from .arduino_signal_generator import ArduinoSignalGenerator


class ProcessRecievedCloudSignal:
	def __init__(self):
		self.logger = get_logger(_type="cloud_rx", name=__name__)

	def pocess_signal(self, signal):
		self.logger.info("Signal Processing Start.")
		msg = self.divide_message(signal)
		arduino_signal = ArduinoSignalGenerator().generate_ard_signal()
		if arduino_signal:
			self.get_logger.info("Signal Processed Successfully.")
			# TODO: Send arduino signal for further processing
			return True
		else:
			self.get_logger.error("Recieved Signal Processing Failed.")
			return False

	def divide_message(self, signal):
		assert isinstance(signal, str)
		
		with open(os.path.join(os.environ["CUTIE_CONFIG"], "message_format.json")) as frmt:
			msg_specs = json.load(frmt)

		msg_parts = signal.split(msg_specs["splitter"])
		
		if msg_parts[0] != msg_specs["source"]:
			self.logger.error("Invalid Signal %s" % signal)
			raise ValueError("Invalid Signal Recieved")
			# TODO: Handle this signal error in caller's home.
		elif len(msg_parts) < 3:
			self.logger.error("Invalid Signal Format %s" % signal)
			raise ValueError("Invalid Signal Format")
			# TODO: Handle this signal error in caller's home.
		else:
			return msg_parts
