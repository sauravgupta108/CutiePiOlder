from helper import HideAndSeek
from helper import get_logger


class SignalReception:
    """
    This class receives signals from via MQTT protocol.
    """
    def __init__(self):
        self.logger = get_logger(_type="cloud_rx", name=__name__)

    def decode_signal(self, signal):
        decrypted_signal = HideAndSeek().decrypt(signal)
        self.logger.info("Signal Decrypted.")
        return decrypted_signal

    def verify_recieved_msg(self, signal):
        parts = self.break_signal(signal)
        if len(parts) != 5:
            raise ValueError("Invalid Signal")

    def break_signal(self, signal):
        with open(os.path.join(os.environ["CUTIE_CONFIG"], "message_format.json")) as frmt:
            msg_specs = json.load(frmt)
        return signal.split(msg_specs["splitter"])

    def process_signal(self, signal):
        assert(signal, str)

        decrypted_signal = self.decode_signal()
        is_valid_signal = self.verify_recieved_msg(decrypted_signal)

