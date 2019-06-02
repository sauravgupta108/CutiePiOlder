import RPi.GPIO as GPIO

import json
import time


class LCDEngine:
	def __init__(self):
		with open("/opt/app/arduino_app/CutiePi/config/lcd_connection.json") as lcd_conn:
			self.__lcd = json.load(lcd_conn)

		self.prepare_lcd()

	def prepare_lcd(self):		
		for pin in self.__lcd.keys():
			GPIO.setup(int(self.__lcd[pin]), GPIO.OUT)
		self.lcd_start()
		self.lcd_clear()
		self.cursor_blink()
		self.go_to_first_line()

	def command(self, command):
		GPIO.output(int(self.__lcd["rs"]), False)
		self.write_8_bit_mode(bin(command))
		self.green_signal()

	def print(self, chr):
		assert len(chr) == 1
		GPIO.output(int(self.__lcd["rs"]), True)
		self.write_8_bit_mode(bin(ord(chr)))
		self.green_signal()

	def write_8_bit_mode(self, bits):		
		bits = self.pad_bits(bits)
		bits = bits[::-1]
		for i in range(8):
			GPIO.output(int(self.__lcd["d" + str(i)]), bool(int(bits[i])))

	def pad_bits(self, bits):
		raw_bits = bits.lstrip('0b')
		assert (8-len(raw_bits)) >= 0
		return '0'*(8-len(raw_bits)) + raw_bits

	def green_signal(self):		
		GPIO.output(int(self.__lcd["en"]), True)
		time.sleep(0.01)
		GPIO.output(int(self.__lcd["en"]), False)

	def lcd_start(self):
		self.command(0x38)

	def lcd_clear(self):
		self.command(0x01)

	def cursor_off(self):
		self.command(0x0c)

	def cursor_blink(self):
		self.command(0x0c)

	def right_shift(self):
		self.command(0x1c)

	def left_shift(self):
		self.command(0x18)

	def go_to_first_line(self):
		self.command(0x80)

	def go_to_second_line(self):
		self.command(0xc0)

	def go_to_position(self, row=1, column=1):
		assert row in [1,2]
		assert column in range(1,17)
		# TODO: add logic for this.
		pass

	def clean(self):
		GPIO.cleanup()