from cryptography.fernet import Fernet
import os
import json


class HideAndSeek:
	"""
	This class encrypts or decrypts signals
	"""

	def __init__(self):
		pass

	def encrypt(self, raw_signal):
		assert isinstance(raw_signal, str)
		return Fernet(self.get_key().encode()).encrypt(raw_signal.encode()).decode()

	def decrypt(self, signal):
		assert isinstance(signal, str)
		return Fernet(self.get_key()).decrypt(signal).decode()

	def get_key(self):
		"""
		Returns secret key from configuration file
		"""
		# TODO: Change this o get key from env_settings.
		# return os.environ["secret_key"]
		secret_key = None
		try:
			scrt = open('/opt/app/arduino_app/CutiePi/secret/security.json', 'r')
			secret_key = json.load(scrt)["secret_key"]		
		
		except FileNotFoundError:
			secret_key = None
			
		except Exception as e:
			secret_key = None
					
		finally:
			scrt.close()
			return secret_key
