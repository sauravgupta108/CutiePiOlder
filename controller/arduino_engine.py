from threading import Thread

from helper import get_logger
from libraries import BluetoothClient


class ArduinoClient(Thread):
	"""
	This will communicate with arduino via bluetooth_engine.py. It creates client to communicate via Bluetooth as
	Threads.
	"""
	def __init__(self, name, method):
		Thread.__init__(self)
		self.logger = get_logger(_type="arduino", name=name)
		self.bluetooth = BluetoothClient()
		self.message = None

		if method not in ("SEND", "RECEIVE"):
			raise ValueError("Invalid method provided.")
		else:
			self.method = method

	def channel_ready(self):
		if self.bluetooth.is_active():
			self.logger.info("Bluetooth is ON. Ready for transmission.")
			return True
		else:
			self.logger.info("Bluetooth is OFF.")
			return False

	def send_signal(self, message):
		if not message:
			self.message = message
			self.logger.error("Bluetooth: Invalid/Null Message Provided.")
			raise ValueError("Cannot Send Empty Message")
		if self.channel_ready():
			Thread.start(self)
		else:
			return False

	def receive_signal(self):
		if self.bluetooth.is_active():
			self.logger.info("Ready for Reception from Arduino")
			Thread.start(self)
			return True
		else:
			self.logger.error("Bluetooth is OFF.")
			return False

	def run(self):
		if self.method == "SEND":
			if self.bluetooth.transmit_signal(self.message):
				self.logger.info("Message Transmitted Successfully.")
			else:
				self.logger.error("Not able to send message to Arduino.")

		elif self.method == "RECEIVE":
			if self.bluetooth.start_receiving():
				self.logger("Bluetooth reception from Arduino started.")
			else:
				self.logger.error("Error during Receiving data from Arduino.")
