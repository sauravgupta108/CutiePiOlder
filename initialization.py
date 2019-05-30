from components import Lcd
from components import Seven_Segment
from components import Led


def initiate():
	led_start = Led().initiate()
	sevnment_start = Seven_Segment().initiate()
	lcd_start = Lcd().initiate()
	
	return led_start and sevnment_start and lcd_start
