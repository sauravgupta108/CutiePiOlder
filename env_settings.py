import os

os.environ["CUTIE_HOME"] = "/opt/app/arduino_app/CutiePi/"
os.environ["CUTIE_CONFIG"] = os.environ["CUTIE_HOME"] + "config/"
os.environ["CUTIE_SECRET"] = os.environ["CUTIE_HOME"] + "secret/security.json"
os.environ["CUTIE_LOG"] = "/opt/app/arduino_app/logs/"

os.environ["LCD_CONF"] = os.environ["CUTIE_CONFIG"] + "lcd_connection.json"
