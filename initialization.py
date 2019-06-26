import RPi.GPIO as GPIO

from components import Lcd
from components import SevenSegment
from components import Led
from libraries import BluetoothClient
from cloud import SignalTransmission
from helper import get_logger


def initiate():
	# led_start = Led().initiate()
	# sevnment_start = Seven_Segment().initiate()
	# GPIO.setmode(GPIO.BOARD)
	# GPIO.setwarnings(False)
	# lcd = Lcd()
	# lcd.display("Hello, Ready for IoT..!!")
	msg = SignalTransmission().send_signal("Hello.....!!!!!")


class Initialization:
	"""
	This class is for initiation of different parts i.e. components, signal receivers (for Cloud and Arduino.)
	"""
	def __init__(self):
		self.logger = get_logger(_type="start", name=__name__)

		GPIO.setmode(GPIO.BOARD)
		# TODO: Check return type of GPIO.setmode.
		GPIO.setwarnings(False)
		self.logger.info("BOARD mode activated.")

		lcd = Lcd().prepare_lcd()
		if not lcd:
			self.logger.error("Failed to start LCD.")

		sevnment_start = SevenSegment().initiate()
		if not sevnment_start:
			self.logger.error("Failed to start Seven Segment's Section.")

		bluetooth = BluetoothClient().start()
		if not bluetooth:
			self.logger.error("Failed to Activate Bluetooth.")

	@staticmethod
	def activate_receivers():
		from cloud import CloudClient
		from controller import ArduinoClient

		cloud_rx = CloudClient(name="Cloud_RX", client_type="RECEIVE")
		arduino_rx = ArduinoClient(name="Arduino_RX", method="RECEIVE")

		cloud_rx.receive()
		arduino_rx.receive_signal()
