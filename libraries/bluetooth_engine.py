from helper import get_logger


class BluetoothClient:
    """
    Class to interface with Arduino using Bluetooth.
    """
    def __init__(self):
        self.logger = get_logger(_type="bluetooth", name=__name__)

    def start(self):
        """
        It switches Bluetooth on and Connect
        :return: True/False if Bluetooth is on and connected.
        """
        pass
        return True

    def is_active(self):
        """
        Check if Bluetooth is On and Connected.
        :return: True/False
        """
        pass
        return True

    def is_connected(self):
        pass

    def transmit_signal(self, signal):
        """
        Transmit signal to Arduino via Bluetooth
        :param signal: signal to transmit
        :return: True/False if signal transmitted.
        """
        pass

    def start_receiving(self):
        """
        Start receiving signal from Arduino via Bluetooth.
        :return: True/False if reception started or not.
        """
        pass

    def connect_to_arduino(self):
        pass

    def disconnect(self):
        pass
