import os
import logging
from datetime import datetime


def get_logger(_type, name="default"):
	"""
	Creates a file handler logger with name 'name'
	:param _type: name of directory where logs has to store
	:param name: name of logger
	:return: logger object
	"""
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler(os.path.join(os.environ["CUTIE_LOG"], _type, datetime.today().strftime(
		'%Y-%m-%d')+".log"))
	formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	return logger
