from components import Lcd
from components import Seven_Segment
from components import Led
import RPi.GPIO as GPIO

def initiate():
	# led_start = Led().initiate()
	# sevnment_start = Seven_Segment().initiate()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	lcd = Lcd()
	lcd.display("Hello, Ready for IoT..!!")
