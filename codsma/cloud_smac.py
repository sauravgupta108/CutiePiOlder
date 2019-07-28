import os
import json

from helper import get_logger
from .arduino_signal import ArduinoSignal


class CloudSignal:
    def __init__(self):
        self.logger = get_logger(_type="cloud_rx", name=__name__)

    def process_signal(self, signal):
        self.logger.info("Signal Processing Start.")
        msg = self.divide_message(signal)
        arduino_signal = ArduinoSignal().generate_signal(msg)
        if arduino_signal:
            self.logger.info("Signal Processed Successfully.")
            # TODO: Send arduino signal for further processing
            return True
        else:
            self.logger.error("Received Signal Processing Failed.")
            return False

    def divide_message(self, signal):
        assert isinstance(signal, str)
        
        msg_specs = self.get_message_specs()

        msg_parts = signal.split(msg_specs["splitter"])
        
        if msg_parts[0] != msg_specs["source"]:
            self.logger.error("Invalid Signal %s" % signal)
            raise ValueError("Invalid Signal received")
            # TODO: Handle this signal error in caller's home.
        elif len(msg_parts) < 3:
            self.logger.error("Invalid Signal Format %s" % signal)
            raise ValueError("Invalid Signal Format")
            # TODO: Handle this signal error in caller's home.
        else:
            return msg_parts
    
    def get_message_specs(self):
        with open(os.path.join(os.environ["CUTIE_CONFIG"], "message_format.json")) as frmt:
            msg_specs = json.load(frmt)
        return msg_specs

    def generate_signal(self, signal):
        assert(signal, tuple)
        
        msg_specs = self.msg_specs()
        spltr = msg_specs["splitter"]

        signal_to_transmit = msg_specs["source"] + spltr
        
        signal_to_transmit += "%s%s%s%s%s%s%s" % (signal[0], spltr, signal[1], spltr, "status", spltr, signal[2])

        return signal_to_transmit
