import os

from helper import get_logger


class ArduinoSignal:
    
    def __init__(self, signal):
        assert isinstance(signal, str)
        self.signal = signal
        self.entity = None
        self.zone = 0
        self.logger = get_logger(_type="", name=__name__)

    def generate_signal(self):      
        self.logger.info("Generating Signal for Arduino.")
        # TODO: Generate signal for Arduino
        self.logger.info("Signal Generated for Arduino")

    def decode_signal_from_arduino(self):
        self.logger.info("Started Signal interpretation from Arduino.")
        if len(self.signal) == 18:
            self.entity = "light"
        elif len(self.signal) == 12:
            self.entity = "tank"
        else:
            self.entity = "dustbin"

        parts = self.break_signal()
        self.zone = int(parts[0])
        curent_state = self.binary_from_parts(parts[1:])
        self.logger.info("Signal decoded successfully.")
        return tuple(self.zone, self.entity, curent_state)

    def break_signal(self):
        part_signal = [self.signal[i:i+2] for i in range(0, len(self.signal), 2)]
        for i in part_signal[1:]:
            if int(i) < 0 or int(i) >15:
                raise ValueError("Invalid Signal.")
        return part_signal

    def self.binary_from_parts(self, parts):
        binary_data = None
        for i in parts:
            binary_data += bin(i).lstrip("0b")

        return binary_data