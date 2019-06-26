from initialization import Initialization
import RPLCD as RPLCD, time
from RPLCD import CharLCD
import RPi.GPIO as GPIO


if __name__ == "__main__":
	app = Initialization()
	app.activate_receivers()
