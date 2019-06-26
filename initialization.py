from components import Lcd
from components import Seven_Segment
from components import Led
from cloud import SignalTransmission


def initiate():
	# led_start = Led().initiate()
	# sevnment_start = Seven_Segment().initiate()
	# GPIO.setmode(GPIO.BOARD)
	# GPIO.setwarnings(False)
	# lcd = Lcd()
	# lcd.display("Hello, Ready for IoT..!!")
	msg = SignalTransmission().send_signal("Hello.....!!!!!")
