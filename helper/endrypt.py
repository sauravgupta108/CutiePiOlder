from cryptography.fernet import Fernet
import os
import json

class HideAndSeek:
	'''
	This class encrypts or decrypts a string
	'''

	def __init__(self, string):
		assert isinstance(string, str)
		self.message = string

	def encrypt(self):
		return Fernet(self.get_key()).encypt(self.message.encode())

	def decrypt(self):
		return Fernet(self.get_key()).decrypt(self.message).decode()

	def get_key(self):
		'''
		Returns encoded secret key from configuration file
		'''
		pass