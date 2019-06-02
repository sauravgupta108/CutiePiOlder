from .lcd_engine import LCDEngine


class Lcd(LCDEngine):
	def __init__(self):
		super().__init__()

	def display(self, message):
		toggle_line = 0
		for i in range(len(message)):
			self.print(message[i])
			toggle_line+=1
			if toggle_line == 16:
				self.command(0xC0)
			elif toggle_line == 32:
				self.command(0x80)
				toggle_line = 0
			