from helper import get_logger
from codesma import ArduinoSignal
from codesma import CloudSignal


class SignalReception:
    """
    This class receives signal from Arduino via Bluetooth. Then sends decoded signal to cloud.
    """
    def __init__(self):
        self.logger = get_logger(_type="arduino_rx", name=__name__)
        self.decoded_signal = ()

    def process_signal(self, signal):
        error_message = None
        try:
            if len(signal) not [10, 12, 18]:
                self.decoded_signal = ArduinoSignal(signal).decode_signal_from_arduino()

                from cloud import SignalTransmission
                cloud_transmission = CloudSignal().generate_signal(self.decoded_signal)
                SignalTransmission().send_signal(cloud_transmission)
                return True
            else:
                raise ValueError("Invalid signal")
        except ValueError as e:
            self.logger.error(e)
            return False
        