from cryptography.fernet import Fernet
import os
import json

class HideAndSeek:
	'''
	This class encrypts or decrypts signals
	'''

	def __init__(self):
		pass

	def encrypt(self, raw_signal):
		assert isinstance(raw_signal, str)
		return Fernet(self.get_key()).encypt(raw_signal.encode())

	def decrypt(self, signal):
		assert isinstance(signal, str)
		return Fernet(self.get_key()).decrypt(signal).decode()

	def get_key(self):
		'''
		Returns secret key from configuration file
		'''
		secert_key = None
		try:
			scrt = open('/opt/app/arduino_app/CutiePi/secret/security.json', 'r')
			secert_key = json.loads(scrt.read())["secret_key"]			
		
		except FileNotFoundError: 
			# TODO: log error
			secert_key = None
			
		except Exception as e:
			# TODO: log error
			secert_key = None
					
		finally:
			scrt.close()
			return secret_key
