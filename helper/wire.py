from threading import Thread


class Wire(Thread):
	def __init__(self):
		Thread.__init__(self)

	def start(self):
		Thread.start(self)

	def run(self):
		pass
